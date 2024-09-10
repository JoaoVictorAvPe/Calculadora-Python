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

if __name__ == '__main__':
    print(ICON_PATH)