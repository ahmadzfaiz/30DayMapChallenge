import ee
from ee_plugin import Map

jogja = ee.Geometry.Polygon(
    [[
        [110.05, -7.70],
        [110.05, -7.84],
        [110.17, -7.84],
        [110.17, -7.70]
    ]]
);

l8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA").filterBounds(jogja);

def addNDVI(image):
  cloud = ee.Algorithms.Landsat.simpleCloudScore(image).select('cloud');
  mask = cloud.lt(20);
  ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI');
  return image.addBands(ndvi).updateMask(mask);

withNDVI = l8.filterDate('2017-01-01', '2017-12-31').map(addNDVI);
ndvi = withNDVI.median().select('NDVI');
vis = {'min': -0.2, 'max': 0.7, 'palette': ['blue', 'white', 'green']};

Map.centerObject(jogja, 10);
Map.addLayer(ndvi, vis, 'NDVI');