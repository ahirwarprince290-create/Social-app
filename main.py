from fastapi import FastAPI
from database import engine, Base
import models
from routers import auth, posts, follows

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Media API")

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Social Media API Server Active!",
        "docs": "/docs"
    }

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(follows.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
