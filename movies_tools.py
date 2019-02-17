import pandas as pd

'''
    Movie class will parse the data from pandas row and store them as properties.
    It handles standardizing data format as well as abstract the low-level string operation,
    so that the flask app can focus on web dev instead of processing data format.
'''
class Movie:
    def __init__(self, pandas_row):
        self.title = pandas_row['Title']
        self.imdb_rating = pandas_row['IMDB Rating'] if not pd.isnull(pandas_row['IMDB Rating']) else 'NA'
    
    def __repr__(self):
        return '{} | {}'.format(self.title, self.imdb_rating)

def get_movies_df():
    return pd.read_csv("movies_clean.csv")

def get_movie_samples(amount, column_list):
    movies_df = get_movies_df()
    return movies_df[column_list].sample(amount)

    