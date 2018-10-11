from ..base import Base
from sqlalchemy import Table, Column, Integer, PrimaryKey
from sqlalchemy.orm import relationship

class CFR(Base):

    __tablename__ = 'cfr_page_urls'

