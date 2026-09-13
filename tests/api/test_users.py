import allure
import pytest
from api_clients.posts_client import PostsClient


@pytest.fixture
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()


@allure.feature("Users API")
@allure.story("GET user")
@allure.title("GET /users/1 returns user with nested objects")
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_returns_nested_objects(posts_client):
    """Проверяем, что пользователь содержит вложенные объекты."""
    response = posts_client.get_user(1)

    assert response.status_code == 200
    user = response.json()

    assert user["id"] == 1
    assert "name" in user
    assert "email" in user

    # Вложенные объекты
    assert "address" in user
    assert "city" in user["address"]
    assert "geo" in user["address"]
    assert "lat" in user["address"]["geo"]

    assert "company" in user
    assert "name" in user["company"]


@allure.feature("Users API")
@allure.story("GET user")
@allure.title("GET /users/1 returns correct email format")
@allure.severity(allure.severity_level.MINOR)
def test_user_email_has_correct_format(posts_client):
    """Проверяем формат email пользователя."""
    response = posts_client.get_user(1)
    user = response.json()

    assert "@" in user["email"]
    assert "." in user["email"]


@allure.feature("Users API")
@allure.story("GET user")
@allure.title("GET /users/99999 returns 404")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_user_returns_404(posts_client):
    """Несуществующий пользователь возвращает 404."""
    response = posts_client.get_user(99999)
    assert response.status_code == 404
    