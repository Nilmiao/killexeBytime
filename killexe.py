#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by nil_mmm
import os
import time
import sys

program = "Thunder.exe"
pids = []
minute = 0.1
sleepTime = minute * 60

def killexe(stime,program):
    count = 0
    while ( count < stime):
        ncount = stime - count
        sys.stdout.write("\r%d " % ncount)
        sys.stdout.flush()
        time.sleep(1)
        count += 1
    # 获取program的PID
    for getpid in os.popen("tasklist | findstr %s" % program).readlines():
        pids.append(getpid.split()[1].splitlines()[0])
    # kill掉获取的programPID
    for pid in pids:
        os.system("taskkill /F /PID %s" % pid)

    print program + " 关闭成功"

if __name__ == "__main__":
    killexe(sleepTime,program)
