#!/bin/bash
# path to logfile
LOGPATH="/data0/logs"
TIMESTAMP_TODAY="$(date +%Y%m%d)"
LOGFILE=${LOGPATH}/${TIMESTAMP_TODAY}
DELAY=60
COUNT=60

writelog_memory() {
        echo " ###################################################" >>${LOGFILE}_memory_status.log 2>&1
        echo "[`date +%Y-%m-%d-%H-%M`] $*" >>${LOGFILE}_memory_status.log 2>&1
}
writelog_cpu() {
        echo " ###################################################" >>${LOGFILE}_cpu_status.log 2>&1
        echo "[`date +%Y-%m-%d-%H-%M`] $*" >>${LOGFILE}_cpu_status.log 2>&1
}
writelog_top() {
        echo " ###################################################" >>${LOGFILE}_top_status.log 2>&1
        echo "[`date +%Y-%m-%d-%H-%M`] $*" >>${LOGFILE}_top_status.log 2>&1
}
writelog_io() {
        echo " ###################################################" >>${LOGFILE}_io_status.log 2>&1
        echo "[`date +%Y-%m-%d-%H-%M`] $*" >>${LOGFILE}_io_status.log 2>&1
}
writelog_network() {
        echo " ###################################################" >>${LOGFILE}_network_status.log 2>&1
        echo "[`date +%Y-%m-%d-%H-%M`] $*" >>${LOGFILE}_network_status.log 2>&1
}
cpu_log() {
        writelog_cpu()
        /usr/bin/ps -aux | sort -k3nr | head -20 >>${LOGFILEE}_cpu_status.log 2>&1 &
}
memory_log() {
        writelog_memory()
        /usr/bin/ps -aux | sort -k4nr | head -20 >>${LOGFILE}_memory_status.log 2>&1 &
}
io_log() {
        writelog_io()
        /usr/bin/iostat -t -k -x ${DELAY} ${COUNT} >>${LOGFILE}_io_status.log 2>&1 &
}
network_log() {
        writelog_network()
        /usr/bin/sar -n DEV ${DELAY} ${COUNT} >>${LOGFILE}_network_status.log 2>&1 &
}
memory_log()
cpu_log()
io_log()
network_log()