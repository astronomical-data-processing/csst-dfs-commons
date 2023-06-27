import unittest
from astropy.io import fits

from csst_dfs_commons.utils.fits import get_header_value, get_healpix_id, get_healpix_ids, hdul_of_healpix_ids

class CommonFitsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_hdul_of_healpix_ids(self):
        # hdul = fits.open()
        # r = hdul_of_healpix_ids(id = 1)
        pass

    def test_get_header_value(self):
        # cat_image_file = ""
        # hdul = fits.open(cat_image_file)
        # filter_str = get_header_value("FILTER", hdul, "")
        # print("-"*20)
        # print(filter_str)
        # hdul.close()
        pass


