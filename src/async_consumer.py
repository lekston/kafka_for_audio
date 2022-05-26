import asyncio

from aiokafka import AIOKafkaConsumer

TOPIC_NAME = 'demo-events'
SERVER_DATA = 'localhost:9092'


async def receiver():
    """
    Run async client
    """
    consumer = AIOKafkaConsumer(TOPIC_NAME,
                                bootstrap_servers=SERVER_DATA)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"{msg.topic}:{msg.partition}:{msg.offset} key={msg.key}"
                  f" value={msg.value} timestamp_ms={msg.timestamp}")
    finally:
        await consumer.stop()


if __name__=='__main__':
   asyncio.run(receiver())
