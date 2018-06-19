__Oguplot Repository__
=====================================

Repository to contain source code and versions of the python
live plot project. Will contain;

* Code
* Plan
* Workflow
* Research
* Features to be added

Current Issues:

Pyserial warning. The following error warning keeps coming up when I run on Windows 7 (does not happen on Ubuntu 14.04)
```
SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)
```
Restarting the kernel is a solution.


<s>The lists need to be roled to avoid them getting too large.<\s>

<s>These lines need to be replaced:<\s>

Now popping after each append

```python
def update():
  global curve1, curve2, data1, data2, x
  line = ser.readline()
  csv = line.decode().split(',')
  if len(csv) == 2:	    
    set1 = csv[0]
    set2 = csv[1]
    data1.append(float(set1))
    data2.append(float(set2))
    data1.pop(0)
    data2.pop(0)
    xdata1 = np.array(data1[-500:], dtype='float32')
    xdata2 = np.array(data2[-500:], dtype='float32')
    curve1.setData(xdata1)
    x += 1
    curve1.setPos(x, 0)
    curve2.setData(xdata2)
    curve2.setPos(x, 0)
    app.processEvents()
```



