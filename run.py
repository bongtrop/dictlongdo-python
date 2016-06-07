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

class Longdo(Resource):
    isLeaf = True

    def render_GET(self, request):
        request.responseHeaders.addRawHeader(b"content-type", b"application/json")
        if "word" not in request.args:
            request.setResponseCode(402)
            return json.dumps({"error": "Please define args word."})

        return json.dumps(pydictlongdo.translate(request.args["word"][0]))


resource = Longdo()
factory = Site(resource)
reactor.listenTCP(10005, factory)
reactor.run()
