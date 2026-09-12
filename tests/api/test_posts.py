import pytest
from api_clients.posts_client import PostsClient

pytestmark = pytest.mark.api

@pytest.fixture
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()


def test_get_post_returns_200(posts_client):
    """GET /posts/1 возвращает 200 и корректные данные."""
    response = posts_client.get_post(1)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body


def test_get_all_posts_returns_list(posts_client):
    """GET /posts возвращает список из 100 постов."""
    response = posts_client.get_all_posts()

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100


def test_create_post(posts_client):
    """POST /posts создаёт новый пост."""
    response = posts_client.create_post(
        title="QA Test Post",
        body="This is a test post from automation",
        user_id=1
    )

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "QA Test Post"
    assert body["userId"] == 1
    assert "id" in body


def test_update_post(posts_client):
    """PUT /posts/1 обновляет пост."""
    response = posts_client.update_post(1, title="Updated Title")

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_post(posts_client):
    """DELETE /posts/1 возвращает 200."""
    response = posts_client.delete_post(1)

    assert response.status_code == 200


@pytest.mark.parametrize("post_id,expected_status", [
    (1, 200),
    (100, 200),
    (99999, 404),
])
def test_get_post_status_codes(posts_client, post_id, expected_status):
    """Параметризованная проверка статус-кодов."""
    response = posts_client.get_post(post_id)
    assert response.status_code == expected_status


def test_post_has_correct_structure(posts_client):
    """Проверяем структуру ответа."""
    response = posts_client.get_post(1)
    body = response.json()

    required_fields = {"userId", "id", "title", "body"}
    assert required_fields.issubset(body.keys())
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str)
