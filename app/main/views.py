from flask import render_template,url_for
from . import main
from ..request import get_source,get_news
from ..models import Source,Article



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    newsource=get_source('sources')

    title = 'Home - Welcome to The Best News Articles Preview Website'
    return render_template('index.html',title=title,sources=newsource)

@main.route('/articles/<source>',methods=['GET']) 
def articles(source):

    '''
    View root page function that returns the index page and its data

    '''
    articles=get_news(source)
    title='Articles - Welcome to The Best News Articles Preview Website' 

    return render_template('articles.html',title=title,articles=articles,source=source)

