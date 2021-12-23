from AMD import ardata
import sys

if(len(sys.argv)==2):
    msg=(str(sys.argv[1]).lower()).split(" ")
else:
    print("No CLA")
    exit()

com = 4

print(msg)
rawData = ardata(com,dynamic=True,msg=msg[0],lines=1,squeeze=False,numeric=False)