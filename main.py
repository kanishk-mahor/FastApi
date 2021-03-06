from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def get_user():
    return {"message": "Welcome to Api"}


@app.get("/posts")
def get_posts():
    return {"data: Posts triggered"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "new_post"}
