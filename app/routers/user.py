from .. import models, schemas , utils,oauth2
from fastapi import Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
import base64


router = APIRouter(
    prefix= "/users",
    tags=['Users']
)

#forgot password and recovery
# @router.post("/forgot_password/", status_code=status.HTTP_200_OK)
# def forgot_password(data:schemas.ForgotPassword,db: Session = Depends(get_db)) -> Response:

#     user = db.query(models.User).filter(models.User.email == data.email).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{data.email} not registered")

#     send_email.send_pass_recovery_email(user.user_id,data.email)

#     return f"Recovery email sent to {data.email}"


@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




#create an endpoint to see current_user details from the token received in the header
@router.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    return current_user


@router.get("/main_background_image", response_model=schemas.HeroBackgroundImageDB)
def get_main_background_image(db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    hero_image = db.query(models.MainBackgroundImage).order_by(models.MainBackgroundImage.id.desc()).first()
    
    if hero_image:
        # Encode the image binary data to base64
        image_base64 = base64.b64encode(hero_image.image).decode('utf-8')
        
        return schemas.HeroBackgroundImageDB(
            id=hero_image.id,
            active=hero_image.active,
            image=image_base64,  # Use the base64 encoded image
            altText=hero_image.altText,
            created_at=hero_image.created_at,
            updated_at=hero_image.updated_at,
            user=hero_image.user
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active main background image found")

@router.get("/cricket_background_image",response_model=schemas.CricketBackgroundImageDB)
def get_cricket_background_image(db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    cricket_image = db.query(models.CricketBackgroundImage).order_by(models.CricketBackgroundImage.id.desc()).first()
    
    if cricket_image:
        # Encode the image binary data to base64
        image_base64 = base64.b64encode(cricket_image.image).decode('utf-8')
        
        return schemas.CricketBackgroundImageDB(
            id=cricket_image.id,
            active=cricket_image.active,
            image=image_base64,  # Use the base64 encoded image
            altText=cricket_image.altText,
            created_at=cricket_image.created_at,
            updated_at=cricket_image.updated_at,
            user=cricket_image.user
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active cricket background image found")
    
    
@router.get("/football_background_image",response_model=schemas.FootballBackgroundImageDB)
def get_football_background_image(db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    football_image = db.query(models.FootballBackgroundImage).order_by(models.FootballBackgroundImage.id.desc()).first()

    if football_image:
        # Encode the image binary data to base64
        image_base64 = base64.b64encode(football_image.image).decode('utf-8')
        
        return schemas.FootballBackgroundImageDB(
            id=football_image.id,
            active=football_image.active,
            image=image_base64,  # Use the base64 encoded image
            altText=football_image.altText,
            created_at=football_image.created_at,
            updated_at=football_image.updated_at,
            user=football_image.user
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active football background image found")
    
    
@router.get("/reviews",response_model=List[schemas.ReviewOut])
async def get_reviews(db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    reviews = db.query(models.Review).all()
    return reviews

