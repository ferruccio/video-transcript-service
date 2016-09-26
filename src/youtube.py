from __future__ import unicode_literals
import xmltodict

import sys
sys.path.append('./youtube_dl')
import youtube_dl

class Logger(object):
    def debug(self, msg):
        print('debug:', msg)

    def warning(self, msg):
        print('warn:', msg)

    def error(self, msg):
        print('error:', msg)

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

def get_transcript(video_id, lang):
	lang = 'en'
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
		'outtmpl': '/tmp/vid-' + video_id
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['https://www.youtube.com/watch?v=' + video_id])
	    with open('/tmp/vid-' + video_id + '.' + lang + '.ttml') as transcript:
	    	return clean(xmltodict.parse(transcript.read()))
