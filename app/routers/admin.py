from .. import models, schemas , utils,oauth2
from fastapi import Response,status,HTTPException,Depends,APIRouter,File, UploadFile, Form
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(
    prefix= "/admin",
    tags=['Admin']
)



@router.post("/hero_image_update", status_code=status.HTTP_201_CREATED, response_model=schemas.HeroImageOut)
async def hero_image_update(
    altText: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Read the contents of the uploaded file
    image_contents = await image.read()

    # Create a new MainBackgroundImage instance
    new_hero_image = models.MainBackgroundImage(
        image=image_contents,
        altText=altText,
        user_id=current_user.id
    )

    # Add to database
    db.add(new_hero_image)
    db.commit()
    db.refresh(new_hero_image)

    # Return the created image data
    return new_hero_image



@router.post("/cricket_image_update", status_code=status.HTTP_201_CREATED, response_model=schemas.CricketBackgroundImageOut)
async def cricket_image_update(
    altText: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Check if the user is an admin (you need to implement this logic)
    if current_user.isAdmin == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Read the contents of the uploaded file
    image_contents = await image.read()

    # Create a new CricketBackgroundImage instance
    new_cricket_image = models.CricketBackgroundImage(
        image=image_contents,
        altText=altText,
        user_id=current_user.id
    )

    # Add to database
    db.add(new_cricket_image)
    db.commit()
    db.refresh(new_cricket_image)

    # Return the created image data
    return new_cricket_image


@router.post("/football_image_update", status_code=status.HTTP_201_CREATED, response_model=schemas.FootballBackgroundImageOut)
async def football_image_update(
    altText: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Check if the user is an admin (you need to implement this logic)
    if current_user.isAdmin == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Read the contents of the uploaded file
    image_contents = await image.read()

    # Create a new FootballBackgroundImage instance
    new_football_image = models.FootballBackgroundImage(
        image=image_contents,
        altText=altText,
        user_id=current_user.id
    )

    # Add to database
    db.add(new_football_image)
    db.commit()
    db.refresh(new_football_image)

    # Return the created image data
    return new_football_image


@router.post("/post_review", status_code=status.HTTP_201_CREATED, response_model=schemas.ReviewOut)
async def post_review(
    review_data: schemas.ReviewCreate,  # Accept HTML content as a string
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Create a new Review instance using data from the request body
    new_review = models.Review(
        match_id=review_data.match_id,
        content=review_data.content,  # Store the raw HTML content
        user_id=current_user.id
    )

    # Add to the database
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    # Return the created review data
    return new_review



@router.get("/users", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.get("reviews", response_model=List[schemas.ReviewOut])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).offset(skip).limit(limit).all()
    return reviews

