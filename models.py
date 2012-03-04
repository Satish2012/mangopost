import transaction
from sqlalchemy import Column
from sqlalchemy import Integer, DateTime
from sqlalchemy import Unicode, String, Text
from sqlalchemy import Table, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID
import uuid, datetime, time, hashlib

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(Unicode(2048))
    created = Column(DateTime(), default=datetime.datetime.now())

    # board comments = 1 - many

    # pin comments = 1 - many

class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag = Column(Unicode(2048))
    created = Column(DateTime(), default=datetime.datetime.now())

    # board tags = many - many

    # pin tags = many - many

class Pins(Base):
    __tablename__ = 'pins'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime(), default=datetime.datetime.now())
    title = Column(Unicode(255), unique=True)

    # url to the location of the pic
    pin = Column(String)

    # Author ==> 1:1 mapping for the author

    # Tags ==> many:many for the pins

    # likes ==> many:many for the users

    # comments ==> 1:many for comments on the entity


class Boards(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime(), default=datetime.datetime.now())
    title = Column(Unicode(255), unique=True)
    description = Column(Unicode(2048))
    # Author ==> 1:1 mapping for the author

    # Pins ==> 1:many for the pins

    # Tags ==> many:many for the pins

    # likes ==> many:many for the users

    # comments ==> 1:many for comments on the entity


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Unicode(255), unique=True)
    firstname = Column(Unicode(255))
    refresh_token = Column(Unicode(255))
    picurl = Column(String)

    # Pins ==> 1:many for the pins

    # Tags ==> many:many for the pins

    # likes ==> many:many for the users

    # comments ==> 1:many for comments on the entity

    # followers ==> 1:many for the users

    # boards ==> 1:many for the users