# import pymongo
from models.post import Post
from database import Database


# mongodb commands
# show dbs
# use fullstack
# show collections
# db.students.insert({"name": "Oren", "mark": 99})
# db.students.remove({"name": "Oren"})
# db.students.find({})

# address of Mongodb instance
# uri = "mongodb://127.0.0.1:27017"
#
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
#
# # finds all the data in the collection
# students = [student['mark'] for student in collection.find({})]
#
# print(students)

# db.posts.find({}).pretty()


Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            content="This is some sample content",
            author="Oren")

post.save_to_mongo()

