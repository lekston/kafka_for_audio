#! /bin/bash

kafka_is_running=`ps -ef | grep -E "java.*kafka.*server" | sed '/grep.*java/d' | wc -l`
kafka_path=../kafka_install/

if [[ $? && $kafka_is_running -eq "0" ]]; then
    echo "starting local kafka server"
    pushd .
    cd $kafka_path
    TMUX='' tmux new-session -d -s zookeeper './bin/zookeeper-server-start.sh config/zookeeper.properties'
    TMUX='' tmux new-session -d -s kafka_server './bin/kafka-server-start.sh config/server.properties'
    # NOTE: setting "TMUX=''" allows this to execute correctly also when called from within tmux
    popd
else
    echo "kafka server seems to be running"
fi
