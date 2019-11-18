import http.client
import json

from generalToMovie import generalToMovie
from generalToPeople import generalToPeople
from generalToSerie import generalToSerie

from generalToTrendMovies import generalToTrendMovies
from generalToTrendSeries import generalToTrendSeries
from generalToTrendDirectors import generalToTrendDirectors

from generalToRatingMovie import generalToRatingMovie

from generalReviewMovie import generalReviewMovie

conn = http.client.HTTPSConnection("api.themoviedb.org")
img_path = "https://image.tmdb.org/t/p/w500"
language = "es-PE"  # "en-US"
api_key = "a52e5d45825556b239d085e464958814"
payload = "{}"


def printJson(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def GET(path):

    conn.request("GET", path, payload)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")

    return data

# - /actor/{name} & /director/{name}


def getPeople(name):

    path = "/3/search/person?api_key=" + api_key
    path += "&language=" + language + "&query=" + name
    path += "&page=1&include_adult=true"

    try:
        data = GET(path)
        data = generalToPeople(data, img_path)
    except:
        return None

    return data


getDirector = getActor = getPeople
# print(json.dumps(getActor("robert downey"), indent=4, sort_keys=True))
# print(json.dumps(getDirector("christopher nolan"), indent=4, sort_keys=True))

# - /serie/{name}


def getSerie(name):

    path = "/3/search/tv?api_key=" + api_key
    path += "&language=" + language + "&query=" + name + "&page=1"

    try:
        data = GET(path)
        data = generalToSerie(data, img_path)
    except:
        return None

    return data
# print(json.dumps(getSerie("bob esponja"), indent=4, sort_keys=True))

# - /movie/{name}


def getMovie(name):
    path = "/3/search/movie?api_key=" + api_key
    path += "&language=" + language + "&query=" + name

    try:
        data = GET(path)
        data = generalToMovie(data, img_path)
    except:
        return None

    return data
# print(json.dumps(getMovie("asu mare"), indent=4, sort_keys=True))

# - /trends/movies


def getTrendMovies():
    path = "/3/trending/movie/week?api_key=" + api_key

    try:
        data = GET(path)
        data = generalToTrendMovies(data, img_path)
    except:
        return None

    return data
# print(json.dumps(getTrendMovies(), indent=4, sort_keys=True))

# - /trends/directors


def getTrendDirectors():

    tMovies = getTrendMovies()
    data = {"results": []}

    for movie in tMovies["results"]:

        path = "/3/movie/" + str(movie["id"])
        path += "/credits?api_key=" + api_key

        content = GET(path)
        content = generalToTrendDirectors(content)

        directors = [getPeople(name) for name in content["results"]]

        data["results"].append(directors)

    return data


# print(json.dumps(getTrendDirectors(), indent=4, sort_keys=True))

# - /trends/series


def getTrendSeries():

    path = "/3/trending/tv/week?api_key=" + api_key
    try:
        data = GET(path)
        data = generalToTrendSeries(data, img_path)
    except:
        return None

    return data
# print(json.dumps(getTrendSeries(), indent=4, sort_keys=True))

# - /rating/movie/{name}


def getRatingMovie(name):
    path = "/3/search/movie?api_key=" + api_key
    path += "&language=" + language + "&query=" + name

    try:
        data = GET(path)
        data = generalToRatingMovie(data)
    except:
        return None

    return data
# print(json.dumps(getRatingMovie('asu mare'), indent=4, sort_keys=True))

# - /rating/serie/{name}
# - /rating/short/{name}

# - /reception/movie/{name}


def getReviewMovie(name):

    try:
        movieId = str(getMovie(name)['id'])
    except:
        return None

    path = '/3/movie/' + movieId + '/reviews?api_key=' + \
        api_key + '&language=en-US&page=1'

    try:
        data = GET(path)
        data = generalReviewMovie(data)
    except:
        return None

    return data
# print(json.dumps(getReviewMovie('avengers'), indent=4, sort_keys=True))

# - /reception/serie/{name}
# - /reception/short/{name}
