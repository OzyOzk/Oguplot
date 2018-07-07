__Oguplot Repository__
=====================================

Repository to contain source code and versions of the python
live plot project. Will contain;

* Code
* Plan
* Workflow
* Research
* Features to be added
### Demo

[Demo of the script in action](https://www.youtube.com/watch?v=c8xMLtfUHTE)

### Current Issues:

Pyserial warning. The following error warning keeps coming up when I run on Windows 7 (does not happen on Ubuntu 14.04)
```
SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)
```
Restarting the kernel is a solution. Removing all variables also works. (From IPython console in Spyder)

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

