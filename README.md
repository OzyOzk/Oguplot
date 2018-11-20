__Oguplot Repository__
=====================================

![sample_image](https://github.com/OzyOzk/Oguplot/blob/master/window_sample.png)

Repository to contain source code and versions of the python
live plot project. Will contain;

* Code
* Plan
* Workflow
* Research
* Features to be added
### Demo

[Demo of the old script in action](https://www.youtube.com/watch?v=c8xMLtfUHTE)

### Current Issues:

~~Pyserial warning. The following error warning keeps coming up when I run on Windows 7 (does not happen on Ubuntu 14.04)~~
```python
SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)
```
~~Restarting the kernel is a solution. Removing all variables also works. (From IPython console in Spyder)~~

**Issue resolved**. The program now checks if the port is available. 

Also resolved an issue where every second time the script is run from the ipython console, the kernel crashes. This is specifically
a spyder issue.This is due to the previous instance of QT not being ternimated when the script is shut, thus when the script is
executed again, the kernel crashes as Qt does not like more than one instance of itself running at once. Previously, a new instance
would be created at the start;

```python
    app = QtGui.QApplication([])
```

Now the instance is created only if one does not already exist. Otherwise old instance is used
```python
if not QtGui.QApplication.instance():
    app = QtGui.QApplication([])
else:
    app = QtGui.QApplication.instance()
```

### Added GUI

The script no longer plots as soon as it is run. Now the serial number of the device printing csv values needs to be entered. Hitting
poll button will then queery all connected serial devices for their serial numbers. If a matching serial number is found, the graph will start plotting. Also added a close button to close the current port. Hitting close will close the serial port and the plot will stop.

### Micro-controller setup

For testing I'm using an Arduino Uno Rev3 with an MPU6050. The code is printed to the serial monitor in comma separated format in x,y pairs on a new line. Any two values will work as long as they are separated by a comma. See below code for example;

```c++
Serial.print(AcX);Serial.print(",");Serial.println(AcY);
```
Where AcX and AcY are 16 bit signed integers (int16_t). See below for sample output in Serial monitor;

```
140,-140
48,-256
104,-188
176,-372
172,-208
-32,-204
124,-212
336,-388
0,-328
```

