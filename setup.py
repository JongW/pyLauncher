import sys
from cx_Freeze import setup, Executable

# build_exe_options = {"zip_include_packages": "PyQt5", "optimize": 2}

setup(
    name="MiniScript",
    version="1",
    description="MiniScript",
    # options={"build_exe": build_exe_options},
    executables=[Executable("GUI.py", base="Win32GUI")])
