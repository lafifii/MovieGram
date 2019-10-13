import http.client
import json

from generalToMovie import generalToMovie
from generalToPeople import generalToPeople
from generalToSerie import generalToSerie

conn = http.client.HTTPSConnection("api.themoviedb.org")
img_path = "https://image.tmdb.org/t/p/w500/"
language = "es-PE" # "en-US"
api_key = "a52e5d45825556b239d085e464958814"
payload = "{}"

def getPeople(name):

    conn.request("GET",
        "/3/search/person?api_key="+ api_key +
        "&language=" + language + "&query=" + name +
        "&page=1&include_adult=true", payload)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    data = data["results"][0]
    data = generalToPeople(data)

    return data
# - /actor/{name} # - /director/{name}
getDirector = getActor = getPeople
# print(json.dumps(getActor("robert downey"), indent=4, sort_keys=True))
# print(json.dumps(getDirector("christopher nolan"), indent=4, sort_keys=True))

# - /serie/{name}
def getSerie(name):

    conn.request("GET",
        "/3/search/tv?api_key="+ api_key +
        "&language=" + language + "&query=" + name + "&page=1", payload)
    
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    data = data["results"][0]
    data = generalToSerie(data)

    return data
# print(json.dumps(getSerie("bob esponja"), indent=4, sort_keys=True))

# - /movie/{name}
def getMovie(name):

    conn.request("GET",
        "/3/search/movie?api_key="+ api_key +
        "&language=" + language + "&query=" + name, payload)
    
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    data = data["results"][0]
    data = generalToMovie(data)

    return data
# print(json.dumps(getMovie("asu mare"), indent=4, sort_keys=True))


# - /trends/directors
# - /trends/movies
# - /trends/series

# - /rating/movie/{name}
# - /rating/serie/{name}
# - /rating/short/{name}

# - /reception/movie/{name}
# - /reception/serie/{name}
# - /reception/short/{name}