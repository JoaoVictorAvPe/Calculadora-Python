from pathlib import Path

ROOT = Path(__file__).parent.parent
ICON_PATH = ROOT / 'assets' / 'icons' / 'icon.png'

#FONT
BIG_FONT_SIZE = 30
MEDIUM_FONT_SIZE = 20
SMALL_FONT_SIZE = 12

#SPACEMENT
TEXT_MARGIN = 10
MINIMUN_WIDTH = 400

#STYLE
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'

if __name__ == '__main__':
    print(ICON_PATH)