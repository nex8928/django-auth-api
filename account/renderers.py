from rest_framework import renderers
import json

class UserRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        # Check if data contains errors by looking for 'errors' or checking if it's a dict of field errors
        if isinstance(data, dict) and ('errors' in data or any(key in data for key in ['email', 'name', 'password', 'password2', 'terms_conditions'])):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps(data)
        return response
