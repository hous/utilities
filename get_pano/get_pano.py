#!/usr/bin/python
import sys, re
import urllib2, urllib
from PIL import Image
from cStringIO import StringIO

def main():
	""" Given the URL of a Google Maps Street View URL, this script generates an equirectangular panoramic image by fetching each image tile and stitching them together.

	Example:
		$ python get_pano.py https://www.google.com/maps/place/Dolby+Theatre/@34.1027387,-118.340471,3a,75y,354h,90t/data=!3m8!1e1!3m6!1soInaTCic7TsAAAQDMaZ31A!2e0!3e2!6s%2F%2Fgeo1.ggpht.com%2Fcbk%3Fpanoid%3DoInaTCic7TsAAAQDMaZ31A%26output%3Dthumbnail%26cb_client%3Dsearch.TACTILE.gps%26thumb%3D2%26w%3D86%26h%3D86%26yaw%3D354.01968%26pitch%3D0!7i13312!8i6656!4m2!3m1!1s0x0000000000000000:0xf5f01d0d3b59ab76!6m1!1e1

	TODO:
		- [ ] Use wget module instead of urllib2 for fetching images, to allow for parallel requests
	"""
	tile_dimensions = (512, 512)
	tile_count = (5, 4) 
	image = Image.new("RGB", (tile_dimensions[0] * tile_count[0], tile_dimensions[1] * tile_count[1]), None)

	try:
		url = sys.argv[1]
	except:
		print "Please enter a Google Maps URL as a parameter."
		print "Usage: $ python get_pano.py https://www.google.com/maps/@34.1027387,-118.340471,3a,75y,32.1h,87.53t/data=!3m7!1e1!3m5!1soInaTCic7TsAAAQDMaZ31A!2e0!3e2!7i13312!8i6656"
		return

	try:
		print "************************************"
		print "Fetching images from Google Maps, this could take some time..."
		regex = re.compile(r'panoid\=([^&]*)', re.I)
		pano_id = regex.findall(urllib.unquote(url))[0]
		for y in range(tile_count[1]):
			for x in range(tile_count[0]):
				img_url = "https://geo2.ggpht.com/cbk?cb_client=maps_sv.tactile&authuser=0&hl=en&panoid=" + pano_id + "&output=tile&x="+str(x)+"&y="+str(y)+"&zoom=3&nbt&fover=2"
				response = urllib2.urlopen(img_url)
				file_data = StringIO(response.read())
				image.paste(Image.open(file_data), (x * tile_dimensions[0], y * tile_dimensions[1]))
		
		filename = "pano-" + pano_id + ".jpg"
		image.save(filename)
		print "Success, image saved as \033[96m" + filename + "\033[00m"
		print "************************************"


	except Exception as e:
		print "Sorry something broke."
		print e 

main()
