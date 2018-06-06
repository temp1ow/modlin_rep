import urllib2
import json

#fileformatlocaldb (db.txt)- user:project:last_sha

user_global="alexey-igrychev"
project_global="dapp"
def get_commits(user,user_project):

    all_commits=json.load(urllib2.urlopen("https://api.github.com/repos/"+user+"/"+user_project+"/commits"))
    return all_commits
print get_commits("alexey-igrychev","dapp")

