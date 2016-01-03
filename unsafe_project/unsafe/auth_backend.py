from unsafe.models import UnsafeUser
from django.contrib.auth.models import User


class UnsafeAuthBackend(object):
    def authenticate(self, username=None, password=None):
        # Check the username/password and return a User.
        unsafe_user = UnsafeUser.objects.get(user__username=username, plaintext_password=password)
        return unsafe_user.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
