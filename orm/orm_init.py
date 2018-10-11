from sqlalchemy import create_engine
from models.root_url import Url, Base

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
