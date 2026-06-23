#!/usr/bin/env python3
"""A minimal Kafka consumer that prints messages from the 'demo-events' topic.

Run the broker first:  docker compose up -d
Install deps:          pip install -r requirements.txt
Run:                   python consumer.py
"""
import json
import os
import signal
import sys

from kafka import KafkaConsumer

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "demo-events")


def main() -> None:
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="python-demo-consumer",
        value_deserializer=lambda b: json.loads(b.decode("utf-8")),
    )

    # Graceful shutdown on Ctrl-C / SIGTERM.
    def shutdown(*_):
        print("\nShutting down consumer...")
        consumer.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    print(f"Listening to '{TOPIC}' on {BOOTSTRAP} (Ctrl-C to stop)...")
    for message in consumer:
        print(f"[{message.partition}@{message.offset}] {message.value}")


if __name__ == "__main__":
    main()
