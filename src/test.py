#! /usr/bin/python

from __future__ import unicode_literals

import sys
sys.path.append('./youtube_dl')
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        print('debug:', msg)

    def warning(self, msg):
        print('warn:', msg)

    def error(self, msg):
        print('error:', msg)


ydl_opts = {
	'verbose' : True,
    'logger': MyLogger(),

	'writesubtitles': True,
	'writeautomaticsub': True,
	'subtitlesformat': 'ttml',
	'subtitleslangs': ['en'],
	'skip_download': True,
	'cachedir': False,
	'nocheckcertificate': True,
	'no_color': True,
	'outtmpl': '/tmp/vid'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=7FfKaIgArJ8'])