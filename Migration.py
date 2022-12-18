#!/usr/bin/env python
# coding:utf-8

import os
import glob
from library import ImageHash

os.environ['PYTHONIOENCODING'] = 'UTF-8'

print('Image Search Start!!')

crawlmarket = ImageHash.ImageHash()
RenameFileList = glob.glob("C:/Users/tktomaru/Desktop/blog-new-rename/*")
OldFileList = glob.glob("C:/Users/tktomaru/Desktop/blog/*")
# print( RenameFileList )#
for rfile in RenameFileList:
   rhash = crawlmarket.calc_dhash_image( rfile )
   for ofile in OldFileList:
      ohash = crawlmarket.calc_dhash_image( ofile )
      if( rhash == ohash ) :
         print( rfile + "   " + ofile)
         break
