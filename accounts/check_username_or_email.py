import re
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def check_username_or_email(email_or_username):
    if bool(re.search(r"^[\w.-]+@[\w.-]+.\w+$", email_or_username)):
        try:
            user_request = get_object_or_404(
                    User,
                    email=email_or_username,
            )
            if user_request:
                return user_request.username
        except: 
            return False
        finally:
            if User.objects.filter(username=email_or_username).exists():
                return email_or_username
    else:
        if User.objects.filter(username=email_or_username).exists():
            return email_or_username
        else:
            return False
