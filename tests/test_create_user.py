import pytest
from assertpy import assert_that


@pytest.mark.parametrize("create_user", ["SuperMacho2"], indirect=True)
def test_user_data(create_user, get_user):
    expected_user = create_user
    user = get_user
    assert_that(user.id).is_not_none().described_as("User ID is None")
    assert_that(expected_user["username"]).is_equal_to(user.username)
    assert_that(expected_user["firstName"]).is_equal_to(user.firstName)
    assert_that(expected_user["lastName"]).is_equal_to(user.lastName)
