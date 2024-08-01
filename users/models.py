from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Profile(AbstractUser):
    bio = models.CharField('User Biography', max_length=60, default='No Biography.', blank=True)
    following = models.ManyToManyField('self', verbose_name='User Following List', related_name='followers', blank=True, symmetrical=False)
    pic = models.ImageField('User Profile Image', upload_to='profile_pics/', height_field=400, width_field=400, max_length=100)
    kicked_until = models.DateField('kicked until', blank=True, null=True)

    class Meta:
         permissions = [
              ("kick_user", "Can kick users"),
         ]

    def is_kicked(self):
        if self.kicked_until < timezone.now():
             self.kicked_until = None
             self.save()
             return False
        return True

    def __str__(self) -> str:
        return self.username
    
    def get_friends(self) -> list:
        friends = []
        for follow in self.following.all():
                if follow in self.followers.all():
                    friends += follow
        return friends
    
class Report(models.Model):
     subject = models.ForeignKey("users.Profile", verbose_name="Report of", on_delete=models.CASCADE, related_name="reports")
     reporter = models.ForeignKey("users.Profile", verbose_name="Report by", on_delete=models.PROTECT, related_name="made_reports")
     content = models.TextField("Report Content")
     reviewed = models.BooleanField("Is reviewed", blank=True, default=False)

    
