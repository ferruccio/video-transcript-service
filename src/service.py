#! /usr/bin/python

from flask import Flask, request
import json
import xml
import mimerender
import dicttoxml
import pprint

import youtube

app = Flask(__name__)
mime = mimerender.FlaskMimeRender()

@app.route('/v1/transcripts/youtube/<vid>')
@mime(
    default = 'json',
    json = lambda **args: json.dumps(args),
    xml = lambda **args: dicttoxml.dicttoxml(args),
    html = lambda **args: '<html><body><pre>%s</pre></body></html>' % pprint.pformat(args)
)
def youtube_transcript(vid):
    lang = request.args.get('lang')
    if lang == None:
        lang = 'en'
    print 'lang: ', lang
    return youtube.get_transcript(vid, lang)

if __name__ == "__main__":
    app.run()