import json

def generalToMovie(general, img_path):
    
    general = json.loads(general)
    general = general["results"][0]
    
    data = {
        "id": general["id"],
        "title": general["original_title"],
        "overview": general["overview"],
        "image": img_path + general["backdrop_path"],
        "vote_average": general["vote_average"]
    }
    return data