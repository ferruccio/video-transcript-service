from __future__ import unicode_literals
import os
import ttml

import sys
sys.path.append('./youtube_dl')
import youtube_dl

class Logger(object):
	def debug(self, msg):
		print 'debug:', msg

	def warning(self, msg):
		print 'warn:', msg

	def error(self, msg):
		print 'error:', msg

def delete_quietly(filename):
	try:
		os.remove(filename)
	except OSError:
		pass

def get_transcript(video_id, lang):
	base = '/tmp/vid-' + video_id
	ydl_opts = {
		'verbose' : True,
	    'logger': Logger(),

		'writesubtitles': True,
		'writeautomaticsub': True,
		'subtitlesformat': 'ttml',
		'subtitleslangs': [lang],
		'skip_download': True,
		'cachedir': False,
		'nocheckcertificate': True,
		'no_color': True,
		'outtmpl': base
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		filename = base + '.' + lang + '.ttml'
		delete_quietly(filename)
		try:
			ydl.download(['https://www.youtube.com/watch?v=' + video_id])
		except:
			return None
		else:
			return ttml.parse(filename) if os.path.isfile(filename) else None
