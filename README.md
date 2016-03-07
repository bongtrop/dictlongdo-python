# python-dictlongdo

Dict Longdo API from http://dict.longdo.com/mobile.php?search=[word]

Written by Pongsakorn Sommalai bongtrop@gmail.com.

All code is under a BSD-style license, see LICENSE for details.

Source: [https://github.com/bongtrop/python-dictlongdo.git](https://github.com/bongtrop/python-dictlongdo.git)

## Requirements

- python 2.7
- python-requests

## Installation

To install run

    ``python setup.py install``

which will install the library into python's site-packages directory.

## Usage
    >>> import pydictlongdo
    >>> pydictlongdo.translate([word], dtype=[dict type])

dict type example "NECTEC Lexitron Dictionary EN-TH", "Longdo Approved EN-TH"

return type is list

## Extra
You can use this on my server

URL: [http://pongsakorn.xyz:10001/?word=cat](http://pongsakorn.xyz:10001/?word=cat)

It return in json format
