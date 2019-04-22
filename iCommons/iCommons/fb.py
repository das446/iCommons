import requests
import json

def GetFbImage():

    access_token = "EAAIiV84yj4EBAG97LEft6l7wn91Y9CNeduBfekjiEAL2RE398urEoL4uuZAIg7yHYYrk3WDgPpc2cedml9F2ssLfuzkCwygYkHXbP7dA2CGIHZAQjrfpmKnS0xcNCfFJpLND0EFQexA33h4R37ZA3KfFRNnmxoZD"

    album_id="142767529186546"
    URL = "https://graph.facebook.com/drexelcci?fields=albums{photos{images}}&access_token="+access_token
    r = requests.get(url = URL)
    data = r.json() 
    image = data['albums']['data'][0]['photos']['data'][0]['images'][0]
    img = {
        "url": image['source'],
        "width" : image['width'],
        "height" : image['height']
    }
    print(img)
    return img