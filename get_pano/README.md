Given a Google Maps Street View URL, this script generates an equirectangular panoramic image by fetching each image tile and stitching them together.

To install:
	pip install -r requirements.txt

Usage:
	python get_pano.py https://www.google.com/maps/@34.1027387,-118.340471,3a,75y,277.38h,70.4t/data\=\!3m8\!1e1\!3m6\!1soInaTCic7TsAAAQDMaZ31A\!2e0\!3e2\!6s%2F%2Fgeo1.ggpht.com%2Fcbk%3Fpanoid%3DoInaTCic7TsAAAQDMaZ31A%26output%3Dthumbnail%26cb_client%3Dmaps_sv.tactile.gps%26thumb%3D2%26w%3D203%26h%3D100%26yaw%3D354.01968%26pitch%3D0\!7i13312\!8i6656
