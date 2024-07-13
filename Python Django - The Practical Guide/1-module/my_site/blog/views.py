from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "download1.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
    {
        "slug": "travel-on-the-world",
        "image": "download.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 22),
        "title": "travel cool",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
    {
        "slug": "move-on-to-another-coutre",
        "image": "download.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 23),
        "title": "journay great",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "download1.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 24),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
    {
        "slug": "travel-on-the-world",
        "image": "download.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 25),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
    {
        "slug": "move-on-to-another-coutre",
        "image": "download.jpeg",
        "author": "villefort",
        "data": date(2021, 7, 26),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate totam eaque nemo assumenda at\
            sint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
        "content": "    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id alias omnis cupiditate\
            totam eaque nemo assumenda atint, beatae maiores, in tempora laudantium quis quo, repudiandae fuga reprehenderit accusantium suscipit.",
    },
]


def sorted_value(value):
    return value["data"]


# Create your views here.
def starting_page(request):
    sorted_posts: list = sorted(all_posts, key=lambda x: x["data"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    print("sdsds")
    print(request.path)
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
