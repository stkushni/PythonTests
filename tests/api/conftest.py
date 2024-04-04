import json
import pytest
import requests
from assertpy import assert_that
from models.user_model import UserModel
from test_data.urls import base_url
from test_data.users_data import user_data


@pytest.fixture
def create_user(request):
    user_name = request.param
    post_data = user_data[user_name]
    response = requests.post(base_url, json=post_data)
    assert_that(response.status_code).is_equal_to(200).described_as(
        f"Failed to create user: {response.text}"
    )
    yield post_data


# TODO: remove user


@pytest.fixture
def get_user(create_user):
    user_name = create_user["username"]
    url = f"{base_url}/{user_name}"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200).described_as(
        f"Failed to create user: {response.text}"
    )

    try:
        parsed_response = UserModel.parse_obj(response.json())
    except Exception as e:
        assert False, f"Failed to parse JSON: {e}"

    yield parsed_response
