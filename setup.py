import serial
from Tkinter import *
import tkMessageBox
import Tkinter
import time
from random import randint
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 3}},
    windows = [{'script': "RCP GUI.py"}],
    zipfile = None,
)