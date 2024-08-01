from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import ProfileCreationForm

def detail(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    is_self = True if request.user == user else False    

    context = {'user':user, 'is_self':is_self}
    return render(request, 'users/detail.html', context)

@login_required
def my_profile(request):
    user_id = request.user.pk
    return redirect('users:profile-detail', pk=user_id)

class EditBio(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio']
    template_name = 'users/edit_bio.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('posts:home')

#@permission_required("kick_user")
#def kick_user(request):
#    kick_until = request.POST['kick_until']
#    subject = request.POST['subject']

#    subject.kicked_until = kick_until
#    subject.save()

#    return HttpResponse(status_code = 201)

def search_users(request):
    query = request.POST.get('user-search')   

    if not query:
        results = Profile.objects.none() 
    else:
        results = Profile.objects.filter(username__icontains=query)

    return render(request, 'users/search_result.html', { 'results':results })
    

class Register(CreateView):
    form_class = ProfileCreationForm
    template_name = "users/register.html"

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('posts:home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
        
        return response
    
class DeleteProfile(DeleteView):
    model = Profile
    template_name = "users/delete_user.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('posts:home')