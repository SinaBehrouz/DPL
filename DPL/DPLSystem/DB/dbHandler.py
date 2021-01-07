from .models import User, Deliveries, DPLstations
from . import Session

class dbHandler():
    def get_delivery_by_passcode(self,passcode):
        '''
            checks the given _passcode to see if it belongs to any of the deliveries
            if it exists then it will return the delivery_id of the delivery
            otherwise it will return None
        '''
        return Session.query(Deliveries).filter_by(passcode=passcode).first()

    def get_delivery_by_trackingNumber(self,trackingNumber):
        '''
            checks the given _tracking_number to see if it belongs to any of the deliveries
            if it exists then it will return the delivery_id of the delivery
            otherwise it will return None
        '''
        return Session.query(Deliveries).filter_by(tracking_number=trackingNumber).first()

    def update_delivery_status(self, delivery_id, status):
        delivery = Session.query(Deliveries).filter_by(delivery_id=delivery_id).first()
        delivery.status = status
        Session.commit()

    def update_locker_state(self, locker_num, state):
        '''
            takes in locker_num and state and changes the bit value in the
            station.lockers_available.
            For simplicty locker_num is in the range of [0, station.total_lockers-1]
            upon successs return True else return False
        '''
        try:
            station = Session.query(Dplstations).filter_by(station_id=1).first()
        except:
            print("can not find the table")
            return False
        if locker_num >= station.total_lockers or locker_num < 0:
            print("invalid locker_num -- return False")
            return False
        if state == "available":
            station.lockers_available | (1<<locker_num)
        elif state == "unavailable":
            station.lockers_available & ~(1<<locker_num)
        Session.commit()
        return True

    def testFunc(self, x):
        query = Session.query(Deliveries).filter_by(delivery_id=x).first()
        print(query)
        if not query:
            return -1
        return query.delivery_id

    def get_delivery_by_trackingNumber_test(self,trackingNumber):
        '''
            test function that returns test Tracking Number
        '''
        return "0812442025424"
