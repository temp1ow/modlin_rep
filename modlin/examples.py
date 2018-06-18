from os import path
from datetime import datetime, timedelta
user = 'zoul'
user_project = 'Finch'
home_dir=(str("/home/modlin/modlin/"))




week_ago = datetime.now() - timedelta(minutes=15)
filetime = datetime.fromtimestamp(path.getctime('/home/modlin/modlin/zoulFinch.zip'))

if filetime < week:
    print ("больше недели")
else:
    print ('меньше недели')
