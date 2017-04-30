echo "=unmounting qcow2 image from /mnt/MALTA-DRIVE="
sudo unmount /mnt/MALTA-DRIVE
echo "=disconnecting qemu from block device="
sudo qemu-nbd --disconnect /dev/nbd0
echo "=job finished="
