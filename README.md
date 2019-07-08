# ansible
Fedora installation and administration

- download Fedora ISO

- create bootable USB using "ISO Image Writer"

- install Fedora

- format and configure data disks: using the utility "Disks", rename data disks to "data1", "data2", etc. and format them (ext4) if necessary. 
Then in each disk, create a directory "users" (owner: root, mode: 0777) and in one of them also a directory "backup" (owner: jacquem, mode: 0755).

- dnf install -y ansible

- git clone https://github.com/jacquemv/ansible.git

- cd ansible

- ansible-playbook -K workstation.yml

- additional customization: vincent.yml, fileserver.yml, adduser.yml

