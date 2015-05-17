"""
Example showing the Request class which wraps the "environ" dictionary to ease
the access to informatio about the HTTP request.
"""


class Request:
    def __init__(self, environ):
        self.path = environ['REQUEST_URI']

        self.GET = {}
        for element in environ['QUERY_STRING'].split('&'):
            if element:
                key, value = element.split('=')
                self.GET[key] = value

        body = b''
        for line in environ['wsgi.input']:
            body += line
        self.body = body.decode('utf-8')

        self.POST = {}
        for element in self.body.split('&'):
            if element:
                key, value = element.split('=')
                self.POST[key] = value


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    request = Request(environ)

    response_body = 'PATH: {}\nGET: {}\nPOST: {}'.format(
        request.path, request.GET, request.POST)

    return [response_body.encode('utf-8')]
