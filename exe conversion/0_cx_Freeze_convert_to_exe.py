# thanks to https://www.youtube.com/watch?v=GSoOwSqTSrs
from cx_Freeze import setup, Executable
import sys, os

fileName = input("What's the name of the py file to be converted to .exe?\n")
sys.argv.append('build')

os.environ['TCL_LIBRARY'] = r'C:\Users\Naelone Maxwell\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Naelone Maxwell\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.
elif (sys.platform == "win64"):
    base = "Win64GUI"    # Tells the build script to hide the console.



setup(
    name='KutsalAklinNerde?',
    version='0.1',              #Further information about its version
    description='Parse stuff',  #It's description
    executables=[Executable(fileName + ".py", base=base)])


'''

import tkinter
build_exe_options = {"includes":["tkinter"],
                     "excludes":[],
}

setup(
    name='KutsalAklinNerde?',
    options={"build_exe": build_exe_options},
    version='0.1',              #Further information about its version
    description='Parse stuff',  #It's description
    executables=[Executable(fileName + ".py", base=base)])

'''
