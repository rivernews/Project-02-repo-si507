'''
write some code to make your Flask app easier.
'''

import pandas as pd

class Movie:
    def __init__(self, pandas_row):
        self.title = pandas_row['Title']
        self.imdb_rating = pandas_row['IMDB Rating'] if not pd.isnull(pandas_row['IMDB Rating']) else 'NA'
    
    def __repr__(self):
        return '{} | {}'.format(self.title, self.imdb_rating)

def get_movies_df():
    return pd.read_csv("movies_clean.csv")
