from common.command.shell_command import *
from git.git_alias import *


def gl(oneline=None, glg=None, author=None):
    option = [' ', ' ', ' ']
    if oneline is not None:
        option[0] = '--oneline'
    if glg is not None:
        option[1] = "--stat --color"
    if author is not None:
        option[2] = "--author=%s" % author
    shell_with_green(str_gl % (option[0], option[1], option[2]))


if __name__ == '__main__':
    gl(glg=True)
