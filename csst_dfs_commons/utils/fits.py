from astropy_healpix import HEALPix
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.coordinates import SkyCoord

def get_header_value(key: str, header, default_value = None):
    try:
        v = header[key]
        if type(v) == str:
            return v.strip()
        return v
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