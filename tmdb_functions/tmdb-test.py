import unittest
from tmdb import getMovie, getSerie, getActor, getDirector, getTrendMovies, getTrendSeries, getTrendDirectors, getRatingMovie, getReviewMovie

class TestStringMethods(unittest.TestCase):
    # CP005, CP006
    def test_getMovie(self):
        movie = getMovie('asu mare')
        self.assertEqual(movie['id'], 564297)
        test = getMovie('/')
        self.assertIsNone(test)
    # CP003, CP004
    def test_getSerie(self):
        serie = getSerie('spiderman')
        self.assertEqual(serie['id'], 888)
        test = getSerie('/')
        self.assertIsNone(test)
    # CP001, CP002
    def test_getActor(self):
        person = getActor('will smith')
        self.assertEqual(person['id'], 2888)
        test = getActor('/')
        self.assertIsNone(test)
    # CP007, CP008
    def test_getDirector(self):
        person = getDirector('christopher nolan')
        self.assertEqual(person['id'], 525)
        test = getDirector('/')
        self.assertIsNone(test)
    # CP0010
    def test_getTrendMovies(self):
        tMovie = getTrendMovies()
        self.assertIsNotNone(tMovie)
    # CP011
    def test_getTrendSeries(self):
        tMovie = getTrendSeries()
        self.assertIsNotNone(tMovie)
    # CP009
    def test_getTrendDirectors(self):
        tMovie = getTrendDirectors()
        self.assertIsNotNone(tMovie)
    # CP015, CP012
    def test_getRatingMovie(self):
        movie = getRatingMovie('avengers')
        self.assertEqual(movie['id'], 299536)
        test = getMovie('/')
        self.assertIsNone(test)
    # CP013, CP014
    def test_getReviewMovie(self):
        reviews = getReviewMovie('avengers')
        self.assertIsNotNone(reviews)
        test = getReviewMovie('/')
        self.assertIsNone(test)

if __name__ == '__main__':
    unittest.main()
