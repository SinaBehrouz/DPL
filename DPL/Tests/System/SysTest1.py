from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)()

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    email = Column(String(120))
    first_name = Column(String(20))
    last_name = Column(String(20))
    password = Column(String(20))
    phone_number = Column(String(16))
    postal_code = Column(String(10))
    Dplstation = Column(Integer, ForeignKey('dplstations.station_id'))
    users_deliveries = relationship('Deliveries', backref='User', lazy=True)

class DPLstations(Base):
    __tablename__ = "dplstations"
    station_id = Column(Integer, primary_key=True)
    city = Column(String(20))
    address = Column(String(60))
    total_lockers = Column(Integer)
    lockers_available = Column(Integer)
    postal_code =Column(String(6))
    owner_id = Column(Integer, ForeignKey('user.uid'))
    def __repr__(self):
        return f"email={self.email}, user_del={self.users_deliveries}"


class Deliveries(Base):
    # passcode = [DPL_id(2)] + [locker_num(2)] + [random number(6)]
    __tablename__ = "deliveries"
    delivery_id = Column(Integer, primary_key = True)
    tracking_number = Column(String(40))
    status = Column(Integer) #change this to an enum
    passcode =  Column(String(10))
    to_customer = Column(Integer, ForeignKey('user.uid'), nullable=False)

    def __repr__(self):
        return f"--did={self.delivery_id}, user_id={self.to_customer}--"

def fill():
    Base.metadata.create_all(engine)
    Session.add(DPLstations(station_id=1, city="Vancouver"))
    Session.add(DPLstations(station_id=2, city="Toronto"))
    Session.add(DPLstations(station_id=3, city="NY"))
    Session.add(DPLstations(station_id=4, city="LA"))

    Session.add(User(email="a@a.com",Dplstation=1 ))
    Session.add(User(email="b@b.com",Dplstation=2 ))
    Session.add(User(email="c@c.com",Dplstation=2 ))
    Session.add(User(email="d@d.com",Dplstation=1 ))
    Session.add(User(email="e@e.com",Dplstation=1 ))

    Session.add(Deliveries(to_customer=1,passcode="11111"))
    Session.add(Deliveries(to_customer=1,passcode="11112"))
    Session.add(Deliveries(to_customer=1,passcode="11113"))
    Session.add(Deliveries(to_customer=2,passcode="11114"))
    Session.add(Deliveries(to_customer=3,passcode="11115"))
    Session.add(Deliveries(to_customer=4,passcode="11116"))

    Session.commit()

def checkpasscode(_passcode):
    query = Session.query(Deliveries).filter_by(passcode = _passcode).first()
