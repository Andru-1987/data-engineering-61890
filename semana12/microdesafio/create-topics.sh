#!/bin/bash

set -e
# Function to check if the Kafka broker is reachable
check_broker() {
  echo "Checking Kafka broker availability on localhost:9092..."
  cub kafka-ready -b localhost:9092 1 20
  if [ $? -ne 0 ]; then
    echo "Kafka broker not ready. Exiting."
    exit 1
  else
    echo "Kafka broker is ready."
  fi
}

# Create a Kafka topic with partitions and replication factor
create_topic() {
  if [ -z "$KAFKA_TOPIC" ]; then
    echo "Error: KAFKA_TOPIC is not set."
    exit 1
  fi

  echo "Creating topic '$KAFKA_TOPIC' with 1 partition and replication-factor 1..."
  kafka-topics --create --topic "$KAFKA_TOPIC" --bootstrap-server localhost:9092 \
               --partitions 1 --replication-factor 1

  if [ $? -ne 0 ]; then
    echo "Failed to create topic '$KAFKA_TOPIC'. Exiting."
    exit 1
  else
    echo "Topic '$KAFKA_TOPIC' created successfully."
  fi
}


# Check if the Kafka broker is ready
check_broker

# Create the topic
create_topic

# List topics to verify creation
echo "Listing available topics..."
kafka-topics --list --bootstrap-server localhost:9092
