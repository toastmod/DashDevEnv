echo "=setting max partitions to 8="
sudo modprobe nbd max_part=8
echo "=ensuring /mnt/MALTA-DRIVE directory exists="
mkdir /mnt/MALTA-DRIVE
echo "=connecting qemu to block device /dev/ndb0="
sudo qemu-nbd --connect=/dev/nbd0 ./debian_squeeze_mipsel_standard.qcow2
echo "=mounting block device="
sudo mount /dev/nbd0p1 /mnt/MALTA-DRIVE
echo "=job finihsed="
