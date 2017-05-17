# DashDevEnv
Dash OS Development Environment for Ubuntu users

# How do I use this?
Download these files as a zip, unpack wherever you want, make sure qemu is installed, and finally run the startvm-nographic.sh script.
If you want to back up the current vm image, just run the savebackup.sh script.

# Making a new chroot
Run the mount_qcow.sh to mount the current qemu image, it will be mounted in /mnt/MALTADRIVE
Copy all contents of MALTADRIVE (except for dev) to a folder where you want to store the chroot.
Inside this folder make a new file called startchroot.sh, and inside paste this:

```bash
echo "Mounting system stuff..."
mount -o loop /dev dev/
mount -o loop /proc proc/
mount -o loop /sys sys/
mount -o loop /tmp tmp/
mount -t devpts dev/pts
echo "Starting chroot!"
chroot .
```

Now put the folder on an ext3 formatted usb drive, and connect it to the Dash.
SSH into the Dash as root, cd into /mnt/usb/NAMEOFYOURCHROOTFOLDERHERE and run the startchroot.sh
Congrats, you are in a chroot!
