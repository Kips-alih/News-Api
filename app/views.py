from flask import render_template
from app import app
from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The Best News Articles Preview Website'
    return render_template('index.html',title=title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)

@app.route('/sources')
def sources():

    '''
    View root page function that returns the index page and its data
    '''
  
    source=get_source('sources')
    title = " HOME-Welcome to the best News online website"
    return render_template('source.html',title=title,sources=source)