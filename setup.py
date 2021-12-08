from cx_Freeze import setup, Executable
#py setup.py build
#py setup.py py setup.py bdist_msi
setup(name = "mathstuff" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("mathstuff.py")])