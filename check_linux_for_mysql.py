#!/usr/bin/python
# __author__="richard"
# coding=utf-8
#检测linux环境  1.numa检查 2.limit 检查 小于1025 设置为65535  3. 设置vm.swappiness=10 4.关闭selinux
import os, sys, time
import commands


def done_shell(shell_str):
    if len(shell_str):
        (status, output) = commands.getstatusoutput(shell_str)
        return status, output
    else:
        print "shell is null"
        exit()


def check_numa():
    str = 'numactl --hardware'
    (t1, t2) = done_shell(str)
    if t1 == 0:
        print "-----------check linux for mysql--------------------------"
        print "numa is on ,you can cloes it in BIOS"
        print t2
        print "-------------------------------------"
    else:
        print t2


def check_limit():
    str1 = "ulimit -n "
    open_files = done_shell(str1)

    if open_files[1] >= 1024:
        print "open files is %s" % (open_files[1])
    else:
        done_shell("unlimit -Sn 65535")

    str2 = "ulimit -u"
    max_u_processes = done_shell(str2)
    if max_u_processes[1] >= 1024:
        print "max_u_processess is %s" % (max_u_processes[1])
    else:
        done_shell("unlimit -Su 65535")
    print "-------------------------------------"


def check_swap():
    str3 = "cat /proc/sys/vm/swappiness"
    swap_t = done_shell(str3)
    if swap_t >= 60:
        done_shell("sysctl vm.swappiness=10")
    else:
        print "swappiness is ok "


def check_selinux():
    str4 = "getenforce"
    selinx = done_shell(str4)
    if selinx[1] == "Disabled":
        print "selinux is disbaled"
    else:
        done_shell("setenforce 0")
        print "selinux set 0"


def main():
    check_numa()
    check_limit()
    check_swap()
    check_selinux()

if __name__ == "__main__":
    main()
