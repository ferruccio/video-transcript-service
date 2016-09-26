#! /usr/bin/python

from flask import Flask
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
    return youtube.get_transcript(vid, 'en')

if __name__ == "__main__":
    app.run()