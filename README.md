# Fun project to explore ROS-like features of kafka topics

## Getting started
### Installation
The script ``./bin/initial_setup.sh`` will download a local installation of kafka from apache.
NOTE: the signature checking is skipped so please download manually if it is critical for your use case.

### Starting the server
Use ``./bin/start_local_kafka_server.sh``

### Stopping the server
Use ``./bin/stop_local_kafka_server.sh``
NOTE: this also removes all events that remained in any used kafka topics.

### Demo run
Open 2 terminals, in the first one start:
```
python3 ./src/async_consumer.py
```
In the other run:
```
python3 ./src/producer.py
```

## Docs

For kafka installation and basic use please see:
[Kafka Quickstart](https://kafka.apache.org/quickstart)

For details on async kafka bindings for python see:
[aiokafka RTFM](https://aiokafka.readthedocs.io/en/stable/)
