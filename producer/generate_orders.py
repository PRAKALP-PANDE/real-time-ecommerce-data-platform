from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime


def generate_orders(num_orders=10):

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    for _ in range(num_orders):

        order = {
            "order_id": random.randint(1000, 9999),
            "customer_id": random.randint(1, 100),
            "product_id": random.randint(1, 50),
            "quantity": random.randint(1, 5),
            "amount": round(random.uniform(100, 5000), 2),
            "timestamp": datetime.now().isoformat()
        }

        producer.send(
            "orders",
            key=str(order["customer_id"]).encode(),
            value=order
        )

        print("Sent:", order)

        time.sleep(2)

    producer.flush()
    producer.close()


if __name__ == "__main__":
    generate_orders()