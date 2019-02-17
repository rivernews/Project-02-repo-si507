from flask import Flask, render_template
import pandas as pd

import movies_tools as tools

'''
Create an SI507_project2.py file in the directory for the Flask app you'll write, and add import statements and comments to it to indicate structure/your plans/your goals for it.
'''

# Set up application
app = Flask(__name__)

@app.route('/')
def index():
    num = 0
    movies_df = tools.get_movies_df()
    num = movies_df.shape[0]
    return '''<h1>{} movies recorded.</h1>
        <a href="/movies/ratings/">Ratings</a>
    '''.format(num)

@app.route('/movies/ratings/')
def rating_page():
    movies_df = tools.get_movies_df()
    samples = movies_df[['Title', 'IMDB Rating']].sample(10)

    movies = []
    for index, movie in samples.iterrows():
        movie = tools.Movie(movie)
        movies.append(movie)
    return render_template('movie_ratings.html', movies=movies)


if __name__ == '__main__':
	app.run(debug=True)