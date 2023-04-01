from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import AbstractUser, Group



class Clientadapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        client = Group.objects.get_or_create(name="Client")
        user.role=client
        user.save()


