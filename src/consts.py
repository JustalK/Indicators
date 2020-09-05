NAME_MENU = 'Latsuj Menu'
NAME_SETTING = 'Latsuj Settings'
BACKGROUND_COLOR = '#3e3e3e'
BORDER_COLOR = '#222222'
MENU_COLOR = '#343434'
MENU_TEXT_COLOR = '#FFF'
MENU_TEXT_ACTIVE_COLOR = '#3e3e3e'
MENU_SIZE = 260
COMMANDS = {
    'Bashrc': 'gedit ~/.bashrc',
    'Crontab': "gnome-terminal -e 'sudo crontab -e'",
    'Wordpress-compass': "gnome-terminal --working-directory=~/eclipse-workspace/wordpress/wp-content/themes/latsuj/ -e 'compass watch'"
}
