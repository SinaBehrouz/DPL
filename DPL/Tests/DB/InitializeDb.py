from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#echo is used for purpose of logging
engine = create_engine('sqlite:///dbFile.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)()

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    password = Column(String(20))
    phone_number = Column(String(16))
    postal_code = Column(String(10))
    Dplstation = Column(Integer, ForeignKey('dplstations.station_id', ondelete='SET NULL') )
    users_deliveries = relationship('Deliveries', backref='User', lazy=True)

class DPLstations(Base):
    __tablename__ = "dplstations"
    station_id = Column(Integer, primary_key=True)
    city = Column(String(20))
    address = Column(String(60))
    total_lockers = Column(Integer)
    lockers_available = Column(Integer)
    postal_code =Column(String(6))
    owner_id = Column(Integer, ForeignKey('user.uid', ondelete='CASCADE'))
    def __repr__(self):
        return f"email={self.email}, user_del={self.users_deliveries}"


class Deliveries(Base):
    # passcode = [DPL_id(2)] + [locker_num(2)] + [random number(6)]
    __tablename__ = "deliveries"
    delivery_id = Column(Integer, primary_key = True)
    tracking_number = Column(String(40))
    status = Column(Integer)
    # (registered=0, delivered=1, pickedup=2, .... )
    passcode =  Column(String(10))
    to_customer = Column(Integer, ForeignKey('user.uid', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"--did={self.delivery_id}, user_id={self.to_customer}--"

Base.metadata.create_all(engine)
