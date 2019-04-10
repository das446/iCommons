import requests

def GetFbImage():
    URL = "https://graph.facebook.com/drexelcci/"
    r = requests.get(url = URL)
    data = r.json() 
    return data