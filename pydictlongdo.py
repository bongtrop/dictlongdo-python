# -*- coding: utf-8 -*-

'''
Author: Pongsakorn Sommalai (bongtrop@gmail.com)
Date: 08/03/2016
Description: Api for connect to Longdo Dict Mobile http://dict.longdo.com/mobile.php?search=[word]
'''

import requests
import re

def removeTagHtml(text):
    return re.sub('<[^<]+?>', '', text)

def translate(word, dtype="NECTEC Lexitron Dictionary EN-TH"):
    r = requests.get("http://dict.longdo.com/mobile.php?search="+word)
    content = r.content

    m = re.search(r"[<]b[>]"+dtype+r"[<][/]b[>][<]table border[=]1 width[=]100[%][>](.+?)[<][/]table[>]", content)
    res = []
    if m:
        words = re.findall(r"[<]tr[>](.+?)[<][/]tr[>]", m.group(1))

        for word in words:
            m = re.search(r"[<]td width[=]40[%][>](.+?)[<][/]td[>][<]td[>](.+?)[<][/]td[>]", word)
            if m:
                w = removeTagHtml(m.group(1))
                m = removeTagHtml(m.group(2)).split(", ")[0]
                res.append({"word": w, "meaning": m})


    return res
