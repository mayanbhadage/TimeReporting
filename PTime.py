from datetime import *
import time as t
class Time:

    def __init__(self):
        self.day = None
        self.date = None
        self.inTime = None
        self.outTime = None

    def get_day(self):
        now = datetime.now()
        self.day = now.strftime("%A")
        print self.day

    def get_date(self):
        self.date = datetime.today().strftime('%m/%d/%Y')
        print self.date

    def get_in_time(self):
        self.inTime = datetime.now().strftime('%H:%M:%S')
        print self.inTime

    def get_out_time(self):
        self.outTime = datetime.now().strftime('%H:%M:%S')
        print self.outTime


time = Time()
time.get_day()
time.get_date()
time.get_in_time()
t.sleep(5)
time.get_out_time()
