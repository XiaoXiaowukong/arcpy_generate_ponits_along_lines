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
print shp_file
if os.path.exists(shp_file):
    print "ok"
else:
    print "file is not exist"
    exit(1)
##################################################################
arcpy.AddField_management(shp_file,"LengthKM","DOUBLE","","","","","NULLABLE","NON_REQUIRED","")

arcpy.CalculateField_management(shp_file, "LengthKM", "!shape.geodesicLength@KILOMETERS!", "PYTHON_9.3")
##################################################################

arcpy.Generalize_edit(in_features=shp_file, tolerance="1 Centimeters")
print "1"
# arcpy.Generalize_edit(in_features=shp_file, tolerance="1 Centimeters")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "1"
retval=arcpy.Densify_edit(in_features=shp_file, densification_method="DISTANCE", distance="100 Meters",
                   max_deviation=".1 Meters",
                   max_angle="10")
print"2"
print retval.status
retval.save("123.shp")
print type(retval.getOutput(0))
print type(retval)
