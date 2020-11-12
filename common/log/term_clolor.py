from common.log.color_constants import *
import os


def get_normal(string):
    return get_color_text(string, None, None, None)


def get_yellow_bold(string):
    return get_color_text(string, ForegroundColor.YELLOW, None, Mode.BOLD)


def get_yellow_normal(string):
    return get_color_text(string, ForegroundColor.YELLOW, None, None)


def get_red_bold(string):
    return get_color_text(string, ForegroundColor.RED, None, Mode.BOLD)


def get_red_normal(string):
    return get_color_text(string, ForegroundColor.RED, None, None)


def get_color_text(string, foreground_color=None, background_color=None, mode=None):
    f"""
    :param string: string to use style
    :param foreground_color: foreground color, support list see {ForegroundColor}
    :param background_color: background color, support list see {BackgroundColor}
    :param mode: mode, support list see {Mode}
    :return: 
    """
    style_list = []
    if mode is not None:
        style_list.append(str(mode.value))
    if foreground_color is not None:
        style_list.append(str(foreground_color.value))
    if background_color is not None:
        style_list.append(str(background_color.value))

    style = ';'.join(style_list)
    style = '\033[%sm' % style
    end = '\033[%sm' % 0
    return '%s%s%s' % (style, string, end)


if __name__ == '__main__':
    print(get_color_text("hello world", ForegroundColor.RED, None, None))
    print(get_color_text("hello world", ForegroundColor.CYAN, BackgroundColor.WHITE, Mode.BOLD))
    print(get_color_text("hello world", ForegroundColor.BLACK, BackgroundColor.WHITE, Mode.UNDERLINE))
    print(get_color_text("hello world", ForegroundColor.GREEN, BackgroundColor.PURPLE, Mode.BOLD))
    print(get_color_text("hello world", ForegroundColor.YELLOW, BackgroundColor.WHITE, Mode.BLINK))
    print(get_color_text("hello world", ForegroundColor.PURPLE, BackgroundColor.WHITE, Mode.NORMAL))
    print(get_color_text("hello world", ForegroundColor.CYAN, BackgroundColor.PURPLE, Mode.BOLD))
    print(get_color_text("hello world", ForegroundColor.GREEN, BackgroundColor.WHITE, None))
    print(get_color_text("hello world", ForegroundColor.BLACK, BackgroundColor.WHITE, None))

    print(get_normal("hello cat"))
    print(get_yellow_bold("hello cat"))
    print(get_yellow_normal("hello cat"))
    print(get_red_bold("hello cat"))
    print(get_red_normal("hello cat"))

    os.system("echo %s" % get_red_normal("hello leo ~~ "))
