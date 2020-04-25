#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "1"
import arcpy
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

shp_file = r"E:\janpan_data\order1.shp"
out_fc_1 = r"E:\janpan_data\order1_1.shp"
print shp_file
if os.path.exists(shp_file):
    print "ok"
else:
    print "file is not exist"
    exit(1)
arcpy.GeneratePointsAlongLines_management(shp_file, out_fc_1, 'DISTANCE',
                                          Distance='100 meters',Include_End_Points=False)
arcpy.close()