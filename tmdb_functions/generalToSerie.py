import json

def generalToSerie(general, img_path):
    
    general = json.loads(general)
    general = general["results"][0]
    
    data = {
        "id": general["id"],
        "title": general["name"],
        "overview": general["overview"],
        "image": img_path + general["poster_path"],
        "popularity": general["popularity"]
    }
    return data