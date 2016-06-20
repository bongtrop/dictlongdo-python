# -*- coding: utf-8 -*-

'''
Author: Pongsakorn Sommalai (bongtrop@gmail.com)
Date: 08/03/2016
Description: Server to translate en2thai and return it by json
'''

# Default
import json
import pydictlongdo

# Web Server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

class L(Resource):
    def __init__(self, word):
        Resource.__init__(self)
        self.word = word

    def render_GET(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        return json.dumps(pydictlongdo.translate(self.word))

class Longdo(Resource):
    def getChild(self, name, request):
        if len(name)==0:
            return self

        return L(name)

    def render_GET(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        request.setResponseCode(402)
        return json.dumps({"error": "Please define args word."})



class Novels(Resource):
    def getChild(self, name, request):
        if len(name)==0:
            return self

        return Chapters(name)

    def render_GET(self, request):
        request.setHeader("content-type", "application/json")
        return json.dumps(wuxiaworld.getNovels())


resource = Longdo()
factory = Site(resource)
reactor.listenTCP(10005, factory)
reactor.run()
