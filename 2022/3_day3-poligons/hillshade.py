import ee
from ee_plugin import Map

srtm = ee.Image('CGIAR/SRTM90_V4');
hillshade = ee.Terrain.hillshade(srtm);
Map.addLayer(hillshade, {'min':100, 'max':180,}, 'Hillshade');