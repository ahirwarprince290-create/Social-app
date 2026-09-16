from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Follow

router = APIRouter(prefix="/social", tags=["Social"])

@router.post("/follow")
def follow(follower_id: int, following_id: int, db: Session = Depends(get_db)):
    if follower_id == following_id:
        raise HTTPException(status_code=400, detail="Cannot follow yourself")
    
    follow_rec = Follow(follower_id=follower_id, following_id=following_id)
    db.add(follow_rec)
    db.commit()
    return {"message": f"User {follower_id} followed {following_id}"}
  
