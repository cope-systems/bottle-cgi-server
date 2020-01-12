__version__ = (0, 1, 0)

import logging
import subprocess
import os
from six.moves.urllib_parse import urljoin
from bottle import HTTPResponse

plugin_logger = logging.getLogger(__name__)


class CGIServerPlugin(object):
    name = 'cgi-server'
    api = 2

    def __init__(self, base_url, cgi_directory):
        self.base_url = base_url
        self.cgi_directory = cgi_directory

    def apply(self, callback, route):
        return callback

    def setup(self, app):
        app.route(urljoin(self.base_url, "<path:path>"))(self._handle)

    def _handle(self, path):
        # result = subprocess.check_output([os.path.join(self.cgi_directory, path)])
        # return HTTPResponse(body=result)
        return ""
