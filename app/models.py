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
    
    reviews = relationship("Review", back_populates="user")
    main_background_images = relationship("MainBackgroundImage", back_populates="user")
    cricket_background_images = relationship("CricketBackgroundImage", back_populates="user")
    football_background_images = relationship("FootballBackgroundImage", back_populates="user")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, nullable=False)
    match_id = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="reviews")

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