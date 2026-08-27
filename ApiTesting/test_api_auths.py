import base64
import os

import pytest
from playwright.sync_api import Playwright


# 1) Basic Authentication 1
# url: https://httpbin.org/basic-auth/user/pass
# username: user
# password : pass
def test_basic_auth(playwright: Playwright):
    request_context = playwright.request.new_context()

    credentials = base64.b64encode(b"user:pass").decode("utf-8")

    response = request_context.get("https://httpbin.org/basic-auth/user/pass",
                                   headers={"Authorization": f"Basic {credentials}"}
                                   )
    assert response.status == 200
    response_body = response.json()
    print("Response body:", response_body)

    request_context.dispose()


# 2) Basic Authentication 2
# url: http://the-internet.herokuapp.com/basic_auth
# username: admin
# password : admin
def test_basic_auth(playwright: Playwright):
    request_context = playwright.request.new_context()

    credentials = base64.b64encode(b"admin:admin").decode("utf-8")

    response = request_context.get("http://the-internet.herokuapp.com/basic_auth",
                                   headers={"Authorization": f"Basic {credentials}"}
                                   )
    assert response.status == 200
    response_body = response.text()
    print("Response body:", response_body)

    request_context.dispose()


# 3) Bearer Token Authentication
# url: https://api.github.com/user/repos

def test_bearer_token_auth_github_repos(playwright: Playwright):
    token = os.getenv("GITHUB_TOKEN")

    print("Token exists:", token is not None)
    print("Token length:", len(token) if token else 0)

    request_context = playwright.request.new_context()
    response = request_context.get("https://api.github.com/user/repos",
                                   headers={"Authorization": f"Bearer {token}"}
                                   )
    assert response.status == 200
    response_body = response.json()

    print("Response Body(Repositories....)", response_body)


# 4) Bearer Token Authentication
# url: https://api.github.com/user

def test_bearer_token_auth_github_repos(playwright: Playwright):


    token = os.getenv("GITHUB_TOKEN")
    print("Token exists:", token is not None)
    print("Token length:", len(token) if token else 0)

    request_context = playwright.request.new_context()
    response = request_context.get("https://api.github.com/user",
                                   headers={"Authorization": f"Bearer {token}"}
                                   )
    assert response.status == 200
    response_body = response.json()

    print("Response Body(User details.....)", response_body)


#5) API_key authentication - weather API

def test_api_key_auth_openweather(playwright: Playwright):
    request_context = playwright.request.new_context()

    query_params= {
        "q": "Coimbatore",
        "appid": "a26b94bb142e59f9b22f5dd713dee602"

    }

    response = request_context.get("https://api.openweathermap.org/data/2.5/weather", params=query_params)

    assert response.status == 200
    response_body = response.json()

    print("Weather Info--->", response_body)

    request_context.dispose()








    








