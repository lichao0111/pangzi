#!/bin/bash

# IP access
IP=('192.168.1.15' '192.168.1.16' '192.168.1.17' '192.168.1.18' '192.168.1.17' '192.168.1.137' '192.168.1.112')
start_time=`date +%s`

[ -e /tmp/fd1 ] || mkfifo /tmp/fd1
exec 3<>/tmp/fd1
rm -rf /tmp/fd1

for ((i=1;i<=10;i++))
do
        echo >&3
done
for ((i=0;i<${#IP[*]};i++))
do
read -u3
{
        sleep 1
        echo 'success'${IP[i]}
        echo >&3
}&
done
wait
stop_time=`date "+%s"`
echo "TIME:`expr $stop_time - $start_time`"
exec 3<&-
exec 3>&-
