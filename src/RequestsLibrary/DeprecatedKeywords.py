from RequestsLibrary import utils
from .SessionKeywords import SessionKeywords


class DeprecatedKeywords(SessionKeywords):

    def get_request(
            self,
            alias,
            uri,
            headers=None,
            data=None,
            json=None,
            params=None,
            allow_redirects=None,
            timeout=None):
        """ Send a GET request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the GET request to

        ``params`` url parameters to append to the uri

        ``headers`` a dictionary of headers to use with the request

        ``data`` a dictionary of key-value pairs that will be urlencoded
               and sent as GET data
               or binary data that is sent as the raw body content

        ``json`` a value that will be json encoded
               and sent as GET data if data is not specified

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects

        response = self._common_request(
            "get",
            session,
            uri,
            params=params,
            headers=headers,
            data=data,
            json=json,
            allow_redirects=redir,
            timeout=timeout)

        return response

    def post_request(
            self,
            alias,
            uri,
            data=None,
            json=None,
            params=None,
            headers=None,
            files=None,
            allow_redirects=None,
            timeout=None):
        """ Send a POST request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the POST request to

        ``data`` a dictionary of key-value pairs that will be urlencoded
               and sent as POST data
               or binary data that is sent as the raw body content
               or passed as such for multipart form data if ``files`` is also defined
               or file descriptor retrieved by Get File For Streaming Upload

        ``json`` a value that will be json encoded
               and sent as POST data if files or data is not specified

        ``params`` url parameters to append to the uri

        ``headers`` a dictionary of headers to use with the request

        ``files`` a dictionary of file names containing file data to POST to the server

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        if not files:
            data = utils.format_data_according_to_header(session, data, headers)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects

        response = self._common_request(
            "post",
            session,
            uri,
            data=data,
            json=json,
            params=params,
            files=files,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)
        return response

    def patch_request(
            self,
            alias,
            uri,
            data=None,
            json=None,
            params=None,
            headers=None,
            files=None,
            allow_redirects=None,
            timeout=None):
        """ Send a PATCH request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the PATCH request to

        ``data`` a dictionary of key-value pairs that will be urlencoded
               and sent as PATCH data
               or binary data that is sent as the raw body content
               or file descriptor retrieved by Get File For Streaming Upload

        ``json`` a value that will be json encoded
               and sent as PATCH data if data is not specified

        ``headers`` a dictionary of headers to use with the request

        ``files`` a dictionary of file names containing file data to PATCH to the server

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``params`` url parameters to append to the uri

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        data = utils.format_data_according_to_header(session, data, headers)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects

        response = self._common_request(
            "patch",
            session,
            uri,
            data=data,
            json=json,
            params=params,
            files=files,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)

        return response

    def put_request(
            self,
            alias,
            uri,
            data=None,
            json=None,
            params=None,
            files=None,
            headers=None,
            allow_redirects=None,
            timeout=None):
        """ Send a PUT request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the PUT request to

        ``data`` a dictionary of key-value pairs that will be urlencoded
               and sent as PUT data
               or binary data that is sent as the raw body content
               or file descriptor retrieved by Get File For Streaming Upload

        ``json`` a value that will be json encoded
               and sent as PUT data if data is not specified

        ``headers`` a dictionary of headers to use with the request

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``params`` url parameters to append to the uri

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        data = utils.format_data_according_to_header(session, data, headers)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects

        response = self._common_request(
            "put",
            session,
            uri,
            data=data,
            json=json,
            params=params,
            files=files,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)

        return response

    def delete_request(
            self,
            alias,
            uri,
            data=None,
            json=None,
            params=None,
            headers=None,
            allow_redirects=None,
            timeout=None):
        """ Send a DELETE request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the DELETE request to

        ``json`` a value that will be json encoded
               and sent as request data if data is not specified

        ``headers`` a dictionary of headers to use with the request

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        data = utils.format_data_according_to_header(session, data, headers)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects

        response = self._common_request(
            "delete",
            session,
            uri,
            data=data,
            json=json,
            params=params,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)

        return response

    def head_request(
            self,
            alias,
            uri,
            headers=None,
            allow_redirects=None,
            timeout=None):
        """ Send a HEAD request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the HEAD request to

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``headers`` a dictionary of headers to use with the request

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = False if allow_redirects is None else allow_redirects
        response = self._common_request(
            "head",
            session,
            uri,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)

        return response

    def options_request(
            self,
            alias,
            uri,
            headers=None,
            allow_redirects=None,
            timeout=None):
        """ Send an OPTIONS request on the session object found using the
        given `alias`

        ``alias`` that will be used to identify the Session object in the cache

        ``uri`` to send the OPTIONS request to

        ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed.

        ``headers`` a dictionary of headers to use with the request

        ``timeout`` connection timeout
        """
        session = self._cache.switch(alias)
        # XXX workaround to restore library default behaviour. Not needed in new keywords
        redir = True if allow_redirects is None else allow_redirects
        response = self._common_request(
            "options",
            session,
            uri,
            headers=headers,
            allow_redirects=redir,
            timeout=timeout)

        return response
