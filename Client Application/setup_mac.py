from distutils.core import setup
import py2exe

setup(
    name = "VITCloud",
    app = "VITCloud.pyw"
    author = "Saurabh & Siddharth",
    author_email= "battlex94@gmail.com",
    setup_requires=['py2app'],
    OPTIONS = {'argv_emulation': True, 'includes': ['sip', 'PyQt4._qt']}
               }
      )

