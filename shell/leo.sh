#!/bin/bash

# kill java process
kJava() {
	# ps -ef | grep java | awk '{print $2}'
	for pid_num in $(ps -ef | grep 'java' | awk '{print $2}')
	do
		# echo $pid
		kill -9 $pid_num
	done
}

# calculate code lines
codeLine() {
	for i in "$@";
	do
		# shellcheck disable=SC2038
		find . -name "$i" > /dev/null | xargs wc -l
	done
	# find . "(" -name "*.java" -or -name "*.mm" ")" -print | xargs wc -l
}