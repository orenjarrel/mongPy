from models.post import Post
from database import Database


Database.initialize()


posts = Post.from_blog('321')

for post in posts:
    print(post)