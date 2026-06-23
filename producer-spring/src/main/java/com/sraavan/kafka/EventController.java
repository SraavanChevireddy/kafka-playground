package com.sraavan.kafka;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

/**
 * POST a message and it gets published to the 'demo-events' topic.
 *
 *   curl -X POST "http://localhost:8080/publish?text=hello"
 */
@RestController
public class EventController {

    public static final String TOPIC = "demo-events";

    private final KafkaTemplate<String, String> kafkaTemplate;

    public EventController(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @PostMapping("/publish")
    public Map<String, Object> publish(@RequestParam(defaultValue = "hello from spring") String text) {
        kafkaTemplate.send(TOPIC, text);
        return Map.of("published", text, "topic", TOPIC);
    }
}
