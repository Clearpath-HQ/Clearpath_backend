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
            idinfo = id_token.verify_oauth2_token(auth_token, requests.Request(), clock_skew_in_seconds=5)

            # Acceptable issuer URLs
            valid_issuers = [
                'https://accounts.google.com',
                'accounts.google.com'
            ]

            # matching value issuers
            if idinfo['iss'] not in valid_issuers:
                raise serializers.ValidationError('Invalid token issuer.')

            print(f"Token validated successfully: {idinfo}") 
            return idinfo

        except ValueError as ve:
            raise serializers.ValidationError('The token is either invalid or has expired.')

        except Exception as e:
            # error handling
            print(f"Token validation error: {e}")  
            raise serializers.ValidationError('An error occurred during token validation.')
