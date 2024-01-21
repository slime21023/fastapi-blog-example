from fastapi import FastAPI
from .routers import auth, blog, user

app = FastAPI()


@app.get('/health')
def health():
    return 'OK'

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)