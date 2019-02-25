import random
import os

def get_root_dir():
	return "audio/"


def get_song_ids():
	melody_dir = "harmoeval/static/audio/melody/mp3/"
	songs = []
	for song_file in os.listdir(melody_dir):
		songs.append(song_file[:-11])
	return sorted(songs)


def get_last_song_id():
	return get_song_ids()[-1]


def get_melody_file_path(song_id):
	return "../static/audio/melody/mp3/"+song_id+"_melody.mp3"

def get_shuffled_file_paths(song_id):
	versions = ['harmony', 'label', 'rootsuffix', 'rootintervals', 'pitch', 'embeddings']
	random.shuffle(versions)
	paths = ["../static/audio/"+ver+"/mp3/"+song_id+"_"+ver+".mp3" for ver in versions]
	return paths, versions

	