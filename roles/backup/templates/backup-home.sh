rsync -uqphaxHAX --delete /home /backup/home
echo "local rsync home: `date`" >> /backup/backup.log

