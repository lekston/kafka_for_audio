#! /bin/bash

sudo apt install --fix-missing -y openjdk-11-jre-headless tmux

wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.13-3.2.0.tgz
tar -xf kafka_2.13-3.2.0.tgz
mv kafka_2.13-3.2.0 ../kafka_install

