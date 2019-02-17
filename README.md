# Project-02-repo-si507

This web app disaplays movies information from a movie csv dataset.

## Getting Started

In order to run this project, follow the steps as below:

1. Clone this project
1. `cd` to project root directory, and create a virtual environment, `python3 -m venv venv`
1. Activate virtual environment, `. ./venv/bin/activate`
1. Install the depenedencies `pip install -r requirements.txt`
1. Run the server `python SI507_project2.py runserver`
1. Open browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## What the app does

1. The [homepage](http://127.0.0.1:5000/) `/` will show the number of movies we have in our dataset.
1. The [ratings page](http://127.0.0.1:5000/movies/ratings/) `/movies/ratings/` shows some movie titles and their IMDB ratings.
    - This view creates some `Movie` instances and use them to show the titles and ratings in the html page.

# Dev Notes

- The image `SI507_movies_database_plan.png` shows our database diagram, which contains 5 tables representing some data from our dataset.
- Flask view: at least one view should create Movie()

# Reference

- [This repo url](https://github.com/rivernews/Project-02-repo-si507)