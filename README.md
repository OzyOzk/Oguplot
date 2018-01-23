__Oguplot Repository__
=====================================

Repository to contain source code and versions of the python
live plot project. Contains:

* Code
* Plan
* Workflow
* Research
* Features to be added

Current Issues:

The lists are growing!

These lines need to be replaced:

```python
data1 = [0]
data2 = [0]
data3 = [0]

def update():
    global curve1, curve2, data1, data2, data3
    line = ser.readline()
    csv = line.split(',')
    if len(csv) == 3:
	    set1 = csv[0]
	    set2 = csv[1]
	    set3 = csv[2]
	    #print set1, set2
	    data1.append(float(set1))
	    data2.append(float(set2))
            data3.append(float(set3))
```

These list just keep growing. Also, I'm appending floats which are 32 bits each. These arrays (data1, data2, data3) grow in size significantly (3000 elements in 1 minute). This could potentially lead to some memory issues. 
3000 x 3 x 32=288000.

288000/4=72000 bytes

72000/1000=72 megabytes/minute


