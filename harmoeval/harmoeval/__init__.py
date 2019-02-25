import os
from flask import Flask, render_template, request, url_for, session, redirect, flash
from . import audio_files as af


def create_app():

	app = Flask(__name__)


	# Ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass



	# Starting page
	@app.route('/', methods=('GET', 'POST'))
	def start():
		return render_template('start.html')



	# Evaluation page
	@app.route('/eval', methods=(['POST']))
	def eval():

		version_ranking = []				

		if request.method == 'POST':
			if request.form['state'] == 'start':
				participant_id = request.form['participant_id']
				song_index = 0
				record_file = "harmoeval/rec/" + participant_id + ".csv"
				open(record_file, 'w').close()
				
			elif request.form['state'] == 'eval':
				song_index = int(request.form['song_index'])
				song_id = request.form['song_id']
				version_ranking = request.form['version_ranking']
				participant_id = request.form['participant_id']

				record_file = "harmoeval/rec/" + participant_id + ".csv"
				data = song_id + ','+ version_ranking + '\n'
				with open(record_file, 'a') as f:
					f.write(data)
				song_index += 1

		if song_index == len(af.get_song_ids()):
			return redirect(url_for('end'))			
		else:
			song_ids = af.get_song_ids()
			current_song = song_ids[song_index]
			last_song = af.get_last_song_id()
			eval_len = len(af.get_song_ids())

			file_paths, versions_shuffle = af.get_shuffled_file_paths(current_song)
			melody_file = af.get_melody_file_path(current_song)

			return render_template('eval.html', participant_id=participant_id, eval_len=eval_len, song_id=current_song, song_index=song_index, current_song=current_song, melody_file=melody_file, file_paths=file_paths, versions_shuffle=versions_shuffle)



	# Ending page
	@app.route('/end', methods=('GET', 'POST'))
	def end():
		return render_template('end.html')


	return app
