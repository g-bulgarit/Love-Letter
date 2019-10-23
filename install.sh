
#----------------------------------|
#     __                           |
#    / /   ____ _   _____          |
#   / /   / __ \ | / / _ \         |
#  / /___/ /_/ / |/ /  __/         |
# /_____/\____/|___/\___/          |
#    / /   ___  / /_/ /____  _____ |
#   / /   / _ \/ __/ __/ _ \/ ___/ |
#  / /___/  __/ /_/ /_/  __/ /     |
# /_____/\___/\__/\__/\___/_/      |
#                                  |
#----------------------------------|

echo -e "Setting up static IP\n"
# request static IP with dhcpcd, I want to use the IP 10.0.0.9
sudo sed -i "\$interface wlan0" /etc/dhcpcd.conf
sudo sed -i "\$static ip_address=10.0.0.9/24" /etc/dhcpcd.conf
sudo sed -i "\$static routers=10.0.0.138" /etc/dhcpcd.conf
sudo sed -i "\$static domain_name_servers=10.0.0.138 8.8.8.8 192.168.0.1" /etc/dhcpcd.conf


echo -e "Setting up python pre-requisites\n"
# install python pre-requisite...
python -m pip install flask

echo -e "Setting up startup scripts \n"
# add sleep to startup
sudo sed -i "\$i sleep 10" /etc/rc.local

# add server to startup
sudo sed -i "\$i python /home/pi/Love-Letter/main.py &" /etc/rc.local

# add print_manager to startup
sudo sed -i "\$i python /home/pi/Love-Letter/print_manager.py &" /etc/rc.local

echo -e "Setting up duckDNS on startup\n"
# ping duckDNS on startup
sudo sed -i "\$i bash ~/duckdns/duck.sh >/dev/null 2>&1" /etc/rc.local

echo -e "Done!\n"