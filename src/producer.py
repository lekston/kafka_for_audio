#! /usr/bin/env python3

from kafka import KafkaProducer
from time import sleep

from src.connection_config import TOPIC_NAME, SERVER_DATA
from src.audio.sample_generator import generate_chirp


# TODO support sending spectrograms

def produce_and_send():
    producer = KafkaProducer(bootstrap_servers=SERVER_DATA)
    for i in range(100):
        msg = f"demo message {i:2f}"
        msg = msg.encode('utf-8')
        if i % 2 == 0:
            audio = generate_chirp()
            print(f"sending audio {audio.shape} {audio.dtype}")
            data_key=b'audio'
            producer.send(TOPIC_NAME, audio.tobytes(), key=data_key)
        else:
            print(f"sending {msg}")
            data_key=b'text'
            producer.send(TOPIC_NAME, msg, key=data_key)
        sleep(0.8)


if __name__=='__main__':
    produce_and_send()
