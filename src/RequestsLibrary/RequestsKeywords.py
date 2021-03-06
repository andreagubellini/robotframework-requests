import json

import robot
from robot.api import logger
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.utils.asserts import assert_equal

from RequestsLibrary import utils
from RequestsLibrary.compat import PY3


class RequestsKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self._cache = robot.utils.ConnectionCache('No sessions created')
        self.builtin = BuiltIn()
        self.debug = 0

    @keyword("Status Should Be")
    def status_should_be(self, expected_status, response, msg=None):
        """
        Fails if response status code is different than the expected.

        ``expected_status`` could be the code number as an integer or as string.
        But it could also be a named status code like 'ok', 'created', 'accepted' or
        'bad request', 'not found' etc.

        The ``response`` is the output of other requests keywords like ``Get Request``.

        A custom message ``msg`` can be added to work like built-in keywords.
        """
        self._check_status(expected_status, response, msg)

    @keyword("Request Should Be Successful")
    def request_should_be_successful(self, response):
        """
        Fails if response status code is a client or server error (4xx, 5xx).

        The ``response`` is the output of other requests keywords like ``Get Request``.

        In case of failure an HTTPError will be automatically raised.
        """
        self._check_status(None, response, msg=None)

    @staticmethod
    @keyword("Get File For Streaming Upload")
    def get_file_for_streaming_upload(path):
        """
        Opens and returns a file descriptor of a specified file to be passed as ``data`` parameter
        to other requests keywords.

        This allows streaming upload of large files without reading them into memory.

        File descriptor is binary mode and read only. Requests keywords will automatically close the file,
        if used outside this library it's up to the caller to close it.
        """
        return open(path, 'rb')

    @keyword("To Json")
    def to_json(self, content, pretty_print=False):
        """ 
        WARNING: This keyword has been deprecated. Please use ${resp.json()} instead.

        Convert a string to a JSON object

        ``content`` String content to convert into JSON

        ``pretty_print`` If defined, will output JSON is pretty print format
        """
        if PY3:
            if isinstance(content, bytes):
                content = content.decode(encoding='utf-8')
        if pretty_print:
            json_ = utils.json_pretty_print(content)
        else:
            json_ = json.loads(content)
        logger.info('To JSON using : content=%s ' % (content))
        logger.info('To JSON using : pretty_print=%s ' % (pretty_print))
        logger.console('WARNING: This keyword has been deprecated. Please use ${resp.json()} instead.')
        return json_
