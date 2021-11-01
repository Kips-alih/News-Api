import unittest
from app.models import Source,Article
# Source=models.Source
# Article=models.Article



class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(123,'Python Must Be Crazy','A thrilling new Python Series','https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
