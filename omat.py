from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    scenes = []
    effects = [
        Print(screen,
              FigletText("JOGET BRO",
                         font='banner3' if screen.width > 80 else 'banner'),
              screen.height//2-3,
              colour=7, bg=7 if screen.unicode_aware else 0),
    ]
    scenes.append(Scene(effects))
    effects = [
        Print(screen,
              ColourImageFile(screen, "joget.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height,
              speed=1),
        Scroll(screen, 2)
    ]
    scenes.append(Scene(effects))
    effects = [
        BannerText(screen,
                   ColourImageFile(screen, "joget.gif", screen.height-2,
                                   uni=screen.unicode_aware, dither=screen.unicode_aware),
                   0, 0),
    ]
    scenes.append(Scene(effects))
    effects = [
        Print(screen,
              FigletText("THANKS",
                         font='banner3' if screen.width > 80 else 'banner'),
              screen.height//2-3,
              colour=7, bg=7 if screen.unicode_aware else 0),
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError:
            pass