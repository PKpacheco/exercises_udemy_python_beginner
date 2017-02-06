from database import Database
from post import Post

import pymongo


uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)

Database.initialize()


post = Post(blog_id="123",
            title="Another great post",
            content="This is some sample content",
            author="Joseph")
post.save_to_mongo()
