""" init_db.py """

from database import engine, Base
from models import User, Order

Base.metadat.create_all(bind=engine)
