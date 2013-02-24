import datetime
from lxml import etree
import requests
from alexa import SERVICE_HOST, SECRET_ACCESS_KEY, ACCESS_KEY_ID
from signer import RequestSigner


class Request(object):
    def __init__(self):
        self.signer = RequestSigner(SECRET_ACCESS_KEY)

    def _request(self, **kwargs):
        kwargs['AWSAccessKeyId'] = ACCESS_KEY_ID
        kwargs['Timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        kwargs['SignatureMethod'] = 'HmacSHA1'
        kwargs['SignatureVersion'] = 2
        kwargs['Signature'] = self.signer.sign(kwargs)
        query_str = self.signer.build_query_str(kwargs)
        request = requests.get('http://%s/?%s' % (SERVICE_HOST, query_str))
        return request.text

    def sites(self, query):
        text = self._request(**query)
        root = etree.fromstring(text)
        xpath = etree.XPathEvaluator(root)
        xpath.register_namespace('aws', 'http://awis.amazonaws.com/doc/2005-07-11')
        for site in xpath('//aws:DataUrl'):
            yield site.text

