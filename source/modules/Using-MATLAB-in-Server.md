# Using MATLab on Server
If you (your user account) are using MATLAB on the server for the first time, please ask the admin (with sudo access) to activate the Linux gdm3 GUI. Then, please use your user account to enter GUI and activate MATLAB with your Education licenses.

You can find the MATLAB executable located at the path in our server
```
/usr/local/bin/matlab/matlab
```

To run a .m file without opening up the GUI
```
/PATH/TO/MATLAB -nodisplay -nosplash -nodesktop -r "run('PATH/TO/MATLABFILE.m');exit;"
```
Example
```
/usr/local/bin/matlab/matlab -nodisplay -nosplash -nodesktop -r "run('/home/biophotonics/Desktop/hello_world/hello_world.m');exit;"
```

Note: A welcome message from MATLAB will be printed every time you execute a code. In order to ignore the message append the following command to the end where and adjust the number 11 to the number of lines to ignore.

```| tail -n +11```

Full Example
```
./usr/local/bin/matlab -nodisplay -nosplash -nodesktop -r "run('/home/biophotonics/Desktop/hello_world/hello_world.m');exit;" | tail -n +11
```


Tips:

It might be helpful to encapsulate the code above to a shell script so that every time you only have to specify the .m file to execute the code.