""" Example showing simple web application, compatible with WSGI.
"""

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'<h1>Hello, World!</h1>']
