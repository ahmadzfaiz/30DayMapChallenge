import ee
from ee_plugin import Map

komodo = ee.Geometry.Point([119.57121564922411, -8.654575171804208]);
Map.centerObject(komodo, 11);

koleksiCitra = (ee.ImageCollection('LANDSAT/LC08/C02/T1')
    .filterDate('2020-01-01', '2020-12-31')
    .filterBounds(komodo)
    .sort('CLOUD_COVER'))

landsat8 = koleksiCitra.first();

trueColor = {
    'bands': ['B4', 'B3', 'B2'],
    'min': 7000,
    'max': 10000
};
  
Map.addLayer(landsat8, trueColor, 'Citra True Color');