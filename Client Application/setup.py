from distutils.core import setup
import py2exe

setup(name = "VITCloud",
      windows=[{"script":"VITCloud.py" ,
                "icon_resources": [(1, "icon.ico")]
                }
               ],
      author = "Saurabh & Siddharth",
      author_email= "battlex94@gmail.com",
      options={"py2exe":{"includes":["sip"]
                         }
               }
      )

