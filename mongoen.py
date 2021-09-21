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

for user in users:
    print(user.username, user.email, user.bio)

# Filtering

admin_user = User.objects(admin = True)

for a in admin_user:
    print(a.username)

admin_user = User.objects(admin = True, registered = True)

for a in admin_user:
    print(a.username)

# getting an uique result
john_doe = User.objects(username = "JohnDoe").get()
print(john_doe.username, john_doe.email)


john_doe = User.objects(username = "JohnDoe").get()

posts = BlogPost.objects(author = john_doe)
for post in posts:
    print(post.author.username)

# getting the json file for username john doe
print(john_doe.json())


######################################
# Query operators
######################################

# Less than & greater than

young_users = User.obejects(age__lt = 50)

for user in young_users:
    print(user.username, user.age)


older_users = User.obejects(age__gte = 30)

for user in older_users:
    print(user.username, user.age)


# Query that is in a list

posts_tagged_python = BlogPost.objects(tags = "Python")

for post in posts_tagged_python:
    print(post.content)

posts_tagged_python = BlogPost.objects(tags__in = ["Python", "MongoDB"])

for post in posts_tagged_python:
    print(post.content)

# String queries
python_posts = BlogPost.objects(content__icontains = "Python")

for post in python_posts:
    print(post.content)

python_posts = BlogPost.objects(title__icontains = "fourth")

for post in python_posts:
    print(post.title)

######################################
# Limiting and skipping results
######################################
# Gte the first

first = BlogPost.obhects().first()

print(first.title)

# Get the first 2 documents

first_2 = BlogPost.objects()[:2]

for post in first_2:
    print(post.title)

all_but = BlogPost.objects()[2:]
for post in all_but:
    print(post.title)

sliced = BlogPost.objects()[2:4]
for post in sliced:
    print(post.title)


######################################
# Counting
######################################

user_count = User.objects().count()

print(user_count)

######################################
# Aggregation
######################################

average = BlogPost.objects.average("rating")
print(average)

total_rating = BlogPost.objects.sum("rating")
print(total_rating)



