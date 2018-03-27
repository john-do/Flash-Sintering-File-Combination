import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes":["PyQt4","atexit"],"packages": [], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "None"
"""
if sys.platform == "win32":
    print("win32")
    base = "Win32GUI"
else:
    print("None")
"""
setup(  name = "Flash Combination",
        version = "1.0",
        description = "Flash Combination Helper",
        options = {"build_exe": build_exe_options},
        executables = [Executable("flash_process_gui.py", base=base)])