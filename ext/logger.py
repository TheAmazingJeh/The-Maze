import datetime
import os

class Logger():
    def __init__(self,fOBJ):
        self.logfilepath = os.path.dirname(fOBJ)
        self.enabled = False
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
    def LOGGER_INIT(self):
        if self.enabled:
            t = datetime.datetime.now().strftime("%H:%M:%S ~ %d/%m/%y ")
            log_id,log_type,type,name = "Log ID","Log Type","Data Type","Name"
            print(f"  LOG - {t:<19} │ {log_id:<10} │ {log_type:<15}│ {type:<10} │ {name:<20} │\n")


    def log_init(self,log_id,log_type,type,name):
        if self.enabled:
            t = datetime.datetime.now().strftime("%H:%M:%S ~ %d/%m/%y ")
            logger_type = "Info"
            log_type = log_type[:15]
            print(f"  LOG - {t:<19} │ {log_id:<10} │ {log_type:<15}│ {type:<10} │ {name:<20} │")

    def debug_print(self,):
        if self.enabled:
            print("""
            
            
            """)