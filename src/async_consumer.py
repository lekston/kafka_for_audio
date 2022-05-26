import asyncio
import numpy as np

from aiokafka import AIOKafkaConsumer
from src.connection_config import TOPIC_NAME, SERVER_DATA


async def receiver():
    """
    Run async client
    """
    consumer = AIOKafkaConsumer(TOPIC_NAME,
                                bootstrap_servers=SERVER_DATA)
    await consumer.start()
    try:
        async for msg in consumer:
            handle_message(msg)
    finally:
        await consumer.stop()


def handle_message(msg):
    meta = f"{msg.topic}:{msg.partition}:{msg.offset} key={msg.key}"
    stamp = f"timestamp_ms={msg.timestamp}"
    if msg.key == b'audio':
        audio = np.frombuffer(msg.value, dtype='float32')
        audio_details = [audio.shape, audio.dtype]
        val = f"value='audio: {audio_details}"
    elif msg.key == b'text':
        val = f"value={msg.value}"
    else:
        print(f"Unknown msg key {msg.key} skipping value\n" + meta + ' ' + stamp)
    print(' '.join((meta, val, stamp)))

if __name__=='__main__':
   asyncio.run(receiver())
