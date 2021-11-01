class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,author,title,description,url,poster,publishedAt):
        self.author =author
        self.title = title
        self.description = description
        self.link=url
        self.poster = poster
        self.publishedAt= publishedAt