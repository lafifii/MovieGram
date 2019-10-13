import json

def generalToTrendSeries(general, img_path):

    general = json.loads(general)
    data = {"results":[]}
    
    q = 0
    for obj in general["results"]:

        content = {
            "id": obj["id"],
            "title": obj["name"],
            "vote_average": obj["vote_average"],
            # "popularity": obj["popularity"],
            "image": img_path + obj["poster_path"]
        }

        data["results"].append(content)

        q += 1
        if q == 3:
            break

    return data
