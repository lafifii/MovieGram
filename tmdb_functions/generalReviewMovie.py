import json

def generalReviewMovie(general):
    
    general = json.loads(general)
    general = general["results"]
    data = {'results':[]}

    i = 0
    for g in general:
        content = {
            'author': g['author'],
            'content': g['content'],
        }
        data['results'].append(content)
        i += 1
        if i == 3:
            break
    
    return data