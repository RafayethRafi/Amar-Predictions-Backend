from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey, JSON, LargeBinary
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    isAdmin = Column(Boolean, server_default='FALSE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    # reviews = relationship("Review", back_populates="user")
    cricket_reviews = relationship("CricketReview", back_populates="user")
    football_reviews = relationship("FootballReview", back_populates="user")
    main_background_images = relationship("MainBackgroundImage", back_populates="user")
    cricket_background_images = relationship("CricketBackgroundImage", back_populates="user")
    football_background_images = relationship("FootballBackgroundImage", back_populates="user")
    leagues = relationship("League", back_populates="user")

# class Review(Base):
#     __tablename__ = "reviews"

#     id = Column(Integer, primary_key=True, nullable=False)
#     match_id = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
#     user = relationship("User", back_populates="reviews")

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    logo = Column(LargeBinary, nullable=True)
    sport_type = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="leagues")
    # cricket_reviews = relationship("CricketReview", back_populates="league")
    # football_reviews = relationship("FootballReview", back_populates="league")
    

class CricketReview(Base):
    __tablename__ = "cricket_reviews"

    id = Column(Integer, primary_key=True, nullable=False)
    team1 = Column(String, nullable=False)
    team2 = Column(String, nullable=False)
    score1 = Column(Integer, nullable=True)
    score2 = Column(Integer, nullable=True)
    wicket1 = Column(Integer, nullable=True)
    wicket2 = Column(Integer, nullable=True)
    content = Column(String, nullable=False)
    match_type = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="cricket_reviews")
    # league = relationship("League", back_populates="cricket_reviews")
    
class FootballReview(Base):
    __tablename__ = "football_reviews"

    id = Column(Integer, primary_key=True, nullable=False)
    team1 = Column(String, nullable=False)
    team2 = Column(String, nullable=False)
    score1 = Column(Integer, nullable=True)
    score2 = Column(Integer, nullable=True)
    content = Column(String, nullable=False)
    match_type = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id", ondelete="CASCADE"), nullable=False)
    
    
    user = relationship("User", back_populates="football_reviews")
    # league = relationship("League", back_populates="football_reviews")
    

class MainBackgroundImage(Base):
    __tablename__ = "main_background_images"

    id = Column(Integer, primary_key=True, nullable=False)
    image = Column(LargeBinary, nullable=False)
    altText = Column(String, nullable=True)
    active = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="main_background_images")

class CricketBackgroundImage(Base):
    __tablename__ = "cricket_background_images"

    id = Column(Integer, primary_key=True, nullable=False)
    image = Column(LargeBinary, nullable=False)
    altText = Column(String, nullable=True)
    active = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="cricket_background_images")

class FootballBackgroundImage(Base):
    __tablename__ = "football_background_images"

    id = Column(Integer, primary_key=True, nullable=False)
    image = Column(LargeBinary, nullable=False)
    altText = Column(String, nullable=True)
    active = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="football_background_images")