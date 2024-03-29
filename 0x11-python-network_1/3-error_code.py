#!/usr/bin/python3

"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""

if __name__ == '__main__':
    from urllib import request, error
    import sys

    argz = = sys.argz
    url = argz[1]

    try:
        with request.urlopen(url) as response:
            request = response.read().decode('utf-8')
            print("Response body:")
            print(request)
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
