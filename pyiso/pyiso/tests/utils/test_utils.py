import unittest
from urllib import unquote

from pyiso.utils.utils import download_iso

class UtilTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_download(self):
		"""
			download from the lake michigan nowcast 3d 2006 best model
		"""
		url = 'http://64.9.200.113:8080/thredds/iso/glos/glcfs/archive2006/michigan/ncfmrc-3d/Lake_Michigan_-_Nowcast_-_3D_-_2006_best.ncd'
		catalog = unquote('http%3A%2F%2F64.9.200.113%3A8080%2Fthredds%2Fcatalog%2Fglos%2Fglcfs%2Farchive2006%2Fmichigan%2Fncfmrc-3d%2Fcatalog.html')
		dataset = unquote('glos%2Fglcfs%2Farchive2006%2Fmichigan%2Fncfmrc-3d%2FLake_Michigan_-_Nowcast_-_3D_-_2006_best.ncd')

		file_name = download_iso(url, catalog=catalog, dataset=dataset)

		assert file_name == 'Lake_Michigan_-_Nowcast_-_3D_-_2006_best.ncd.xml'
