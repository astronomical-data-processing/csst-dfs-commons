import unittest
from astropy.io import fits

from csst_dfs_commons.models import Request

class CommonModelsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_request_result(self):
        r = Request(id = 1)
        assert r.id == 1, "not equal"
        assert r.xxx == '', "not equal"
