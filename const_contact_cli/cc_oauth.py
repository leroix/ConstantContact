import json
import oauth2 as oauth
from urllib import quote

class CC_OAuth(object):
    cc_authorize_uri = 'https://oauth2.constantcontact.com/oauth2/oauth/siteowner/authorize'
    cc_access_token_uri = 'https://oauth2.constantcontact.com/oauth2/oauth/token'

    def __init__(self, settings, redirect_uri, *args, **kwargs):
        self.client_id = getattr(settings, 'CC_KEY', None)
        self.client_secret = getattr(settings, 'CC_SECRET', None)
        self.redirect_uri = quote(redirect_uri, '')
        self.client = oauth.Client(oauth.Consumer(key=self.client_id,
                       secret=self.client_secret))

        if not self.client_id:
            raise ImproperlyConfigured("Missing Key settings.")
        if not self.client_secret:
            raise ImproperlyConfigured("Missing Secret")
        if not self.redirect_uri:
            raise ImproperlyConfigured("Missing Redirect URI")

    def _params(self, code):
        return u'grant_type=%s&client_id=%s&client_secret=%s&code=%s&redirect_uri=%s' % (
                'authorization_code', self.client_id, self.client_secret,
                code, self.redirect_uri)

    def authenticate(self, code):
        response = {}
        resp, content = self.client.request(self.cc_access_token_uri,
                        'POST', self._params(code))
        response.update(json.loads(content))

        return response

    def authorize_url(self):
        return u'%s?response_type=code&client_id=%s&redirect_uri=%s' % (
           self.cc_authorize_uri, self.client_id, self.redirect_uri)
