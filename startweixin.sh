#!/bin/bash

#pkill -f uwsgi
ps -ef | grep uwsgi

echo "kill uwsig"
ps -ef | grep weixin-uwsgi | awk -F" " '{print $2}' | xargs sudo kill -9
#echo "kill uwsig end"
ps -ef | grep uwsgi
echo "restart uswig"
local_path=`pwd`
nohup $local_path/flask/bin/uwsgi weixin-uwsgi.ini &

echo "restart uwsig end"

ps -ef | grep uwsgi

sleep 3
sudo chmod 777 /tmp/s3.sock

sleep 3
a=`wget --save-headers http://www.pitaya-inc.com:9000/index -O /tmp/t.log && cat /tmp/t.log | grep "200 OK"`
if [ ${#a} -ne 0 ]; then
echo "start success"
else
echo "start fail "
fi
