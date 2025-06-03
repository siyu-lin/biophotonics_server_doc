# Manipulating the Disks
## Identify the Disks
For all disks
```
lsblk
```
or for mounted drives
```
df -h
```

## (sudo) Disk Partitioning(GPT Format>2TB) 
```
sudo parted /dev/DRIVENAME
```
Ex.
```
sudo parted /dev/nvme1n1
```
Type 'help' for instructions
To create a GPT partition table on the disk
```
mklabel gpt
```
Set the unit to sectors (each sector is 512 Bytes)
```
unit s
```
To create a new partition
```
mkpart primary ext4 2048s 100%
```
This will set the whole disk as a partition.
The type ```quit``` to exit parted.
After creating the GPT partition, format it with a filesystem of your choice. (Example with ext4)
```
sudo mkfs.ext4 /dev/DISK_PARTITION_NAME
```
## (sudo) Mount disk
After the partition is done, mount the disk.
Make the folder in the root directory, and define your own DISK_NAME.
```
cd /
sudo mkdir /mnt/DISK_NAME
```
Then mount drive:
```
sudo mount /dev/DISK_PARTITION_NAME /mnt/DISK_NAME
```
After the mount is done, you can check the info with
```
df -h
```