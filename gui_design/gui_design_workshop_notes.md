---
title: Getting Started with PyQt5 & QtDesigner
author: Michael Ward
---

#### A Disclaimer:

You do not have to design a gui in QtDesigner, you can absolutely hand code a gui in Python using PyQt5. If you were to build your gui by hand, you can still use the provided gui_template.py, however you would not need to follow the steps below for getting set up. You would create your gui objects within the init function of the gui template rather than importing the Ui_form and calling the setup_Ui method on your class. The resources at the end of this document have instructions for hand coding a gui using PyQt5 if you are interested. I chose to use QtDesigner for the purposes of this workshop, as it allows us to get straight to the more technical aspects of GUI design.

## Using the Python GUI template with your UI file to build a GUI

If you open the ui file generated from QtDesigner as-is in your IDE, you will see that it looks like a xml file. In order to make use of the ui file we need to compile it into python code. Luckily, PyQt5 comes with a ui to py compiler that you can run in your command line:

```pyuic5 -o (output_file.py) (input_file.ui)```

You should run this from the command prompt that has your virtual environement with PyQt5 active, and you will need to be inside the directory containing your UI file.

You will now have a new python file in your directory, and can open it in spyder. Take note at the top of the file 'Warning! All changes made in this file will be lost'. This is to let you know that no edits should be made inside this script, it is generated code and will be rewritten if you make any changes to your gui in QtDesigner and recompile. The purpose of this script is to build the ui that our main window/widget class will operate on. We will import the class from this file into our gui_template, call it on our main window/widget to build the gui, and may refer to it when writing slots and signals.

Before getting started, ensure that you have both your gui_template.py and the compiled ui within the same working directory.

## Getting Set Up

#### Step 1

Import just the class from the generated python file to your gui template, ex:

``` from login_window import ("class name")  ```

#### Step 2

If you built your ui in QtDesigner as something other than widget, such as main window or dialog, adjust the name and subclass of your main class to reflect the appropriate option. If you built a main window in QtDesigner, the class in your GUI template should look like this:

``` class guiName(qtw.QMainWindow):```

#### Step 3

Initialize the ui object inside the init function

``` self.ui = "class name"()```

#### Step 4

Call the setupUi method of ui on your class to build the GUI:

``` self.ui.setupUi(self)```

This is all that needs to be done to get started, from here you can start to implement the actual functionality of your GUI.

## Signals & Slots

Unlike a console mode application, which is executed in a sequential manner, a GUI based application is event driven. Functions or methods are executed in response to user’s actions like clicking on a button, selecting an item from a collection or a mouse click, and are called events. Widgets used to build the GUI interface act as the source of such events. Each PyQt widget, which is derived from QObject class, is designed to emit ‘signal’ in response to one or more events. The signal on its own does not perform any action. Instead, it is ‘connected’ to a ‘slot’. The slot can be any callable Python function.

Source: https://www.tutorialspoint.com/pyqt/pyqt_signals_and_slots.htm

Lets write a basic function that can be used as a slot for our login button being clicked. You may need to reference your generated code to check what you named your gui objects. For now, it should look something like this:

```
    def auth(self):
        
        username = self.ui.edituser.text()
        password = self.ui.editpass.text()
        
        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'sucess', 'you have logged in')
        else:
            qtw.QMessageBox.critical(self, 'Failure', 'You have not logged in')
```

In order for the login button to execute this function, we need to connect it to our auth function using a signal. Your signals should generally be located inside your init function. For a clickable button, your signal should look like this:

``` self.ui.submitbutton.clicked.connect(self.auth) ```

Thre are a couple parts to this signal. You have to reference the ui class, the name you gave to the button object, the type of signal, and the connection. You then pass the slot (auth function in this case) to the signal. When you pass in a function as a slot, you should not call the function using ().



## Resources for PyQt5:

### Tutorials:

https://www.tutorialspoint.com/pyqt/index.htm

https://www.youtube.com/playlist?list=PLXlKT56RD3kBu2Wk6ajCTyBMkPIGx7O37

### Documentation:

https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index

https://doc.qt.io/qtforpython/

https://doc.bccnsoft.com/docs/PyQt5/