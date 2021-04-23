"""
GDAL
==========================================

Package belonging to Karttur´s GeoImagine Framework.

Author
------
Thomas Gumbricht (thomas.gumbricht@karttur.com)

"""

from .version import __version__, VERSION, metadataD
from .ktgdal import ProcessGDAL, MakeMosaic, GDALinternal, GDALexternal