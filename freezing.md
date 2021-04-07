# Using PyInstaller to Bundle a Python Application

## What is PyInstaller

PyInstaller bundles a Python application and all its dependencies into a single package.  It reads a Python script, analyzes the code to discover every other necessary module and library, collects copies of all those files (including the active Python interpreter), and packages into a single folder, or optionally in a single executable file.

## One Folder Option

This is the default option for bundling the application.  This folder contains all your script’s dependencies and an executable file also named myscript.  It is easy to debug problems that occur when building the app when you use one-folder mode. You can see exactly what files PyInstaller collected into the folder.  A small disadvantage of the one-folder format is that the folder contains a large number of files. Your user must find the myscript executable in a long list of name. Also, your user can create a problem by accidentally dragging files out of the folder.

`pyinstaller script.py`

## One File Option

The one executable file contains an embedded archive of all the Python modules used by your script as well as compressed copies of any non-Python support files.  The advantage is that your users get something they understand, a single executable to launch. A disadvantage is that any related files such as a README must be distributed separately. Also, the single executable is a little slower to start up.

`pyinstaller --onefile or -F script.py`

## Console vs. Windowed

By default, PyInstaller creates a command-line console (a terminal window in Linux and Mac OS, a command window in Windows). It gives this window to the Python interpreter for its standard input and output. Your script’s use of `print()` and `input()` are directed here. 

If the console window is not desired, for example with a Graphical User Interface, the following command would be used.

`pyinstaller -w or --windowed or --noconsole script.py`

## Running PyInstaller in Python
```
import PyInstaller.__main__

PyInstaller.__main__.run([
    'my_script.py',
    '--onefile',
    '--windowed'
])
```

This would be the same as running `pyinstaller --onefile --windowed my_script.py`

See the documentation for more detail on options for bundling as well as debugging tips and changing specs
[PyInstaller Documentation](https://pyinstaller.readthedocs.io/en/stable/index.html)
 