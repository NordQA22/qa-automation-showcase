import requests


class PostsClient:
    """Клиент для работы с JSONPlaceholder API."""

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get_post(self, post_id: int):
        return self.session.get(f"{self.BASE_URL}/posts/{post_id}")

    def get_all_posts(self):
        return self.session.get(f"{self.BASE_URL}/posts")

    def create_post(self, title: str, body: str, user_id: int):
        return self.session.post(
            f"{self.BASE_URL}/posts",
            json={"title": title, "body": body, "userId": user_id}
        )

    def update_post(self, post_id: int, **kwargs):
        return self.session.put(f"{self.BASE_URL}/posts/{post_id}", json=kwargs)

    def delete_post(self, post_id: int):
        return self.session.delete(f"{self.BASE_URL}/posts/{post_id}")
