import mongomock
from bson import objectid
import sample
import unittest

class databaseTestSuite(unittest.TestCase):

    def setUp(self):
        self.client=mongomock.MongoClient()
        self.db= self.client['BaseTesting']
    def tearDown(self):
        self.db.drop_collection('words')
    def test_insertWithContent(self):
        self.dictionary=[('key',0)]
        self.assertEqual(type(sample.CreateFecha(self.dictionary,'2017-01-01',self.db)),str)

   # def test_insertWithNoContent(self):
    #    self.dictionary={}
     #   print type(sample.Create(self.dictionary,self.db))
      #  self.assertEqual(sample.Create(self.dictionary,self.db),None)
    def test_Update(self):
        self.dictionary=[('key',0)]
        self.ID=sample.CreateFecha(self.dictionary,'2017-01-01',self.db)
        self.assertEqual(sample.Update(self.ID,self.db,'palabras.key','RexUnPoliciaDiferente'),'RexUnPoliciaDiferente')
    #def test_checkIdUpdate(self):
	#self.dictionary={'key':'value'}
        #self.ID='pepe'
        #self.assertEqual(sample.Update(self.ID,self.db,'palabras.key','cambios'),'notValidID')
    def test_UpdateNoKey(self):
        self.dictionary = [('key', 0)]
        self.ID = sample.CreateFecha(self.dictionary,'2017-12-20', self.db)
        self.assertEqual(sample.Update(self.ID, self.db, '', 'RexUnPoliciaDiferente'),None)
    def test_UpdateNoValue(self):
        self.dictionary = [('key', 0)]
        self.ID = sample.CreateFecha(self.dictionary,'1994-01-17', self.db)
        self.assertEqual(sample.Update(self.ID, self.db, 'palabras.key', ''),None)
    '''
    def test_Read(self):
        self.dictionary = {'key': 'value'}
        self.ID = sample.Create(self.dictionary, self.db)
        self.assertEqual(sample.Read(self.ID, self.db)['palabras']['key'], 'value')
    
    def test_ReadMultiple(self):
        self.dictionary = {'key': 'value', 'hola':'adios'}
        self.ID = sample.Create(self.dictionary, self.db)
        self.assertEqual(sample.Read(self.ID, self.db)['palabras']['key'], 'value')
        self.assertEqual(sample.Read(self.ID, self.db)['palabras']['hola'], 'adios')
    '''
    #def test_ReadNoContent(self):
     #   self.dictionary = {}
       # self.ID = sample.Create(self.dictionary, self.db)
      #  self.assertEqual(sample.Read(self.ID, self.db), None)


    def test_DeleteValue(self):
        self.dictionary = [('key', 0)]
        self.ID =sample.CreateFecha(self.dictionary, '2015-03-24', self.db)
        self.assertEqual(sample.Delete(self.ID,self.db),None)
    def test_DeleteNoValues(self):
        self.dictionary = {}
        self.ID = sample.CreateFecha(self.dictionary, '2029-02-12', self.db)
        self.assertEqual(sample.Delete(self.ID, self.db), None)
if __name__ == '__main__':
    unittest.main()
