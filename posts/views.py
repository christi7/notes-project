from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return redirect('posts:home')

class Home(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = '-creation_date'

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(parent=None)
    

    #remember to add pagination

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    replies = post.replies.all()

    context = {'post':post, 'replies':replies}
    return render(request, 'posts/detail.html', context)

@login_required
def create_reply(request):
    content = request.POST['content']
    post_id = request.POST['post_id']
    parent = Post.objects.get(pk=post_id)
    user = request.user

    Post.objects.create(poster=user, parent=parent, content=content)

    return redirect('posts:post-detail', pk=post_id)

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']
    template_name = 'posts/create_post.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('posts:home')
    
    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)
    
class PostDelete(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('posts:home')
 
def like_post(request, pk):
    user = request.user

    if not user.is_authenticated:
        next = request.GET.get("next", settings.LOGIN_REDIRECT_URL)
        if 'HX-Request' in request.headers:
            response = HttpResponse(status=200)
            response['HX-Redirect'] = reverse_lazy('users:login')
            return response
        return redirect('users:login', next=next)

    post = get_object_or_404(Post, pk=pk)

    if post.likers.contains(user):
        post.likers.remove(user)
        return render(request, 'posts/likes.html', {'post':post})
    else:
        post.likers.add(user)
        return render(request, 'posts/likes.html', {'post':post})

    