# DashDevEnv
Dash OS Development Environment for Ubuntu users

# How do I use this?
Download these files as a zip, unpack wherever you want, make sure qemu is install, and finally run the startvm-nographic.sh script.
If you want to back up the current vm image, just run the savebackup.sh script.

# Making a new chroot
Run the mount_qcow.sh to mount the current qemu image, it will be mounted in /mnt/MALTADRIVE
Copy all contents of MALTADRIVE (except for dev) to a folder where you want to store the chroot.
That folder is the chroot, congrats u did it!
