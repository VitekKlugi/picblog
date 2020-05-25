import os
import config
import datetime

def log(msg):
    now = datetime.datetime.now()
    with open(os.path.join(config.get()['logdir'], "mailwf"+now.strftime("%Y%m%d")+'.log'), encoding="utf-8", mode="a") as f:
        f.write("%s: %s" % (now.strftime("%d.%m.%Y %H:%M"), msg))