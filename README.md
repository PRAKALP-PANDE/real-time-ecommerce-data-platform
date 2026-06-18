# Real-Time E-commerce Lakehouse Platform
Architecture

                ┌─────────────┐
                │ Order Events│
                └──────┬──────┘
                       │
                ┌──────▼──────┐
                │   Kafka     │
                └──────┬──────┘
                       │
          ┌────────────▼────────────┐
          │ Spark Structured Stream │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Bronze Layer │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Silver Layer │
          └────────────┬────────────┘
                       │
          ┌────────────▼────────────┐
          │ Delta Lake Gold Layer   │
          └────────────┬────────────┘
                       │
             ┌─────────▼─────────┐
             │ Analytics Tables  │
             └─────────┬─────────┘
                       │
                ┌──────▼──────┐
                │ Dashboard   │
                └─────────────┘
