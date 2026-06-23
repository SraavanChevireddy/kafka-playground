package com.sraavan.kafka;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

/**
 * Logs every message that lands on the 'demo-events' topic.
 */
@Component
public class EventConsumer {

    private static final Logger log = LoggerFactory.getLogger(EventConsumer.class);

    @KafkaListener(topics = EventController.TOPIC, groupId = "spring-demo-consumer")
    public void onMessage(String message) {
        log.info("Received from {}: {}", EventController.TOPIC, message);
    }
}
