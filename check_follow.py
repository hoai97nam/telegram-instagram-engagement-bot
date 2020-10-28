from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import requests
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# sign in 
API = InstagramAPI("11ndc", "nguyenhnam")
API.login()
#get user id
usrname='tnt12dck'
API.searchUsername(usrname)
usr_id=API.LastJson['user']['pk']
#get user followings
API.getUserFollowers(usr_id)
fl=API.LastJson['users']
#put result in list
k=1
list_following=set()
list_following_full=[]
for i in fl:
    print('{}. '.format(k) + i['username'])
    list_following.add(i['username'])
    list_following_full.append(str(i))
    k+=1

print(list_following_full[0]+"\n")
print(list_following_full[1]+"\n")
print(list_following_full[-1])
'''
def check_follow_yet(list1):
    for i in list1:
        API.searchUsername(i)
        usr_id=API.LastJson['user']['pk']
        #get user followings
        API.getUserFollowers(usr_id)
        fl=API.LastJson['users']

'''