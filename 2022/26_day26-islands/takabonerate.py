import ee
from ee_plugin import Map

takabonerate = ee.Geometry.Point([121.09888248368289, -6.569026435897765])
Map.centerObject(takabonerate, 11);

landsat8 = ee.Image('LANDSAT/LC08/C02/T1/LC08_113065_20200423')

batimetri = {
    'bands': ['B4', 'B3', 'B1'],
    'min': 6000,
    'max': 20000
};

Map.addLayer(landsat8, batimetri, 'Batimetri');