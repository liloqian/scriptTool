#!/bin/bash

RB_RED=$(printf '\033[38;5;196m')
RB_ORANGE=$(printf '\033[38;5;202m')
RB_YELLOW=$(printf '\033[38;5;226m')
RB_GREEN=$(printf '\033[38;5;082m')
RB_BLUE=$(printf '\033[38;5;021m')
RB_INDIGO=$(printf '\033[38;5;093m')
RB_VIOLET=$(printf '\033[38;5;163m')

say_zsh() {
	printf '%s         %s__      %s           %s        %s       %s     %s__   %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
	printf '%s  ____  %s/ /_    %s ____ ___  %s__  __  %s ____  %s_____%s/ /_  %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
	printf '%s / __ \%s/ __ \  %s / __ `__ \%s/ / / / %s /_  / %s/ ___/%s __ \ %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
	printf '%s/ /_/ /%s / / / %s / / / / / /%s /_/ / %s   / /_%s(__  )%s / / / %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
	printf '%s\____/%s_/ /_/ %s /_/ /_/ /_/%s\__, / %s   /___/%s____/%s_/ /_/  %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
	printf '%s    %s        %s           %s /____/ %s       %s     %s          %s\n' $RB_RED $RB_ORANGE $RB_YELLOW $RB_GREEN $RB_BLUE $RB_INDIGO $RB_VIOLET $RB_RESET
}

sourceAllShell() {
  cd $1 || exit
  # shellcheck disable=SC2045
  for shell_name in $(ls);
  do
    if [ "$shell_name" = "$2" ];then
      continue
    fi
    # echo $shell_name
    # shellcheck disable=SC1090
    source $shell_name && echo "source  $shell_name..."
  done
}

# init do something :)

# export python environment
local_path=$0
shell_path=${local_path%/*}
# Todo python environ ment ,pip3.8 install GitPython
export PYTHONPATH=/usr/local/lib/python3.9/site-packages:${shell_path%/*}:$PYTHONPATH

# source shell
sourceAllShell ${local_path%/*} ${local_path##*/}

alias mgit=" ../m_git/mgit.py"

# say hello
say_zsh
