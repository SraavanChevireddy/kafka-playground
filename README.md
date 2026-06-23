# kafka-playground

> Spin up a complete Apache Kafka lab with **one command**, then produce and consume messages from both **Spring Boot** and **Python**. The fastest way to actually learn Kafka by doing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-KRaft-231F20.svg)](https://kafka.apache.org/)
[![Java](https://img.shields.io/badge/Java-21-orange.svg)](https://openjdk.org/projects/jdk/21/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

Most Kafka tutorials drown you in ZooKeeper config and half-working `docker-compose` files. This one boots a modern **KRaft-mode** broker plus a web UI in seconds, and gives you working producers/consumers in two languages so you can focus on the concepts.

## What you get

- **Kafka in KRaft mode** (no ZooKeeper) via `docker-compose`.
- **Kafka UI** at http://localhost:8088 to browse topics, partitions, and messages in your browser.
- A **Spring Boot** app that exposes a `/publish` endpoint and logs consumed messages.
- A **Python** producer and consumer using `kafka-python`.

## 1. Start the cluster

```bash
docker compose up -d
```

Wait a few seconds, then open the UI: http://localhost:8088

## 2a. Produce & consume with Python

```bash
cd consumer-python
pip install -r requirements.txt

# Terminal 1 — start consuming
python consumer.py

# Terminal 2 — produce a message
python producer.py "hello from python"
```

You'll see the message appear in Terminal 1.

## 2b. Produce & consume with Spring Boot

```bash
cd producer-spring
./mvnw spring-boot:run   # (generate the wrapper with: mvn wrapper:wrapper)

# In another terminal
curl -X POST "http://localhost:8080/publish?text=hello-from-spring"
```

The app's `@KafkaListener` logs the message it just published. Mix and match: produce from Python, consume in Spring, or vice versa — they share the `demo-events` topic.

## Architecture

```
                 ┌─────────────────┐
   Python  ───▶  │                 │  ───▶  Python consumer
                 │  Kafka (KRaft)  │
   Spring  ───▶  │  demo-events    │  ───▶  Spring @KafkaListener
                 └─────────────────┘
                         ▲
                  Kafka UI :8088
```

## Tear down

```bash
docker compose down -v
```

## License

[MIT](LICENSE) © Sraavan Chevireddy
