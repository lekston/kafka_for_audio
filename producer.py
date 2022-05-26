from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(100):
    msg = f"demo message {i:2f}"
    print(f"sending {msg}")
    producer.send('demo-events', msg.encode('utf-8'))
    sleep(1)
