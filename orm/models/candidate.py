from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

candidate_donor_assoc = Tables('candidate_donor_assoc', Base.metadata,
        Column('candidate_id', Integer, ForeignKey('candidate.id')),
        Column('donor_id', Integer, ForeignKey('donor.id')))

class Candidate(Base):

    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    name_id = Column(Integer, nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    crri_page = relationship('crri_page_urls', uselist=False, back_populates='Candidate')
    cfr_pages = relationship('cfr_page_urls')

