import mongomock
from bson import objectid
from .context import sample
import unittest
import mock
class databaseTestSuite(unittest.TestCase):

    def setUp(self):
        self.client=mongomock.MongoClient()
        self.db= self.client['BaseTesting']
    def tearDown(self):
        self.db.drop_collection('words')
    def test_insertWithContent(self):
        self.dictionary={'key','value'}
        print type(sample.Create(self.dictionary,self.db))
        self.assertEqual(type(sample.Create(self.dictionary,self.db)),objectid.ObjectId)

    def test_insertWithContent(self):
        self.dictionary={'key','value'}
        print type(sample.Create(self.dictionary,self.db))
        self.assertEqual(type(sample.Create(self.dictionary,self.db)),objectid.ObjectId)

    def test_insertWithNoContent(self):
        self.dictionary={}
        print type(sample.Create(self.dictionary,self.db))
        self.assertEqual(sample.Create(self.dictionary,self.db),None)
    