import unittest
from pyiso.collectors.geo import GeoCollector

class GeoTest(unittest.TestCase):
	def setUp(self):
		self._geo = GeoCollector()

	def test_download(self):
		self._geo.download_isos()
		pass
		