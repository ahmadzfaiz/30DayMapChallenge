import ee
from ee_plugin import Map

kupang = ee.Geometry.Point([123.60354356441727, -10.16200739363896]);
Map.centerObject(kupang, 11);

landsat8 = ee.Image('LANDSAT/LC08/C02/T1/LC08_111067_20200511')

trueColor = {
    'bands': ['B4', 'B3', 'B2'],
    'min': 7000,
    'max': 10000
};

Map.addLayer(landsat8, trueColor, 'Citra True Color');