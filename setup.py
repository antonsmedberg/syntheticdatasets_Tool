from cx_Freeze import setup, Executable
import sys
import os

# Dependencies are automatically detected, but some modules need to be included.
build_exe_options = {
    "packages": ["flask", "waitress", "os"],  # Include required packages
    "excludes": ["tkinter"],
    "include_files": ["public/", "static/"]  # Include your static and template directories
}

# Base determination (needed for GUI applications)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("run.py", base=base)  # Change to run.py as it's your entry point
]

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=executables
)








