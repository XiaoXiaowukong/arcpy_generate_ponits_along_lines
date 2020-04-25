#!/usr/bin/env python
# -*- coding:utf-8 -*-
import arcpy
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ArcGisUtils():
    def init(self):
        pass

    def set_line_shp(self, line_path):
        self.line_shp = line_path
        if os.path.exists(self.line_shp):
            print "ok"
        else:
            print "file is not exist"
            exit(1)

    def generate_points_along_lines(self, o_dir):
        path_split = os.path.splitext(self.line_shp.split("\\")[-1])
        print path_split
        print path_split[0]
        o_file = "{}\{}_point.shp".format(o_dir, path_split[0].decode("utf-8"))
        print o_file
        arcpy.GeneratePointsAlongLines_management(self.line_shp, o_file, 'DISTANCE',
                                                  Distance='100 meters', Include_End_Points=False)
