import unittest
from astropy.io import fits

from csst_dfs_commons.utils.fits import get_header_value, get_healpix_id, get_healpix_ids, hdul_of_healpix_ids

class CommonFitsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_hdul_of_healpix_ids(self):
        hdul = fits.open()
        r = hdul_of_healpix_ids(id = 1)


