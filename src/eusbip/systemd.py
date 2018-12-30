import os
import pathlib


unit_file_directory = pathlib.Path(os.sep)/'etc'/'systemd'/'system'


# copy to ^^^ usbipd.service
# systemctl enable usbipd




# pi@raspberrypi:~ $ cat /etc/systemd/system/usbipd.service
# [Unit]
# Description=USB-IP Daemon
# After=network.target
#
# [Service]
# ExecStart=/usr/local/sbin/usbipd
# Restart=always
#
# [Install]
# WantedBy=multi-user.target
# pi@raspberrypi:~ $ sudo systemctl start usbipd
# pi@raspberrypi:~ $ sudo systemctl status usbipd
# ● usbipd.service - USB-IP Daemon
#    Loaded: loaded (/etc/systemd/system/usbipd.service; enabled; vendor preset: enabled)
#    Active: active (running) since Sat 2018-12-29 17:18:58 EST; 4s ago
#  Main PID: 1363 (usbipd)
#    CGroup: /system.slice/usbipd.service
#            └─1363 /usr/local/sbin/usbipd
#
# Dec 29 17:18:58 raspberrypi systemd[1]: Started USB-IP Daemon.
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: starting usbipd (usbip-utils 2.0)
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: listening on 0.0.0.0:3240
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: listening on :::3240
# pi@raspberrypi:~ $ sudo systemctl stop usbipd
# pi@raspberrypi:~ $ sudo systemctl status usbipd
# ● usbipd.service - USB-IP Daemon
#    Loaded: loaded (/etc/systemd/system/usbipd.service; enabled; vendor preset: enabled)
#    Active: inactive (dead) since Sat 2018-12-29 17:19:08 EST; 8s ago
#   Process: 1363 ExecStart=/usr/local/sbin/usbipd (code=exited, status=0/SUCCESS)
#  Main PID: 1363 (code=exited, status=0/SUCCESS)
#
# Dec 29 17:18:58 raspberrypi systemd[1]: Started USB-IP Daemon.
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: starting usbipd (usbip-utils 2.0)
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: listening on 0.0.0.0:3240
# Dec 29 17:18:58 raspberrypi usbipd[1363]: usbipd: info: listening on :::3240
# Dec 29 17:19:08 raspberrypi usbipd[1363]: usbipd: info: shutting down usbipd
# Dec 29 17:19:08 raspberrypi systemd[1]: Stopping USB-IP Daemon...
# Dec 29 17:19:08 raspberrypi systemd[1]: Stopped USB-IP Daemon.
# pi@raspberrypi:~ $ sudo systemctl enable usbipd.service
# Created symlink /etc/systemd/system/multi-user.target.wants/usbipd.service → /etc/systemd/system/usbipd.service.
# pi@raspberrypi:~ $ sudo init 6
# Connection to 192.168.0.125 closed by remote host.
# Connection to 192.168.0.125 closed.
#  ✘  ~   master  ssh pi@192.168.0.125
# pi@192.168.0.125's password:
# Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l
#
# The programs included with the Debian GNU/Linux system are free software;
# the exact distribution terms for each program are described in the
# individual files in /usr/share/doc/*/copyright.
#
# Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
# permitted by applicable law.
# Last login: Sat Dec 29 17:20:08 2018
# pi@raspberrypi:~ $ sudo systemctl status usbipd
# ● usbipd.service - USB-IP Daemon
#    Loaded: loaded (/etc/systemd/system/usbipd.service; enabled; vendor preset: enabled)
#    Active: active (running) since Sat 2018-12-29 17:20:03 EST; 1min 7s ago
#  Main PID: 382 (usbipd)
#    CGroup: /system.slice/usbipd.service
#            └─382 /usr/local/sbin/usbipd
#
# Dec 29 17:20:03 raspberrypi systemd[1]: Started USB-IP Daemon.
# Dec 29 17:20:03 raspberrypi usbipd[382]: usbipd: info: starting usbipd (usbip-utils 2.0)
# Dec 29 17:20:03 raspberrypi usbipd[382]: usbipd: info: listening on 0.0.0.0:3240
# Dec 29 17:20:03 raspberrypi usbipd[382]: usbipd: info: listening on :::3240
