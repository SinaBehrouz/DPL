from pyzbar import pyzbar
import time
import cv2
import operator
import threading
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

class Scanner():
    def __init__(self):
        pass
    def getScannedResult(self, found):
        self.vs = cv2.VideoCapture(0)
        stop_time = time.time() + 10
        while time.time() < stop_time:
            rect, frame = self.vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = pyzbar.decode(gray)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                if barcodeData not in found:
                    found[barcodeData] = 1
                if barcodeData in found:
                    found[barcodeData] += 1
            cv2.imshow("Barcode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF

    def finalResult(self):
        found = dict()
        self.getScannedResult(found)
        if len(found) <= 0:
            fh = open('finish.txt', 'r+')
            fh.truncate(0)
            fh.close()
            print("in scanner.py no tracking nuymber fiound")
            return

        trackingNumber = max(found.items(), key=operator.itemgetter(1))[0]
        print("trackingNumber = ", trackingNumber)
        try:
            fh = open('finish.txt', 'w')
            fh.truncate(0)
            fh.write(trackingNumber)
            fh.close()
        except:
            print( "something went wrong in writing the file within scnaner.pty")

        self.vs.release()
        cv2.destroyAllWindows()
        return True
s = Scanner()
s.finalResult()
