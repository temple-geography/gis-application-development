# Using PyInstaller to Bundle a Python Application

## What is PyInstaller

PyInstaller bundles a Python application and all its dependencies into a single folder or file. In Python parlance, this is referred to as **freezing** the application. PyInstaller reads a Python script, analyzes the code to discover every other necessary module and library, collects copies of all those files (including the active Python interpreter), and bundles it into a single folder or executable file.

## Preparation

These instructions are written primarily for a Windows computer with Anaconda Python installed.

This workshop requires a Python environment with the following packages installed:

* PyInstaller
* PyQT5
* Pillow

All of these packages are included in the `gus8066` environment. Open the Anaconda Prompt and activate the `gus8066` environment (or any environment with the necessary packages).

Create a folder called `temp_converter`, and download the files `converter.py` and `thermometer.png`.

Look at `converter.py`. This is a PyQT script that opens a main window with a simple application. The application logic is contained in the following function:

```python
def convert(self, window):
	self.i1 = self.comboBox.currentText()
	self.i2 = self.comboBox_2.currentText()
	inp = float(self.textEdit.toPlainText())
	if self.i1 == 'Celsius':
		if self.i2 == 'Celsius':
			result = inp
		else:
			result = 9*inp/5+32
	elif self.i1 == 'Fahrenheit':
		if self.i2 == 'Celsius':
			result = ((inp-32)/9)*5
		else:
			result= inp

	self.textEdit_2.setText(str(round(result,8)))
```

Prior to running PyInstaller, you can test this application by running `converter.py` in your IDE, or by running `python converter.py` in the terminal or command prompt.

The course repo includes the file `converter.ui`. This is a UI file created by QT Designer. It is included for completeness, but we have already processed `converter.ui` to create `converter.py`, the Python script that launches the GUI application.

## Running PyInstaller

In the terminal, navigate to `temp_converter`, the folder that contains `converter.py`.

Run the following command:

```sh
pyinstaller -F -w -i thermometer.png converter.py
```

Look in the folder `temp_converter`. There should be two new folders: `build` and `dist`. Inside the folder `dist`, you should have one executable file with a thermometer icon. On Windows, this will be called `converter.exe`.

## Understanding the Command Line Options

We ran PyInstaller using the options `-F`, `-w`, and `-i`.

### `-F` or `--onefile`

`-F` (an alias for `--onefile`) creates a single-file executable. This file includes the Python interpreter (so that the user does not need a Python installation to run your file). For our simple application, the source code is 2 KB, but the frozen application is 51 MB.

Omitting `-F` (or replacing it with `-D`, which is the default) produces a single-folder application. I won't demonstrate it in class, but you can try it on your own. In this case you will get a folder named `converter`, which contains a much smaller executable (1 MB) and a bunch of supporting files.

For applications with many imports of large packages, using the one-folder option may be preferable. However, this also raises the possibility of the user not copying all of the application files. If you use the one-folder option, you may want to create an installer or setup application to aid in installing your application. This is beyond the scope of this workshop.

Note that for MacOS, the one-file method is not advised.

### `-w` or `--windowed`

The `converter.py` application is a GUI (windowed) application. We don't want a console to appear when we run it. We achieve this using the `-w` switch.

If you are instead creating a command line application, i.e. one that is intended to be run in the console, omit `-w` (r replace it with `-c`, which is the default).

### `-i`

`-i` is used to pass the path to an icon file (`*.ico` on Windows, `*.icns` on MacOS). If the file is not already in the icon file format, PyInstaller attempts to use Pillow to convert the image file to an icon. Pillow is available in the `gus8066` conda environment.

If your application does not have a custom icon, omit `-i`.

### Other Options

PyInstaller has many other options. Please refer to [Using PyInstaller](https://pyinstaller.org/en/stable/usage.html).

Of particular use is `--clean`. If you run PyInstaller more than once on the same application, you may need to use `--clean` to make sure that you get a fresh build of your application.

## Supporting Multiple Operating Systems

PyInstaller is not a [cross compiler](https://en.wikipedia.org/wiki/Cross_compiler). From the documentation:

> If you need to distribute your application for more than one OS, for example both Windows and macOS, you must install PyInstaller on each platform and bundle your app separately on each.
> 
> Source: <https://pyinstaller.org/en/stable/usage.html#supporting-multiple-operating-systems>

It is fantastic that Python is a cross-platform programming language, but there is still significant work involved in distrubting a cross-platform application. If you use PyInstaller to distribute your application to multiple OSes, please refer to the documentation.

## REFERENCES

[PyInstaller Manual](https://pyinstaller.org/)
 