from server import create_server
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

session_maker = sessionmaker(bind=create_engine(os.getenv("DB_URL")))


server = create_server(session_maker=session_maker)
