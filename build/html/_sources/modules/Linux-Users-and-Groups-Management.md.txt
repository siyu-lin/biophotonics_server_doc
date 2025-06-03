# Setting up groups and accounts

## (sudo) How to Create a Group
Enter the following command in admin account

```
sudo groupadd GROUPNAME
```

Ex.

```
sudo groupadd yang_lab
```

If the user is going to use docker

Add the user to the docker group by
```
sudo usermod -a -G docker USERNAME
```


## (sudo) How to Create a User Under a Group

```
sudo useradd -G GROUPNAME USERNAME
```
```
sudo passwd USERNAME
```

Setup the password when promped.

Ex.
```
sudo useradd -G yang_lab Haowen_Zhou
```
```
sudo passwd Haowen_Zhou
```

Create a Folder for Each User(sudo access)

``` 
cd /home
sudo mkdir USERNAME
```
Ex.
```
cd /home
sudo mkdir Haowen_Zhou
```

Change ownership of Directory(chown --help)
```
sudo chown -R USER_NAME FOLDER_NAME
```

## Checking which Group the Current User Belongs To
```
groups
```
or
```
groups USERNAME
```
Ex.
```
groups Haowen_Zhou
```

## Adding a new group that a user is belonged to
```
sudo usermod -a -G groupName userName
```
Ex.
```
sudo usermod -a -G docker Haowen_Zhou
```