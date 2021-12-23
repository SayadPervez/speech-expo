import sys
import os

if(len(sys.argv)==2):
    msg=(str(sys.argv[1]).lower()).split(" ")
else:
    print("No CLA")
    exit()

msg=(" ".join(msg)).lower()
print(msg)
if((("motor" in msg or "mota" in msg) and ("forward" in msg or "back" in msg or "stop" in msg or "top" in msg or "reverse" in msg))):
    if("forward" in msg):
        os.system('python controller.py "forwards"')
    elif("back" in msg or "reverse" in msg):
        os.system('python controller.py "backwards"')
    elif("top" in msg or "stop" in msg):
        os.system('python controller.py "stop"')
    print("success from python")
else:
    print("Invalid CLA")
    exit()