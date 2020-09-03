NAME_MENU = 'Latsuj Menu'
BACKGROUND_COLOR = '#3e3e3e'
MENU_COLOR = '#343434'
MENU_SIZE = 260
COMMANDS = {
    'Bashrc': 'gedit ~/.bashrc',
    'Crontab': "gnome-terminal -e 'sudo crontab -e'",
    'Wordpress-compass': "gnome-terminal --working-directory=~/eclipse-workspace/wordpress/wp-content/themes/latsuj/ -e 'compass watch'"
}
