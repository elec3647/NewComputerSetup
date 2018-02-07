import sys
import os
platform = sys.platform

if platform == 'darwin':
    install_mac()
elif platform == 'linux':
    install_linux()
else:
    print "I don't know how to install."

def create dirs(platform):
    os.mkdir(platform)



def install_python_packages():
    pass

def install_mac():
    pass

def install_linux():
