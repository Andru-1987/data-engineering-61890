#!/bin/bash

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
cub kafka-ready -b localhost:9092 1 20

# Create the Kafka topic
echo "Creating topic '$KAFKA_TOPIC'..."
kafka-topics --create --topic $KAFKA_TOPIC --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List topics to verify creation
echo "Listing topics..."
kafka-topics --list --bootstrap-server localhost:9092
