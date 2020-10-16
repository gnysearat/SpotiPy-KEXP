import spotipy
import sys
import spotipy.util as util
import pprint
import feedparser
import ssl
import re

username = "ganymedesearat"
scope = "user-read-private" 
testParams1 = "Rick Astley"
testParams2 = "Never Gonna give you up"

clientID = "9dfb657bb07345bc8b4487750f2db86a"
clientSecret = "d38c8da51a984567b2508986f3fdb6b7"

#stdinput = [sys.argv[1], sys.argv[2]]
#Test Data, pull passed args as list to parse through

#Method for searching for artist/track
#Accepts strings for (ArtistName, SongTitle)
def searchTrack(artist, song):
	token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost/')

	sp = spotipy.Spotify(auth=token)
	results = sp.search(q='artist:' + artist + ' track:' + song, type='track')

	try:
		tracks = results['tracks']['items'][0]['id']
		pprint.pprint("spotify:track:" + tracks)

	except:
		print("Song/Artist combo not found. Please check the name and try again.")	

	else:
		print("Done.")
	return

def ImportRss():

	results = []
	

	if hasattr(ssl, '_create_unverified_context'):
		ssl._create_default_https_context = ssl._create_unverified_context
	#Handles ssl error you get otherwise	

	d = feedparser.parse('https://omny.fm/shows/kexp-presents-music-that-matters/playlists/podcast.rss')

	trackList = d["items"][0]["description"].split("<br>")
	i = 0
	for track in trackList:

		#e = re.findall("[0-9](.*)", track)
		results.append(re.dotall("(<p>)[0-9]\. (.*)(</p>)", track))
		#.dotall isn't the actual command, find out how that works.
		#results[i].insert(re.findall("", results[i]))
		print(results[i])
		i+= 1
	
	return

def CreatePlaylist():

	return


#searchTrack(artist=testParams1, song=testParams2)
#searchTrack(artist=stdinput[0], song=stdinput[1])

ImportRss()