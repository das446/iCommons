import requests

def GetFbImage():
    URL = "https://graph.facebook.com/drexelcci/photos"
    r = requests.get(url = URL)
    data = r.json() 
    print(data)
    return data
