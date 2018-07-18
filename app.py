# from models.post import Post
from database import Database
from models.blog import Blog




Database.initialize()

blog = Blog(author="Oren",
            title="Another great post",
            description="Sample description")


blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())

