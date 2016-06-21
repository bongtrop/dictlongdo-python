# python-dictlongdo

Dict Longdo API from http://dict.longdo.com/mobile.php?search=[word]

Written by Pongsakorn Sommalai bongtrop@gmail.com.

All code is under DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, see LICENSE for details.

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

dict type example "NECTEC Lexitron Dictionary EN-TH", "Longdo Approved EN-TH" default is "NECTEC Lexitron Dictionary EN-TH"

return type is list
