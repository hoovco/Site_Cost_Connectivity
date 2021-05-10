import geopandas
from geopandas import *
print("loaded modules")

#this is a program to take a point values, iterate through the points
#create isocrones, then connect points based on isocrone intersection

#ideally this will be a tool to create networks based on distance

#PSEUDOCODE


#mosiac DEM data if needed (maybe)
# --GDAL merge here --- https://gdal.org/programs/gdal_merge.html --#

#bring in DEM data

#calculate slope
# GDAL dem here --- https://gdal.org/programs/gdaldem.html
#maybe create terrain ruggedness index too? This is interesting.
#https://grass.osgeo.org/grass79/manuals/r.slope.aspect.html 


#calculate backlinks?


#bring in point files
#iterate through point files and create isocrones at user defined intervals
#where points fall into isocrones, create network link (line)
#line may be the least cost path or just an arc - haven't decided yet

#iterate so that a is compared to c, then a is compared to b, and so on ...
#how do I do this loop?

