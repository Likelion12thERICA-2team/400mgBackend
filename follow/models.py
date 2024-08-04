# accounts/models.py
from django.db import models
from users.models import CustomUser

class Follow(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    follower = models.ForeignKey(CustomUser, related_name='follow', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follower')  # Ensures a user cannot follow another user multiple times

    def __str__(self):
        return f"{self.follower} follows {self.user}"
