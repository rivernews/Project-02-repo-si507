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
    # pull out the entire movie dataset (as pandas dataframe)
    movies_df = tools.get_movies_df()

    # get the number of movies in our dataset
    num = movies_df.shape[0]

    # generate a piece of html to show the number and respond back to the user
    return '''<h1>{} movies recorded.</h1>
        <a href="/movies/ratings/">Ratings</a>
    '''.format(num)

@app.route('/movies/ratings/')
def rating_page():
    # sample 10 movies randomly from the movie dataset, and cherry pick two columns to include - 'Title' and 'IMDB Rating'
    samples = tools.get_movie_samples(10, ['Title', 'IMDB Rating'])

    # convert pandas sample data into Movie instances 
    movies = []
    for index, movie in samples.iterrows():
        movie = tools.Movie(movie)
        movies.append(movie)
    
    # send our Movie instances to the template for rendering
    return render_template('movie_ratings.html', movies=movies)


if __name__ == '__main__':
	app.run(debug=True)