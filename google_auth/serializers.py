from rest_framework import serializers
from .google import Google
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)
        try:
            user_data['sub']
        except KeyError:
            print('KeyError: sub not found in user_data') 
            raise serializers.ValidationError('The token is invalid or expired. Please login again.')

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            print(f"Invalid client ID: {user_data['aud']} != {os.environ.get('GOOGLE_CLIENT_ID')}")
            raise AuthenticationFailed('Invalid client ID.')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        print(f"User data: user_id={user_id}, email={email}, name={name}, provider={provider}") 

        return register_social_user(provider=provider, user_id=user_id, email=email, name=name)
