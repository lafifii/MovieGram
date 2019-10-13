
def generalToSerie(general):
    data = {
        "id": general["id"],
        "title": general["name"],
        "overview": general["overview"],
        "image": general["backdrop_path"],
        "popularity": general["popularity"]
    }
    return data