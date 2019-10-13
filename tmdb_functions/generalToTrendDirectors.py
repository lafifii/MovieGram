import json

def generalToTrendDirectors(general):
    
    general = json.loads(general)
    data = {"results":[]}

    for obj in general["crew"]:
        if obj["job"] == "Director":
            data["results"].append( obj["name"] )
    
    return data