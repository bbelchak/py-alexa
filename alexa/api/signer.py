import hashlib
import base64
import hmac
import urllib

from alexa import SERVICE_HOST, SECRET_ACCESS_KEY


class RequestSigner(object):
    def __init__(self, secret_access_key):
        """
        Set up the RequestSigner.

        :param secret_access_key:

        """
        self.secret_key = secret_access_key

    def sign(self, query):
        """
        Sign the provided query string.

        :param query:
        :return: b64encoded signature

        """
        if not SECRET_ACCESS_KEY:
            raise RuntimeError("SECRET_ACCESS_KEY is not set!")

        query_str = self.build_query_str(query)
        sign_str = "GET\n%s\n/\n%s" % (SERVICE_HOST, query_str)
        mac = hmac.new(SECRET_ACCESS_KEY, sign_str.encode("utf-8"), hashlib.sha1)
        computed = base64.b64encode(mac.digest()).strip()
        return computed

    def build_query_str(self, query):
        """
        Build a query string from a ``dict``

        :param query: ``dict`` containing the query parameters
        :return: a url-encoded query string

        """
        return "&".join(["%s=%s" % (urllib.quote_plus(k), urllib.quote_plus(str(v))) for k, v in sorted(query.items())])
