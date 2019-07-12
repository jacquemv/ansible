rsync -uqphaxHAX --delete /home /backup
echo "local rsync home: `date`" >> /backup/backup.log

