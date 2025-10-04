#how to uninstall jenkins and all its data
sudo systemctl stop jenkins
sudo systemctl disable jenkins
sudo apt-get remove jenkins -y
sudo apt-get purge jenkins -y
sudo apt-get autoremove -y
sudo rm -rf /var/lib/jenkins
sudo rm -rf /var/log/jenkins
sudo rm -rf /etc/default/jenkins
sudo rm -rf /etc/init.d/jenkins
sudo rm -rf /etc/apt/sources.list.d/jenkins.list
sudo rm -rf /etc/apt/keyrings/jenkins-keyring.asc
sudo systemctl status jenkins






