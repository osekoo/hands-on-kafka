# Hands-on Kafka

This session will guide you through setting up and running a Kafka project using **sbt** and Python. You will also perform exercises to explore key Kafka concepts.



## Setup

### 1. Create a New Project
Use the **Giter8 template** to bootstrap your Kafka project:
```bash
sbt new osekoo/kafka-py.g8
```

### 2. Install `sbt` (if not already installed)
Follow the appropriate guide for your operating system:
- **Windows:** [Install sbt on Windows](https://www.scala-sbt.org/1.x/docs/Installing-sbt-on-Windows.html)
- **macOS:** Use Homebrew:
  ```bash
  brew install sbt
  ```
- **Linux:** Use your package manager:
  - Ubuntu/Debian:
    ```bash
    echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
    curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x99E82A75642AC823" | sudo apt-key add
    sudo apt update
    sudo apt install sbt
    ```



## Running the Project

### 1. Start the Kafka Broker
From the project folder, run:
```bash
./kafka-start
```

### 2. Install Python Dependencies
Install required Python packages:
```bash
python -m pip install -r requirements.txt
```

### 3. Run the Consumer
Run the consumer to start listening for messages:
```bash
python consumer.py
```

### 4. Run the Producer
Send messages to the Kafka topic using:
```bash
python producer.py
```

### 5. Analyze Consumer Output
Observe the messages processed by the consumer in the terminal.

### 6. Explore the Kafka Dashboard
Open your browser and navigate to:
```
http://localhost:9094
```
Use the Kafka dashboard to inspect:
- Topics
- Offsets
- Partitions
- Message content

## Exercises

### 1. Change the Consumer Code

#### Task:
Modify the consumer code to specify a **consumer group**. Update the `consumer.py` file with a `group_id` in the KafkaConsumer configuration:
```python
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BROKER,
    value_deserializer=data_deserializer,
    auto_offset_reset='earliest'
     # Add group_id
)
```

#### Steps:
1. Save the updated code.
2. Re-run the consumer:
   ```bash
   python consumer.py
   ```

#### Questions:
- What happens to the consumer output when re-run?
- If multiple consumers are started with the same group ID, how are messages distributed?

#### Expected Observations:
- Kafka ensures messages are distributed among consumers in the same group. Each partition will be processed by only one consumer in the group.



### 2. Change the Producer Code

#### Task:
Update the producer to publish numbers with a **key** where the key is `n % m` (where `m` is the number of partitions). Modify `producer.py` as follows:
```python
def send(producer, size, partitions):
    for i in range(size):
        key = str(i % partitions).encode('utf-8')  # Create key
        message = {'message': i}
        print(f'Sending: {message} with key: {key}')
        producer.send(TOPIC_NAME,
                      value=message
                      # specify the key
                      )  # Send with key
        time.sleep(1)

    producer.flush()
```

#### Steps:
1. Define the number of partitions (`m`) based on your topic configuration.
2. Save the updated code.
3. Re-run the producer:
   ```bash
   python producer.py
   ```

#### Questions:
- How do messages appear in the Kafka dashboard?
- Are messages evenly distributed across partitions?

#### Expected Observations:
- Messages are partitioned based on the hash of the key.
- For a given key (e.g., `n % m`), all messages will go to the same partition.
- Check the Kafka dashboard to verify message repartitioning.

