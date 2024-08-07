#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.HTTPError as e:
        print("Error code:", e.code)
