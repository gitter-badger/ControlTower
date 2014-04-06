# Control Tower Tester Program
# Author: Kenny Luong
#
# Use this script as an example for ControlTower

from ControlTower import ControlTower

server_path = '../../'
server_name = 'api-server.py'
screen_name = 'TesterScreen'

supervisor = ControlTower(server_path, server_name, screen_name)

while True:
	supervisor.get_menu_option()
