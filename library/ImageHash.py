#!/usr/bin/env python
# coding:utf-8

import re
import sys
import imagehash
from PIL import Image

#=====================================================#
#ハミング距離
def getHammingDistance(n,m):
	data=n ^ m
	data=(data & 0x5555555555555555)+((data & 0xAAAAAAAAAAAAAAAA)>> 1)
	data=(data & 0x3333333333333333)+((data & 0xCCCCCCCCCCCCCCCC)>> 2)
	data=(data & 0x0F0F0F0F0F0F0F0F)+((data & 0xF0F0F0F0F0F0F0F0)>> 4)
	data=(data & 0x00FF00FF00FF00FF)+((data & 0xFF00FF00FF00FF00)>> 8)
	data=(data & 0x0000FFFF0000FFFF)+((data & 0xFFFF0000FFFF0000)>>16)
	data=(data & 0x00000000FFFFFFFF)+((data & 0xFFFFFFFF00000000)>>32)
	return data
		
#=====================================================#

def print_debug_log(str):
#	if not __debug__:
	print(str)

#=====================================================#
# ImageHashクラス
#=====================================================#

class ImageHash(object):

#=====================================================#

# log 出力関数
	@staticmethod
	def log(depth, tag_name, msg):
		if depth == 0: 
			print( "\n")
		print( "\t" * depth +  "[%s] %s" % (tag_name ,msg))

#=====================================================#

	def __init__(self):
		""" initialize: set urllib2.opener """
		#print_debug_log( "=== Callled : " + sys._getframe().f_code.co_name + " ===" )
		
#=====================================================#

	# 画像hashを算出する
	def calc_dhash_image(self, path):
		hash = imagehash.dhash(Image.open(path))
		hash_Str = str(hash)
		return hash_Str
		
#=====================================================#

if __name__ == "__main__":

	print_debug_log( "=== Callled : " + sys._getframe().f_code.co_name + " ===" )
	
	ImageHash = ImageHash.calc_dhash_image( "C:/Users/tktomaru/Desktop/blog/20140609174519_120.jpg" )
	print(ImageHash)

# End of File #
