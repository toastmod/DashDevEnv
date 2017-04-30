-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1,SHA256

Debian Squeeze and Wheezy mipsel images for QEMU
================================================

This directory contains Debian Squeeze and Wheezy mipsel images for QEMU and
the corresponding kernels and initrds:
  818379fa126f4801fbfd6825297bd7fb  debian_squeeze_mipsel_standard.qcow2
  39a2eda46f8d3ca1cf34e8b13bbae9dd  vmlinux-2.6.32-5-4kc-malta
  9d8ce8e757ea04bc9ae7fe2b534ca93a  vmlinux-2.6.32-5-5kc-malta
  bc8fc7e011aa50b329a567c3ebc89ac3  debian_wheezy_mipsel_standard.qcow2
  6010b10d719e6bb55975ae8e1904daeb  vmlinux-3.2.0-4-4kc-malta
  9d450a6ba558a540d9bc2fe83b8e0c93  vmlinux-3.2.0-4-5kc-malta

Both images are 25GiB images in QCOW2 format on which a Debian Squeeze or
Wheezy "Standard system" installation has been performed. The other
installation options are the following:
  - Keyboard:       US
  - Locale:         en_US
  - Mirror:         ftp.debian.org
  - Hostname:       debian-mipsel
  - Root password:  root
  - User account:   user
  - User password:  user

To use this image, you need to install QEMU 1.1.0 (or later). Start QEMU
with the following arguments for a 32-bit machine:
  - qemu-system-mipsel -M malta -kernel vmlinux-2.6.32-5-4kc-malta -hda debian_squeeze_mipsel_standard.qcow2 -append "root=/dev/sda1 console=tty0"
  - qemu-system-mipsel -M malta -kernel vmlinux-3.2.0-4-4kc-malta -hda debian_wheezy_mipsel_standard.qcow2 -append "root=/dev/sda1 console=tty0"

Start QEMU with the following arguments for a 64-bit machine:
  - qemu-system-mips64el -M malta -kernel vmlinux-2.6.32-5-5kc-malta -hda debian_squeeze_mipsel_standard.qcow2 -append "root=/dev/sda1 console=tty0"
  - qemu-system-mips64el -M malta -kernel vmlinux-3.2.0-4-5kc-malta -hda debian_wheezy_mipsel_standard.qcow2 -append "root=/dev/sda1 console=tty0"

By default QEMU emulates a machine with 128MiB of RAM. You can use the -m option
to increase or decrease the size of the RAM. It is however limited to 256MiB
with a 32-bit kernel. With a 64-bit kernel and QEMU >= 1.7, it is possible to
use up to 2047MiB of RAM, passing the memory map to the kernel, adding a mem=
argument to the append parameters as follow: "mem=256m@0x0 mem=XXXm@0x90000000"
where XXX represents the total memory size minus 256MiB. If you don't want to
start QEMU in graphic mode, you can use the -nographic option. The image is
configured to display a login prompt on the first serial port (ttys0). If you
want to switch the boot messages to the serial port, you need to replace
"console=tty0" by "console=ttyS0".

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iD8DBQFTpqgnw3ao2vG823MRAryvAJ9BY0gla6Edv4pt7Ld028W3vEBo7ACdEpk9
LZiI6FjklIYcMeKMpxvkm/eJAhUDBQFTpqgnupx4Bh3djJsBCGXFEACc6uS0CWrn
WJVcvK+t+dY3qc5I150XbuWPeCoePKmn3TvpxxsnPq4LqbgPmoQd4iddwcUqivK3
/Tw/CNdG7dfxKygDBgA1Af3RhTKwOm3E3WvIPpo1CEWMmX/gk6D/AweTIwtlUewU
vjfqL6RUJrt1CK9mbJbHs+NQTFPF7+Y67bArWEEhNG9+nobM8uHeo+jN0XQfurF3
R93ZGaO/vDTpieidgn94P/+ukhl6Y0+XGD+D1mcLk0dc/7okl3JLnnxR9/3vkrh/
dDEVsfXxKHRu9u0YUcMCWCWVYS5lqrv0Y4NwnT2/5KCKQatOgEtc91OZROvwQe1U
1AevBjyLsWCcXbtgLL0O5XKsiRVZnbv5M9eCoeBTt1f2WfycQh/lyan7FB47v3wE
2z1oqWMEhfQjPpsEWGRRRW17WhM4U8Q4tINMzkcnXNODq4bkLEfFxTcoGEYtGJne
+0t7hheV+mfUsruXBN0DOBRNn5ey4WUGLZHvddGloNAP21ZgANS3bLM7YmXVvvM8
UDuMkbljTI4BDcgArw6Op2LjuPjOObQrGVEiZYj6MhXFDI746VRs35jpVqT73s1F
QWV23MFtpOY6lZdyBZgk3YxvE6OzODQ/OG2onKmOM3c3+etYVB74NNGNgv4g3CrM
mDaUnKp7HComC2bxh+K8NF3fMJCP+oyWHg==
=rHUr
-----END PGP SIGNATURE-----
