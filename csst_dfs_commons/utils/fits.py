from astropy_healpix import HEALPix
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits

def get_header_value(key: str, headers, default_value = None):
    try:
        ret_value = None
        if not isinstance(headers, list):
            headers = [headers]
        for header in headers:
            if key in header:
                ret_value = header[key]
                if type(ret_value) == str:
                    return ret_value.strip()
                return ret_value
        if ret_value is None:
            return default_value
    except Exception as e:
        return default_value

def get_healpix_id(ra, dec, nside=32):
    hp = HEALPix(nside=nside, order='nested', frame=ICRS())
    coord = SkyCoord(ra = ra * u.deg, dec = dec * u.deg, frame='icrs')
    return hp.skycoord_to_healpix(coord)

def get_healpix_ids(ra, dec, radius, nside=32):
    hp = HEALPix(nside=nside, order='nested', frame=ICRS())
    coord = SkyCoord(ra = ra * u.deg, dec = dec * u.deg, frame='icrs')
    return hp.cone_search_skycoord(coord, radius = radius * u.deg)    