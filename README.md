# News Distribution MQTT

## Overview

News Distribution MQTT is a small backend project that fetches news articles, normalizes the article data, and publishes each article to MQTT topics based on its category.

The main idea is to simulate a real-time news distribution system. Instead of every client calling the news API directly, the backend fetches the news once, processes it, and lets MQTT handle distributing the articles to subscribers.

For example, a science article can be published to:

```text
news/science
```

A sports article can be published to:

```text
news/sports
```

If an article belongs to multiple categories, it can be published to multiple topics.

---

## Basic Architecture

```text
News API
   ↓
FastAPI Background Fetch Loop
   ↓
Article Normalizer
   ↓
MQTT Topic Router
   ↓
MQTT Publisher
   ↓
Mosquitto Broker
   ↓
Subscribers
```

## Tech Stack

* Python
* FastAPI
* Pydantic
* Paho MQTT
* Mosquitto MQTT Broker
* News API
* TLS certificates
* Environment variables with `.env`

---

## How to Run Locally

### Dependencies

```powershell
pip install fastapi uvicorn paho-mqtt requests pydantic python-dotenv
```

If the project has a `requirements.txt` file later, use:

```powershell
pip install -r requirements.txt
```

## Database Dependencies

This project uses PostgreSQL to store normalized news articles before publishing them through MQTT.

Install the required Python database packages:

```powershell
python -m pip install sqlalchemy alembic "psycopg[binary]"

### Run the FastAPI app

```powershell
fastapi dev
```

---

## Example MQTT Topics

```text
news/science
news/technology
news/business
news/sports
news/health
news/general
```

A subscriber can listen to one category:

```text
news/science
```

Or listen to all news topics:

```text
news/#
```

---

## Project Goal

The goal of this project is to practice backend architecture, MQTT communication, topic-based message routing, and real-time data distribution.
