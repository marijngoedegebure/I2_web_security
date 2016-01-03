from unsafe.models import UnsafeUser
from django.contrib.auth.models import User


class UnsafeAuthBackend(object):
    def authenticate(self, username=None, password=None):
        # Check the username/password and return a User.
        sql = "SELECT * FROM auth_user au, unsafe_unsafeuser uu WHERE au.id = uu.user_id AND au.username='{0}' AND uu.plaintext_password='{1}'".format(username, password)
        unsafe_user_query_set = UnsafeUser.objects.raw(sql)
        unsafe_user = unsafe_user_query_set[0]
        return unsafe_user.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
