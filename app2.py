from models.post import Post
from database import Database


Database.initialize()

post = Post.from_mongo('629c6c0aa5d545feaa33084ab29f6777')

print(post)

