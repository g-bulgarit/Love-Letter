
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

echo -e "Setting up python pre-requisites\n"
# install python pre-requisite...
python -m pip install flask

echo -e "Setting up startup scripts \n"
# add sleep to startup
sudo sed -i "\$i sleep 10" /etc/rc.local

# add server to startup
sudo sed -i "\$i python /home/pi/LoveLetter/main.py &" /etc/rc.local

# add print_manager to startup
sudo sed -i "\$i python /home/pi/LoveLetter/print_manager.py &" /etc/rc.local

echo -e "Done!\n"