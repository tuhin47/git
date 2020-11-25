from datetime import datetime
import os

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
os.system("date")
print('Current Timestamp : ', timestampStr)