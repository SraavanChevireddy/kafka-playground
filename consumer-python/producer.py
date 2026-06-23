#!/usr/bin/env python3
"""A minimal Kafka producer that sends demo JSON events.

Install deps:  pip install -r requirements.txt
Run:           python producer.py "hello kafka"
"""
import json
import os
import sys
import time

from kafka import KafkaProducer

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "demo-events")


def main() -> None:
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    text = " ".join(sys.argv[1:]) or "hello from python"
    event = {"text": text, "ts": time.time()}

    future = producer.send(TOPIC, event)
    record = future.get(timeout=10)
    producer.flush()
    print(f"Sent to {record.topic}[{record.partition}]@{record.offset}: {event}")


if __name__ == "__main__":
    main()
