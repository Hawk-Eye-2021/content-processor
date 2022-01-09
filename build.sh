sudo yum -y update
sudo yum -y install git
git clone https://github.com/Hawk-Eye-2021/content-processor.git
cd content-processor

# add swap
sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=8192
sudo chmod 600 /var/swap.1
sudo /sbin/mkswap /var/swap.1
sudo /sbin/swapon /var/swap.1


pip3 install -r requirements.txt --no-cache-dir
