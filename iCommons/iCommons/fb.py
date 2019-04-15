import requests

def GetFbImage():

    access_token = "EAAIiV84yj4EBANSIquE2k3HNwMv5lDrWEDwfo9ZCqHkLPZBCdlN4CRN9UZAQFDStRPlH4rOz1aIdHzjmBtrL35gniZBu2WaKGZA5mmbblgQ4nUrYj8RjQax5MTXadmjKXB8p8bPkjzOPzuCd6FPRkZBLQEZByha2dgy8VVTThCdZA84lyqNZBRp7L4wtXoKVHD0AZD"

    URL = "https://graph.facebook.com/drexelcci/albums?access_token={}".format(access_token)
    r = requests.get(url = URL)
    data = r.json() 
    album_id = data['data'][0]['id']
    print(album_id)
    URL="https://graph.facebook.com/" + album_id + "/photos?fields=picture&access_token=EAAIiV84yj4EBANSIquE2k3HNwMv5lDrWEDwfo9ZCqHkLPZBCdlN4CRN9UZAQFDStRPlH4rOz1aIdHzjmBtrL35gniZBu2WaKGZA5mmbblgQ4nUrYj8RjQax5MTXadmjKXB8p8bPkjzOPzuCd6FPRkZBLQEZByha2dgy8VVTThCdZA84lyqNZBRp7L4wtXoKVHD0AZD"
    r = requests.get(url = URL)
    data = r.json() 

    print(data)
    return data

#GetFbImage()