from business import getBusinessID, getBusinessURL
from sel import containsBusinessView 
import unittest

class TestFunctions(unittest.TestCase):
	
	def test_equal(self):
		self.assertEqual(getBusinessID("Klaas Dillema Bloemsierkunst", "Molenweg 7, 9751 AE Haren, Netherlands"),"ChIJH2OHQA4tyEcRPJ_SAEOseEA")
		self.assertEqual(getBusinessID("Sturehof", "Sturegallerian, Stureplan 2, 114 35 Stockholm, Sweden"),"ChIJjRRMnFydX0YR1B4u6G720yk")
		self.assertEqual(getBusinessURL("ChIJjRRMnFydX0YR1B4u6G720yk"), "https://maps.google.com/?cid=3014023531843165908")
		
	def test_true(self):
		self.assertTrue(containsBusinessView())


if __name__ == '__main__':
	unittest.main(exit=False)
