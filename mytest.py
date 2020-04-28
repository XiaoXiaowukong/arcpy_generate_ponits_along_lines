#!/usr/bin/env python
# -*- coding:utf-8 -*-
from arcpy_utils import ArcGisUtils
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    river_dir = "/Volumes/pioneer/日本项目/河流/处理结果/base_result1"
    o_dir = r"E:\janpan_data\base_result"
    for root, dirs, files in os.walk(river_dir):
        for name in files:
            file_split = os.path.splitext(name)
            if file_split[-1] == ".shp" and file_split[0].split("_")[-1] == "new":
                line_shp = os.path.join(root, name)
                line_shp = unicode(line_shp, "utf-8")
                arcgis_utils = ArcGisUtils()
                arcgis_utils.set_line_shp(line_shp)
                arcgis_utils.generate_points_along_lines(o_dir)
