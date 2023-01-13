import json


class PostsHandler:
    def __init__(self, path):
        self.path = path

    def load_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_posts(self, substr):
        posts = []

        for post in self.load_json():
            if substr.lower() in post['content'].lower():
                posts.append(post)

        return posts

    def save_post_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        posts = self.load_json()
        posts.append(post)
        self.save_post_to_json(posts)
