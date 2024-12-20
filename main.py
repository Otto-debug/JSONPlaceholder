import requests
import pytest

def test_status_code():
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert req.status_code == 200
    print(req.text)

