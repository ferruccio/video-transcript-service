from __future__ import unicode_literals
import xmltodict
import os

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

def clean(src):
	tt = src['tt']
	return {
		'lang': tt['@xml:lang'],
		'body': map(lambda p: {
					'start': p['@begin'],
					'stop': p['@end'],
					'text': p['#text']
					}, tt['body']['div']['p'])
	}

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
		    if not os.path.isfile(filename): return None
		    with open(filename) as transcript:
		    	return clean(xmltodict.parse(transcript.read()))
