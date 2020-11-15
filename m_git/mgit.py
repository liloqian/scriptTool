#!/usr/bin/python3
import os
import sys

from git import Git, InvalidGitRepositoryError, GitCommandError

from common.log.color_constants import ForegroundColor
from common.log.term_clolor import get_red_bold, get_color_text
from m_git.mgit_config import __base_code_path__, __module_name__


def grant_mgit(path):
    return __module_name__.__contains__(path)


def path_exist(path):
    return os.path.exists(__base_code_path__ % path)


def error_exit(error):
    print(get_red_bold("Error: %s" % error))
    sys.exit(-1)


def mgit(module_list=None, command=''):
    """
       Work with multiple Git at the same time warehouse
    """
    for module in module_list:
        if not grant_mgit(module):
            error_exit("this module have no grant from mgit!")
        if not path_exist(module):
            error_exit("this module don`t find from local disk!")
    for module in module_list:
        print(get_red_bold("---------------- %s ---------------- " % module))
        try:
            git = Git(__base_code_path__ % module)
        except InvalidGitRepositoryError as e:
            error_exit("InvalidGitRepositoryError: %s" % e)
            continue
        try:
            output = git.execute(command=command, shell=True)
            if output == '':
                output = '%s execute done!' % command
            print(get_color_text(output, foreground_color=ForegroundColor.GREEN))
        except GitCommandError as e:
            error_exit("GitCommandError: %s" % e)
            continue
        print('\n')


if __name__ == '__main__':
    command = 'git'
    module = []
    for argc in sys.argv[1:]:
        if argc.startswith('m'):
            module = argc.split(':')[1:]
            continue
        command += " %s" % argc
    if len(module) < 1:
        error_exit("please input command ~~\n"
                   "Example: mgit log m:1:2 ")
    if command == 'git':
        error_exit("please input module ~~\n"
                   "Example: mgit log m:1:2 ")
    mgit(module, command)
