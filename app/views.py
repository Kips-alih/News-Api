from flask import render_template
from app import app
from .request import get_source,get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source=get_source('sources')

    title = 'Home - Welcome to The Best News Articles Preview Website'
    return render_template('index.html',title=title,sources=source)

@app.route('/articles/<source>',methods=['GET']) 
def articles(source):

    '''
    View root page function that returns the index page and its data

    '''
    articles=get_news(source)
    title='Articles - Welcome to The Best News Articles Preview Website' 

    return render_template('articles.html',title=title,articles=articles,source=source)

