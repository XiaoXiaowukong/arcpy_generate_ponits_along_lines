#!/usr/bin/env python
# -*- coding:utf-8 -*-
from arcpy_utils import ArcGisUtils
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    line_shp = r"E:\janpan_data\result\81001001_name.shp"
    line_shp = r"E:\janpan_data\base_result\88080701_中山谷川.shp"
    line_shp = r"E:\janpan_data\base_result\88080700_大坂谷川.shp"
    line_shp=unicode(line_shp,"utf-8")
    o_dir = r"E:\janpan_data\base_result"
    arcgis_utils = ArcGisUtils()
    arcgis_utils.set_line_shp(line_shp)
    arcgis_utils.generate_points_along_lines(o_dir)
