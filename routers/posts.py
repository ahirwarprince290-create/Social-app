from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from models import Post
from pydantic import BaseModel

router = APIRouter(prefix="/posts", tags=["Posts"])

class PostCreate(BaseModel):
    user_id: int
    content: str

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post_data: PostCreate, db: Session = Depends(get_db)):
    post = Post(user_id=post_data.user_id, content=post_data.content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"message": "Post published", "post_id": post.id}

@router.get("/feed/{user_id}")
def get_feed(user_id: int, limit: int = 10, db: Session = Depends(get_db)):
    posts = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .order_by(Post.created_at.desc())
        .limit(limit)
        .all()
    )
    return {"user_id": user_id, "posts": posts}
  
