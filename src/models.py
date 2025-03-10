import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    # Datos del Usuario
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True) 
    name = Column(String(60), unique=False, nullable=False)
    last_name = Column(String(60), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(60), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    password_reset = Column(String(4), unique=True, nullable=True)
    password_reset_date = Column(String(120), unique=True, nullable=True)
    phone_number = Column(String(20), unique=True, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)

    
    #Foreign keys
    favorites = relationship("Favorites", back_populates = "user", lazy = True)
    comments = relationship("Comments", back_populates = "user", lazy = True)
    post = relationship("Post", back_populates = "user", lazy = True)


class Comments(Base):
    # Datos del Hotel
    __tablename__ = 'comments'
    id_comment = Column(Integer, primary_key=True) 
    user_comments = Column(Integer, ForeignKey(User.id_user))
    user = relationship(User)
    content = Column(String(140), nullable= False)
    date = Column(DateTime, nullable = False)

class Post(Base):
    __tablename__ = 'post'
    id_post = Column(Integer, primary_key=True) 
    user_post = Column(Integer, ForeignKey(User.id_user))
    user = relationship(User)
    content = Column(String(140), nullable= False)
    image_url = Column(String(140), nullable= False)
    date = Column(DateTime, nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id_favorites = Column(Integer, primary_key=True) 
    user_favorites = Column(Integer, ForeignKey(User.id_user))
    user = relationship(User)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
