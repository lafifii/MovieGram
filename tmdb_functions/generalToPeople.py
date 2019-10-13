import json

def generalToPeople(general, img_path):

    general = json.loads(general)
    general = general["results"][0]

    known_for = []
    for obj in general["known_for"]:
        if "title" in obj.keys():
            known_for.append(obj["title"])
    
    data = {
        "id": general["id"],
        "name": general["name"],
        "image": img_path + general["profile_path"],
        "popularity": general["popularity"],
        "known_for": known_for
    }
    
    return data