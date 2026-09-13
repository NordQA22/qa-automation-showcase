import allure
import pytest
from api_clients.posts_client import PostsClient


@pytest.fixture
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()


@allure.feature("Filtering API")
@allure.story("Filter posts by user")
@allure.title("GET /posts?userId=1 returns only posts of user 1")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_posts_by_user(posts_client):
    """Фильтрация постов по userId."""
    response = posts_client.get_posts_by_user(1)

    assert response.status_code == 200
    posts = response.json()

    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


@allure.feature("Filtering API")
@allure.story("Filter comments by post")
@allure.title("GET /comments?postId=1 returns comments for post 1")
@allure.severity(allure.severity_level.NORMAL)
def test_get_comments_by_post(posts_client):
    """Фильтрация комментариев по postId."""
    response = posts_client.get_comments_by_post(1)

    assert response.status_code == 200
    comments = response.json()

    assert len(comments) > 0
    assert all(comment["postId"] == 1 for comment in comments)


@allure.feature("Filtering API")
@allure.story("Filter posts by user")
@allure.title("Each user has 10 posts")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_each_user_has_ten_posts(posts_client, user_id):
    """У каждого пользователя ровно 10 постов."""
    response = posts_client.get_posts_by_user(user_id)
    posts = response.json()

    assert len(posts) == 10
    