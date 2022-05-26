#! /bin/bash

# stop server
TMUX='' tmux kill-session -t zookeeper
TMUX='' tmux kill-session -t kafka_server

# clean-up logs
rm -rf /tmp/kafka-logs /tmp/zookeeper
