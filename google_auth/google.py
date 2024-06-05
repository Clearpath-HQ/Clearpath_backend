from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import serializers, status

class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        Validate method queries the Google OAuth2 API to fetch the user info
        """
        try:
            # Allow a small clock skew of 2 seconds
            idinfo = id_token.verify_oauth2_token(auth_token, requests.Request(), clock_skew_in_seconds=5)
            if 'accounts.google.com' in idinfo['iss']:
                print(f"Token validated successfully: {idinfo}")  # Debugging log
                return idinfo
        except Exception as e:
            print(f"Token validation error: {e}")  # Debugging log
            raise serializers.ValidationError('The token is either invalid or has expired.')
