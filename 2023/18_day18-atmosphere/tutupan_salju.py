import ee
from ee_plugin import Map

lt_p90 = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/monthly_lt_p90")

color_palette = [
  'db9e4b', 
  'f4c075', 
  '008489', 
  '00585c'
];

visual = {
  'min': -20,
  'max': 60,
  'palette': color_palette
}

Map.addLayer(lt_p90.first(), visual, 'Tutupan Salju Januari 2000')