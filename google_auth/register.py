from django.contrib.auth import authenticate
from authentication.models import User
import os
from rest_framework.exceptions import AuthenticationFailed


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        print(f"User with email {email} exists.")  
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(email=email, password=os.environ.get('SOCIAL_SECRET'))
            print(f"Authenticated existing user: {registered_user.username}")  
            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()
            }
        else:
            print(f"Authentication failed: Existing user uses a different provider.") 
            raise AuthenticationFailed(detail=f'Please continue your login using {filtered_user_by_email[0].auth_provider}')
    else:
        print(f"Creating new user with email {email}") 
        user = {
            'username': email,
            'email': email,
            'password': os.environ.get('SOCIAL_SECRET')
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        new_user = authenticate(email=email, password=os.environ.get('SOCIAL_SECRET'))
        print(f"Created and authenticated new user: {new_user.username}") 
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }
