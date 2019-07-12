# pyopengl requires GLIBCXX_3.4.26
rm /opt/anaconda3/lib/libstdc++.so
rm /opt/anaconda3/lib/libstdc++.so.6
ln -s /usr/lib64/libstdc++.so.6 /opt/anaconda3/lib/libstdc++.so.6
ln -s /opt/anaconda3/lib/libstdc++.so.6 /opt/anaconda3/lib/libstdc++.so
