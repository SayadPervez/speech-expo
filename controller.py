from AMD import ardata
import sys

if(len(sys.argv)==2):
    msg=(str(sys.argv[1]).lower()).split(" ")
else:
    print("No CLA")
    exit()

com = 4

if("light" in msg or "lights" in msg or "lite" in msg) and ("on" in msg) and ("turn" in msg):
    rawData = ardata(com,dynamic=True,msg='l-on',lines=1,squeeze=False,numeric=False)
elif("light" in msg or "lights" in msg or "lite" in msg) and ("of" in msg or "off" in msg) and ("turn" in msg):
    rawData = ardata(com,dynamic=True,msg='l-off',lines=1,squeeze=False,numeric=False)
else:
    print("invalid")