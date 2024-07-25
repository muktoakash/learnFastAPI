""" database.py """

from sqlalchemy import create_engine
from sqlalchemy.orm import declaritive_base, sessionmaker

# Hide password
engine = create_engine('postgresql:://postgres:password@localhost/pizza_delivery',
                       echo = True
                       )

Base = declaritive_base()

Session = sessionmaker()
