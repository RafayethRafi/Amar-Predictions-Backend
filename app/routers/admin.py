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


# @router.post("/post_review", status_code=status.HTTP_201_CREATED, response_model=schemas.ReviewOut)
# async def post_review(
#     review_data: schemas.ReviewCreate,  # Accept HTML content as a string
#     db: Session = Depends(get_db),
#     current_user: schemas.UserOut = Depends(oauth2.get_current_user)
# ):
#     # Create a new Review instance using data from the request body
#     new_review = models.Review(
#         match_id=review_data.match_id,
#         content=review_data.content,  # Store the raw HTML content
#         user_id=current_user.id
#     )

#     # Add to the database
#     db.add(new_review)
#     db.commit()
#     db.refresh(new_review)

#     # Return the created review data
#     return new_review



@router.post("/post_cricket_review", status_code=status.HTTP_201_CREATED, response_model=schemas.CricketReviewOut)
async def post_cricket_review(
    review_data: schemas.CricketReviewCreate,  # Accept HTML content as a string
    league_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Create a new CricketReview instance using data from the request body
    new_cricket_review = models.CricketReview(
        team1=review_data.team1,
        team2=review_data.team2,
        score1=review_data.score1,
        score2=review_data.score2,
        wicket1=review_data.wicket1,
        wicket2=review_data.wicket2,
        content=review_data.content,  # Store the raw HTML content
        user_id=current_user.id,
        league_id=league_id
    )

    # Add to the database
    db.add(new_cricket_review)
    db.commit()
    db.refresh(new_cricket_review)

    # Return the created review data
    return new_cricket_review


@router.post("/edit_cricket_review", status_code=status.HTTP_201_CREATED, response_model=schemas.CricketReviewOut)
async def edit_cricket_review(
    review_data: schemas.CricketReviewCreate,  # Accept HTML content as a string
    review_id_to_edit: int,
    # league_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the review to edit
    review_to_edit = db.query(models.CricketReview).filter(models.CricketReview.id == review_id_to_edit).first()

    # Check if the review exists
    if not review_to_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")

    # Update the review data
    review_to_edit.team1 = review_data.team1
    review_to_edit.team2 = review_data.team2
    review_to_edit.score1 = review_data.score1
    review_to_edit.score2 = review_data.score2
    review_to_edit.wicket1 = review_data.wicket1
    review_to_edit.wicket2 = review_data.wicket2
    review_to_edit.content = review_data.content
    # review_to_edit.league_id = league_id

    # Commit the changes
    db.commit()

    # Return the updated review data
    return review_to_edit

    
    



@router.post("/post_football_review", status_code=status.HTTP_201_CREATED, response_model=schemas.FootballReviewOut)
async def post_football_review(
    review_data: schemas.FootballReviewCreate,  # Accept HTML content as a string
    league_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Create a new FootballReview instance using data from the request body
    new_football_review = models.FootballReview(
        team1=review_data.team1,
        team2=review_data.team2,
        score1=review_data.score1,
        score2=review_data.score2,
        content=review_data.content,  # Store the raw HTML content
        user_id=current_user.id,
        league_id=league_id
    )

    # Add to the database
    db.add(new_football_review)
    db.commit()
    db.refresh(new_football_review)

    # Return the created review data
    return new_football_review


@router.post("/edit_football_review", status_code=status.HTTP_201_CREATED, response_model=schemas.FootballReviewOut)
async def edit_football_review(
    review_data: schemas.FootballReviewCreate,  # Accept HTML content as a string
    review_id_to_edit: int,
    # league_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the review to edit
    review_to_edit = db.query(models.FootballReview).filter(models.FootballReview.id == review_id_to_edit).first()

    # Check if the review exists
    if not review_to_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")

    # Update the review data
    review_to_edit.team1 = review_data.team1
    review_to_edit.team2 = review_data.team2
    review_to_edit.score1 = review_data.score1
    review_to_edit.score2 = review_data.score2
    review_to_edit.content = review_data.content
    # review_to_edit.league_id = league_id

    # Commit the changes
    db.commit()

    # Return the updated review data
    return review_to_edit




@router.get("/users", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# @router.get("reviews", response_model=List[schemas.ReviewOut])
# def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     reviews = db.query(models.Review).offset(skip).limit(limit).all()
#     return reviews


@router.get("/cricket_reviews", response_model=List[schemas.CricketReviewOut])
def read_cricket_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cricket_reviews = db.query(models.CricketReview).order_by(models.CricketReview.id.desc()).offset(skip).limit(limit).all()
    return cricket_reviews


@router.get("/football_reviews", response_model=List[schemas.FootballReviewOut])
def read_football_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    football_reviews = db.query(models.FootballReview).order_by(models.FootballReview.id.desc()).offset(skip).limit(limit).all()
    return football_reviews



@router.post("/create_league", status_code=status.HTTP_201_CREATED, response_model=schemas.LeagueOut)
def create_league(league_data: schemas.LeagueCreate, db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Create a new League instance
    new_league = models.League(
        name=league_data.name,
        sport_type=league_data.sport_type,
        user_id=current_user.id
    )

    # Add to the database
    db.add(new_league)
    db.commit()
    db.refresh(new_league)

    # Return the created league data
    return new_league

@router.get("/leagues", response_model=List[schemas.LeagueOut])
def read_leagues(db: Session = Depends(get_db)):
    leagues = db.query(models.League).all()
    
    if not leagues:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Leagues not found")
    
    return leagues


# edit league
@router.post("/edit_league", status_code=status.HTTP_201_CREATED, response_model=schemas.LeagueOut)
def edit_league(league_data: schemas.LeagueCreate, league_id_to_edit: int, db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the league to edit
    league_to_edit = db.query(models.League).filter(models.League.id == league_id_to_edit).first()

    # Check if the league exists
    if not league_to_edit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="League not found")

    # Update the league data
    league_to_edit.name = league_data.name
    league_to_edit.sport_type = league_data.sport_type

    # Commit the changes
    db.commit()

    # Return the updated league data
    return league_to_edit


# delete league
@router.delete("/delete_league", status_code=status.HTTP_204_NO_CONTENT)
def delete_league(league_id_to_delete: int, db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the league to delete
    league_to_delete = db.query(models.League).filter(models.League.id == league_id_to_delete).first()

    # Check if the league exists
    if not league_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="League not found")

    # Delete the league
    db.delete(league_to_delete)
    db.commit()

    return {"message": "League deleted successfully"}



# get a league and its reviews
@router.get("/league/{league_id}", response_model=schemas.LeagueOut)
def read_league(league_id: int, db: Session = Depends(get_db)):
    league = db.query(models.League).filter(models.League.id == league_id).first()
    
    if not league:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="League not found")
    
    return league


# delete review
@router.delete("/delete_cricket_review", status_code=status.HTTP_204_NO_CONTENT)
def delete_cricket_review(review_id_to_delete: int, db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the review to delete
    review_to_delete = db.query(models.CricketReview).filter(models.CricketReview.id == review_id_to_delete).first()

    # Check if the review exists
    if not review_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")

    # Delete the review
    db.delete(review_to_delete)
    db.commit()

    return {"message": "Review deleted successfully"}


# delete review
@router.delete("/delete_football_review", status_code=status.HTTP_204_NO_CONTENT)
def delete_football_review(review_id_to_delete: int, db: Session = Depends(get_db), current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
    # Check if the user is an admin
    if not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not an admin")

    # Get the review to delete
    review_to_delete = db.query(models.FootballReview).filter(models.FootballReview.id == review_id_to_delete).first()

    # Check if the review exists
    if not review_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")

    # Delete the review
    db.delete(review_to_delete)
    db.commit()

    return {"message": "Review deleted successfully"}


#get a review
@router.get("/cricket_review/{review_id}", response_model=schemas.CricketReviewOut)
def read_cricket_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.CricketReview).filter(models.CricketReview.id == review_id).first()
    
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    
    return review

#get a review
@router.get("/football_review/{review_id}", response_model=schemas.FootballReviewOut)
def read_football_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.FootballReview).filter(models.FootballReview.id == review_id).first()
    
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    
    return review

