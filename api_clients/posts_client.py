import requests
from config.settings import JSONPLACEHOLDER_BASE_URL


class PostsClient:
    """Клиент для работы с JSONPlaceholder API."""

    BASE_URL = JSONPLACEHOLDER_BASE_URL

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_post(self, post_id: int):
        return self.session.get(f"{self.BASE_URL}/posts/{post_id}")

    def get_all_posts(self):
        return self.session.get(f"{self.BASE_URL}/posts")

    def get_posts_by_user(self, user_id: int):
        """GET /posts?userId=1 — посты конкретного пользователя."""
        return self.session.get(
            f"{self.BASE_URL}/posts",
            params={"userId": user_id}
        )

    def get_comments_by_post(self, post_id: int):
        """GET /comments?postId=1 — комментарии к посту."""
        return self.session.get(
            f"{self.BASE_URL}/comments",
            params={"postId": post_id}
        )

    def get_user(self, user_id: int):
        """GET /users/1 — пользователь с вложенными объектами."""
        return self.session.get(f"{self.BASE_URL}/users/{user_id}")

    def create_post(self, title: str, body: str, user_id: int):
        return self.session.post(
            f"{self.BASE_URL}/posts",
            json={"title": title, "body": body, "userId": user_id}
        )

    def update_post(self, post_id: int, **kwargs):
        return self.session.put(f"{self.BASE_URL}/posts/{post_id}", json=kwargs)

    def delete_post(self, post_id: int):
        return self.session.delete(f"{self.BASE_URL}/posts/{post_id}")
    