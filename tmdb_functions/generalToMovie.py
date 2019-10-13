
def generalToMovie(general):
    data = {
        "id": general["id"],
        "title": general["original_title"],
        "overview": general["overview"],
        "image": general["backdrop_path"],
        "rating": general["vote_average"]
    }
    return data