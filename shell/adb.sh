#!/bin/bash

# resume activity
alias topActivity="adb shell dumpsys activity | grep "mResumedActivity" "

# activity TaskRecord
activityTaskRecord() {
  log_num=20
  if [ -n "${1}" ] ;then
    log_num=${1}
  fi
  adb shell dumpsys activity | grep -A "${log_num}" com.android.server.wm.RootActivityContainer
}

# phone version，need root
alias phoneVersion="adb shell cat /system/build.prop | grep ro.build.software.version"
