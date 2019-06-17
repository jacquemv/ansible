#!/usr/bin/env python

# dnf install -y arp-scan
import datetime
from subprocess import run, PIPE

machines = {
    'e0:cb:4e:e6:d7:18': 'fileserver',
    'bc:ee:7b:9b:32:79': 'vincent',
    '30:5a:3a:79:20:d6': 'ariane',
    '30:5a:3a:79:21:40': 'eric',
    'f4:6d:04:e4:ee:83': 'samuel',
    '30:5a:3a:79:20:08': 'alena',
    '00:26:18:2e:82:b8': 'oldpc'
}

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

