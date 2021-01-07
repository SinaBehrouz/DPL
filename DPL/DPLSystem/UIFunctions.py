from .DB.dbHandler import dbHandler
from .HAL.slaveController import slaveController
import os

class UIHandler():
    def __init__(self):
        self.db = dbHandler()
        self.slaveCntr = slaveController()
    def __del__(self):
        pass
    def verifyPasscode(self, passcode_list):
        '''
            checks the user passcode to make sure it matches a delivery, if it does
            it'll return True else return False
            - verify passcode with DB
            - unlock the locker (idk how to check if its locked)
            - change the state of t
        '''
        passcode = "".join([el for el in passcode_list])
        if not self.db.get_delivery_by_passcode(passcode):
            return False
        locker_num = int(passcode[2:4])
        if not self.slaveCntr.unlock_lock(locker_num):
            print("something went wrong with the slave controller")
            return False

        delivery=self.db.get_delivery_by_passcode(passcode)
        self.db.update_delivery_status(delivery.delivery_id, 2)
        self.db.update_locker_state(locker_num,"available")
        #push to servers?
        return True

    def wait_till_locker_closes(self,passcode):
        '''
            stall till the locker is closed and upon closing it will update the
            status of delivery
        '''
        locker_num = int(passcode[2:4])
        self.slaveCntr.wait_till_locker_closes(locker_num)

    def verifyCameraRecordings(self):
        os.system('python3 DPLSystem/Scanner/Scanner.py')
        f = open("finish.txt", 'r')


        data = f.readline()
        print("data = ",data)
        if not data:
            return -1
        trackingNumber = int(data)
        delivery = self.db.get_delivery_by_trackingNumber(trackingNumber)
        if not delivery:
            return -1

        #unlock the appropiate locker#
        locker_num = int(delivery.passcode[2:4])

        if not self.slaveCntr.unlock_lock(locker_num):
            print("something went wrong with the slave controller")
            return -1

        if delivery.status == 0: #registed
            self.db.update_delivery_status(delivery.delivery_id, 1)
            self.db.update_locker_state(locker_num,"unavailable")
        elif delivery.status == 1:
            self.db.update_delivery_status(delivery.delivery_id, 2)
            self.db.update_locker_state(locker_num,"available")

        return delivery.passcode
