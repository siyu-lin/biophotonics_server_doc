# Server GUI
## (sudo) GNOME Desktop Environment (GDM) is Installed
```
sudo apt update
sudo apt install ubuntu-desktop
```

## After installation is done, reboot
```
sudo reboot
```

## To confirm GDM is active
```
systemctl status gdm3
```

## (sudo) Restart GDM
```
sudo systemctl start gdm3
```
or
```
sudo systemctl restart gdm3
```

## To Use the GDM GUI on Windows
1. Download [MobaXterm](https://mobaxterm.mobatek.net/) with the free edition.
2. Open the executable(.exe) file and choose **Session** -> **SSH**
3. In the **Remote Host** box, type in the IP address of the server
4. Check the **Specify Username** box and type in your username. 
5. Click OK and enter password whenever prompted
6. In the opened terminal, type ```gnome-session``` and the GUI should pop up.

