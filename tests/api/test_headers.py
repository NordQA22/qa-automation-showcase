import allure
import pytest
from api_clients.posts_client import PostsClient


@pytest.fixture
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()


@allure.feature("Headers API")
@allure.story("Response headers")
@allure.title("Response has correct Content-Type header")
@allure.severity(allure.severity_level.NORMAL)
def test_response_content_type(posts_client):
    """Проверяем, что API возвращает JSON."""
    response = posts_client.get_post(1)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]


@allure.feature("Headers API")
@allure.story("Request headers")
@allure.title("Session sends Content-Type on POST")
@allure.severity(allure.severity_level.MINOR)
def test_post_sends_json_content_type(posts_client):
    """Проверяем, что клиент отправляет JSON."""
    response = posts_client.create_post(
        title="Header Test",
        body="Testing headers",
        user_id=1
    )

    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]
