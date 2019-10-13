
def generalToPeople(general):

    known_for = []
    for obj in general["known_for"]:
        known_for.append(obj["original_title"])

    data = {
        "id": general["id"],
        "name": general["name"],
        "image": general["profile_path"],
        "popularity": general["popularity"],
        "known_for": known_for
    }
    
    return data