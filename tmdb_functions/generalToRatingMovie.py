from generalToMovie import generalToMovie 
import json

def generalToRatingMovie(general):
    
    general = json.loads(general)
    general = general["results"][0]
    
    data = {
        "id": general["id"],
        "title": general["original_title"],
        "popularity": general["popularity"],
        "vote_average": general["vote_average"],
        "vote_count": general["vote_count"]
    }
    
    return data