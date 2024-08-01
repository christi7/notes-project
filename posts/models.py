from django.db import models

class Post(models.Model):
    image = models.ImageField("Post Image Content", upload_to="post_image/", max_length=100, blank=True, null=True)
    content = models.TextField("Post Content")
    poster = models.ForeignKey("users.Profile", verbose_name="Posted by", on_delete=models.CASCADE, related_name="posts")
    parent = models.ForeignKey("self", verbose_name="Reply of", on_delete=models.CASCADE, related_name="replies", blank=True, null=True)
    likers = models.ManyToManyField("users.Profile", verbose_name="Liked by", related_name="liked_posts", blank=True)
    creation_date = models.DateTimeField("created at",  auto_now_add=True)
    
    def __str__(self) -> str:
        return self.content
