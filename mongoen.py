from mongoengine import *
from datetime import datetime
import os

# future notice
######################################
######################################
# connect(
#     db = "example-db-name",
#     username = "root",
#     password = "example1234",
#     authentication_source = "admin",
#     host = "localhost",
#     port = 27017
# )
######################################
######################################

connect("mongo-dev-db")

# Defining documents

class User(Document):
    username = StringField(uniwue = True, required = True)
    email = EmailField(unique = True)
    password = BinaryField(required = True)
    age = IntField()
    bio = StringField(max_length = 100)
    categories = ListField(StringField())
    admin = BooleanField(default = False)
    registered = BooleanField(default = False)   
    date_created = DateTimeField(default = datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "admin": self.admin,
            "registered": self.registered,
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-date_created"]
    }

# Dynamic documents

class BlogPost(DynamicDocument):
    title = StringField()
    content = StringField()
    author = ReferenceField(User)
    date_created = DateTimeField(default = datetime.utcnow)

    meta = {
        "indexes": ["title"],
        "ordering": ["-date_created"]
    }

######################################
# Save a document
######################################

user = User(
    username = "JohnDoe",
    email = "jdoe@gmail.com",
    password = os.urandom(16),
    age = 32,
    bio = "Hello World",
    admin = True
).save()

BlogPost(
    title = " My first blog post!",
    content = "MongoDB and Python",
    author = user,
    tags = ["Python", "MongoDB", "MongoEngine"],
    category = " MongoDB"
).save()

# print("Done")

######################################
# saving it differently than above
######################################

user = User(
    username = "PeterPan",
    email = "ppan@gmail.com",
    password = os.urandom(16),
    age = 32,
    bio = "Forever young",
)

user.admin = True
user.registered = True

try:
    user.save()
except NotUniqueError:
    print("Username or email is not unique")

######################################
# Quering the database
######################################

users = User.objects()

print(users)



