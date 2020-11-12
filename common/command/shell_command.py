from common.log.term_clolor import *


def shell(string):
    return system_shell(string)


def shell_with_color(string, foreground_color=None, background_color=None, mode=None):
    print(get_color_text(popen_shell(string), foreground_color, background_color, mode))


def shell_with_green(string, bold=True):
    if bold:
        print(get_color_text(popen_shell(string), ForegroundColor.GREEN, None, Mode.BOLD))
    else:
        print(get_color_text(popen_shell(string), ForegroundColor.GREEN, None, None))


def shell_with_yellow(string, bold=True):
    if bold:
        print(get_yellow_bold(popen_shell(string)))
    else:
        print(get_yellow_normal(popen_shell(string)))


def shell_with_red(string, bold=True):
    if bold:
        print(get_red_bold(popen_shell(string)))
    else:
        print(get_red_normal(popen_shell(string)))


def system_shell(string):
    return os.system(string)


def popen_shell(string):
    return os.popen(string).read()


if __name__ == '__main__':
    popen_shell("cat shell_command.py")
    system_shell("cat shell_command.py")
