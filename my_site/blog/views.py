from django.shortcuts import render
from django.http import request
from datetime import date

posts_list = [
    {
        "slug": "swimming-in-the-sea",
        "image": "me.jpg",
        "author": "me",
        "date": date(2024, 3, 12),
        "title": "usual title",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?",
        "content": """

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?
            """
    },
     {
        "slug": "trip-to-London",
        "image": "other.jpg",
        "author": "someone",
        "date": date(2024, 4, 11),
        "title": "another title",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?",
        "content": """

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?
            """
    },
     {
        "slug": "going-to-downtown",
        "image": "fish.jpg",
        "author": "other",
        "date": date(2024, 5, 12),
        "title": "some title",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?",
        "content": """

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo fugiat exercitationem inventore repellendus impedit earum, sunt eligendi repudiandae aperiam ullam culpa explicabo facilis suscipit consectetur ratione magni sequi a dolor?
            """
    }
]

def get_date(post):
    return post.get('date')

# Create your views here.

def starting_page(request):
    posts_list.sort(key=get_date)
    latest_posts = posts_list[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": posts_list
    })

def post_detail(request, slug):
    identified_post = next(post for post in posts_list if post['slug'] == slug)
    return render(request, "blog/post-detail.html",
                  {"post": identified_post})