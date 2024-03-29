#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests

if __name__ == "__main__":
    request = requests.get('https://alx-intranet.hbtn.io/status')
    text = request.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(text), text))
