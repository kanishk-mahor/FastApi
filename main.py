from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_user():
    return {"message": "Welcome to Api"}


@app.get("/posts")
def get_posts():
    return {"data: Posts triggered"}
