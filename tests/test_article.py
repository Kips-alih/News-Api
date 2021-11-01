import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Kip','Python Must Be Crazy','A thrilling new Python Series','https://readwrite.com/2021/10/18/how-to-avoid-keyword-cannibalization/','https://images.readwrite.com/wp-content/uploads/2021/10/keyword-cannibalization.jpg','2021-10-29T15:31:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))