# Basic Commands
ChatGPT is a good source, if you are not familiar with Linux

## Terminal type
Our terminal provides the Shell terminal type by default. 
For the group users, you can define your terminal type, such as ```bash```. 
You can type ```bash``` in the terminal to change the terminal type.
Different types of terminals may have distinctive features. This can be your personal preference. 

## Upload files to a docker container
Assuming you are in the terminal at your local machine (MacOS).
To upload a single file:
```
docker cp /path/to/local/file my-ssh-container:/path/in/container/
```

## Upload a folder with all subfolders to a remote SSH directory
Assuming you are in the terminal at your local machine (MacOS).
```
scp -r /path/to/local/folder username@server_ip:/path/to/destination/folder
```
Enter the user's password when prompted