from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint
from fastapi import File, UploadFile
import base64


class Token(BaseModel):
    access_token: str
    token_type : str


class TokenData(BaseModel):
    id : Optional[int] = None

class UserBase(BaseModel):
    email : EmailStr
    name : str
    

class UserCreate(UserBase):
    password: str
    phone: Optional[str] = None
    
class UserOut(UserBase):
    id : int
    phone: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    isAdmin: bool
    
    class Config:
        from_attributes = True
     


class HeroImage(BaseModel):
    pass
    
class HeroImageCreate(BaseModel):
    altText: str
    image: UploadFile

class HeroImageOut(HeroImage):
    id : int
    active : bool
    # image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    

    class Config:
        from_attributes = True


class HeroBackgroundImageDB(BaseModel):
    id : int
    active : bool
    altText : str
    image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        
        
        
class CricketBackgroundImage(BaseModel):
    pass
    
class CricketBackgroundImageCreate(CricketBackgroundImage):
    altText: str
    image: UploadFile

class CricketBackgroundImageOut(CricketBackgroundImage):
    id : int
    active : bool
    # image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        

class CricketBackgroundImageDB(BaseModel):
    id : int
    active : bool
    altText : str
    image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        
        
class FootballBackgroundImage(BaseModel):
    pass
    
class FootballBackgroundImageCreate(FootballBackgroundImage):
    altText: str
    image: UploadFile

class FootballBackgroundImageOut(FootballBackgroundImage):
    id : int
    active : bool
    # image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        
        
class FootballBackgroundImageDB(BaseModel):
    id : int
    active : bool
    altText : str
    image : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        
        
class Review(BaseModel):
    pass
    
class ReviewCreate(Review):
    match_id : str
    content : str

class ReviewOut(Review):
    id : int
    match_id : str
    content : str
    created_at : datetime
    updated_at : datetime
    user : UserOut
    
    class Config:
        from_attributes = True
        
        

