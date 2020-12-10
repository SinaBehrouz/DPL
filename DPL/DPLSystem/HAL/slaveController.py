from serial import Serial
from time import sleep


class slaveController():
    def __init__(self):
        # Number of Locks:
        self.nLock = 4
        # Hex of sending unlocking signal to each lock:
        self.toUnlockHex = ['8a0101119b', '8a01021198', '8a01031199', '8a0104119e']
        # Hex of status read from each lock:
        # Locked succeed:
        self.lockSucceedHex = ['8101010081', '8101020082', '8101030083', '8101040084']
        # Unlock succeed:
        self.unlockSucceedHex = ['8101011190', '8101021193', '8101031192', '8101041195']
        # Unlock failed:
        self.unlockFailedHex = ['810101008a', '8a01020089', '8a01030088', '8a0104008f']
        try:
            self.port = Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600)
        except:
            print ("Cannot establish Serial connection to specified port")
            # exit()


    def __del__(self):
        try:
            if self.port.isOpen():
                self.port.close()
        except:
            print("port is not configured correctly")

    def unlock_lock(self, lockNum):
        '''
            it will take a lockNum and unlock the corresponding locker to that
            lock number in success it will return True else its a False
        '''
        try:
            if not self.port.isOpen():
                self.port.open()
        except:
            print("port is disabled")
            return False

        if lockNum<0 or lockNum > self.nLock:
            print("Invalid input, please try again.")
            self.port.close()
            return False
        else:
            self.port.flushOutput()
            self.port.write(bytes.fromhex(self.toUnlockHex[lockNum-1]))
        self.port.close()
        return True

    def wait_till_locker_closes(self, lock_num):
        try:
            if not self.port.isOpen():
                self.port.open()
        except:
            print("port is disabled")
            return False

        self.port.flushInput()
        is_unlocked = True
        while is_unlocked:
            status = self.port.read(self.port.inWaiting()).hex()
            if self.lockSucceedHex[lock_num-1] in status:
                is_unlocked = False
            sleep(2)
        return True

# uncomment codes below to hardware locks
# lockNum = int(input("Which locker do you want to unlock? "))
# s = slaveController()
# s.unlock_lock(lockNum)
# s.wait_till_locker_closes(lockNum)
