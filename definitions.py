from pygame import font
from pygame.font import SysFont as fonts

font.init()

class Fonts:
    quicksand80 = fonts("quicksand", 80)
    notomono35 = fonts("notomono", 35)
    notomono30_italic = fonts("notomono", 30, italic=True)
    quicksand22 = fonts("quicksand", 22)
    quicksand22b = fonts("quicksand", 22, bold=True)
    notomono22 = fonts("notomono", 22)
    quicksand20 = fonts("quicksand", 20, bold=True)
    quicksand20n = fonts("quicksand", 20)
    quicksand16 = fonts('quicksand', 16, italic=True)
    notomono20_italic = fonts("notomono", 20, italic=True)