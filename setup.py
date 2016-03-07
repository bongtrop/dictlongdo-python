from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-dictlongdo",
      version="0.3.0",
      py_modules=["pydictlongdo"],
      description="Dict Longdo API from http://dict.longdo.com/mobile.php?search=[word] ",
      author="Pongsakorn Sommalai",
      author_email = "bongtrop@gmail.com",
      license="BSD",
      url="https://github.com/bongtrop/python-bitlongdo",
      long_description=long_description,
      platforms=["any"]
      )
