#!/usr/bin/env python3

# dnf install -y arp-scan
import datetime
from subprocess import run, PIPE
from urllib.request import urlopen

# download table of MAC addresses
web_site = 'https://raw.githubusercontent.com/jacquemv/ansible/master/'
table_file = 'roles/scanip/templates/mac_table.txt'
table = urlopen(web_site+table_file).read().decode()

# build dict of MAC addresses
machines = {}
for line in table.split('\n'):
    items = line.split()
    for mac in items[1:]:
        machines[mac] = items[0]

# read /etc/hosts
ipdict = {}
with open('/etc/hosts', 'rt') as file:
    for line in file:
        if line.startswith('#'):
            continue
        items = line.split()
        if len(items) > 1:
            ip, name = items[0], items[1]
            if name != 'localhost':
                ipdict[name] = ip

# read the output of arp-scan
out = run(['arp-scan', '-l'], stdout=PIPE).stdout.decode()
for line in out.split('\n'):
    items = line.split()
    if len(items) > 1:
        ip, mac = items[0], items[1]
        if mac in machines:
            ipdict[machines[mac]] = ip

# update /etc/hosts
with open('/etc/hosts', 'wt') as file:
    file.write('# updated ' + str(datetime.datetime.now()) + '\n')
    file.write('127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n')
    file.write('::1         localhost localhost.localdomain localhost6 localhost6.localdomain6\n')
    for name, ip in ipdict.items():
        file.write(ip + ' ' + name + '\n')

