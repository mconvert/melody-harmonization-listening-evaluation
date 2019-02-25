mp3_dir="mp3/"
wav_dir="wav/"

for dirpath in */; do
	echo "$dirpath"
	echo "---"
	for filepath in "$dirpath$wav_dir"*.wav; do
		filename="`basename $filepath`"
		filename=${filename%????}

		wav_file_path="$dirpath$wav_dir$filename".wav
		mp3_file_path="$dirpath$mp3_dir$filename".mp3
		
		ffmpeg -i $wav_file_path $mp3_file_path
	done
done
