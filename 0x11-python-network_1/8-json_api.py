#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": letter}

    body = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        res = body.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
