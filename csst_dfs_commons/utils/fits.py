from astropy_healpix import HEALPix
from astropy.coordinates import ICRS
from astropy import units as u
from astropy.coordinates import SkyCoord, spherical_to_cartesian
from astropy.io import fits
from astropy import wcs
import numpy as np
import healpy as hp

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

def get_healpix_id(ra, dec, nside=256):
    try:
        hp = HEALPix(nside=nside, order='nested', frame=ICRS())
        coord = SkyCoord(ra = ra * u.deg, dec = dec * u.deg, frame='icrs')
        return hp.skycoord_to_healpix(coord)
    except:
        return -1

def get_healpix_ids(ra, dec, radius, nside=256):
    hp = HEALPix(nside=nside, order='nested', frame=ICRS())
    coord = SkyCoord(ra = ra * u.deg, dec = dec * u.deg, frame='icrs')
    return hp.cone_search_skycoord(coord, radius = radius * u.deg)

def get_raw_header(filepath, **keys):
    union = {}
    with fits.open(filepath, **keys) as hdulist:
        for hdu in hdulist:
            for card in hdu.header.cards:
                card.verify('fix')
                key, value = card.keyword, card.value
                if not key:
                    continue
                union[key]= value
    return union

def fits_of_healpix_ids(filepath, nside=256):
    """ Get healpix ids for the fits file

    :param filepath: the file path of fits
    :param nside: default 128, approximate resolution at NSIDE 1024 is 0.057 deg, 12582912 bricks
    :return: a numpy.ndarray (n,)
    """    
    with fits.open(filepath) as hdulist:
        return hdul_of_healpix_ids(hdulist, nside)
    
def hdul_of_healpix_ids(hdulist, nside=256):
    nx = get_header_value('NAXIS1', hdulist, 0)
    ny = get_header_value('NAXIS2', hdulist, 0)

    fits_wcs = wcs.WCS(hdulist[1])
    ra0, dec0 = fits_wcs.all_pix2world(0, 0, 1)
    ra0, dec1 = fits_wcs.all_pix2world(0, ny, 1)
    ra1, dec0 = fits_wcs.all_pix2world(nx, 0, 1)
    ra1, dec1 = fits_wcs.all_pix2world(nx, ny, 1)
    ra_poly, dec_poly = np.array([[ra0, ra0, ra1, ra1], [dec0, dec1, dec0, dec1]])
    xyzpoly = spherical_to_cartesian(np.deg2rad(ra_poly), np.deg2rad(dec_poly), 1)
    xyzpoly = tuple(map(tuple, xyzpoly))
    xyzpoly = np.array(xyzpoly).reshape(-1, 3)
    healpixids = hp.query_polygon(nside, xyzpoly.T)

    return healpixids
