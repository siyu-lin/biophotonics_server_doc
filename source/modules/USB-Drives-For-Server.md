# Using USB Drives For Server
When plugging USB Drivers directly onto server for data transfer. The following steps is required:

## 1. Identifying the disk
Use the following command to see all the storage devices associated with the server and figure out which one is the USB drive
```bash
lsblk
```

Useful command to refresh lsblk and ask the server to rescan the bus
```bash
partprobe
```

## 2. Create a folder to mount the disk
```bash
sudo mkdir /media/YOURFOLDER
```
You can also recycle other unused folders to mount the drive.

## 3. Mounting the disk onto the folder
```bash
sudo mount /dev/YOURDRIVE /media/YOURFOLDER
```

## 4. Manipulate the data
Now you should have read/write access to the drive through this folder
### Copying Files with Progress Bar
```bash
sudo rsync --progress SOURCE_PATH DESTINATION_PATH
```
For recursive copy ( folders in folders in folders... ) use the flag
```bash
-r
```

## 5. Unmount/Eject the USB drive
Make sure you quit the mounting directory before you ```umount``` the drive.

If you ```umount``` the drive, you should be able to re- ```mount``` it back immediately as the underlying device is still available.
```bash
sudo umount -l /media/MOUNTINGPATH
```
Please wait patiently for the drive to umount to prevent data corruption.


```bash
sudo eject /dev/YOURDEVICE
```
Note:
```eject``` should automatically ```umount``` the drive. If you need access again, you need to reboot the USB or (easier) plug-out and plug it back in the USB driver.


There's a chance you may see ``` eject: unable to eject ```

The udisksctl command is a helpful tool for managing disk drives and can be used to eject the drive safely:
```
udisksctl unmount -b /dev/sdX1
udisksctl power-off -b /dev/sdX
```
Replace /dev/sdX with the appropriate device identifier for your portable drive, which you can find using lsblk. The power-off command will turn off the drive, making it safe to physically remove.
