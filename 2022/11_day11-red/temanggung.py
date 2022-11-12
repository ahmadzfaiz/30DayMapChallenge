import ee
from ee_plugin import Map

jumo = ee.Geometry.Point([110.10799602668077, -7.2278567238753055]);
Map.centerObject(jumo, 11);

landsat8 = ee.Image('LANDSAT/LC08/C02/T1/LC08_120065_20200627')

trueColor = {
    'bands': ['B5', 'B4', 'B3'],
    'min': 4000,
    'max': 35000
};

Map.addLayer(landsat8, trueColor, 'Citra True Color');