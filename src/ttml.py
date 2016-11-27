import xml.sax

class TTMLContentHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.lang = None
        self.body = []
        self.copy = False

    def startElement(self, name, attrs):
        if name == "tt":
            self.lang = attrs["xml:lang"]
        elif name == "p":
            self.text = ""
            self.start = attrs["begin"]
            self.stop = attrs["end"]
            self.copy = True

    def characters(self, content):
        if self.copy:
            self.text += content
    
    def endElement(self, name):
        if name == "p":
            self.copy = False
            self.body.append({ "start": self.start, "stop": self.stop, "text": self.text })

def parse(filename):
    tch = TTMLContentHandler()
    xml.sax.parse(filename, tch)
    return { "lang": tch.lang, "body": tch.body }