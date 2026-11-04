# Lesson Design

# Lesson

# Making an API Call with requests Library

---

> **You sell shoes online through your website. Every day you receive calls from different customers scattered across the country, asking how they can pay you and which number or till they should use to make payments. How can you solve this problem? An API call to M-PESA Express (STK Push) solves this problem.**

---

## By the end of the lesson you will have:

- Made your first API call with Python and the `requests` library

---

## How an API Call Works

Every API call has the same basic structure:

---

### Step 1: You Send a Request

Your code sends an HTTP request to a URL. The URL is the address of the API. Like visiting a website, but instead of a browser making the request, your Python code does it.

### Step 2: The API Processes It

The server receives your request, checks if you are allowed to make it, runs whatever logic it needs to, and prepares a response.

### Step 3: You Receive a Response

The API sends back data, usually in JSON format. JSON is a structured way to send data that both humans and computers can read. You parse it and use what you need.

---

### Step 4: Your Program Uses the Data

Once the response arrives, your code can display it, save it to a file, perform calculations, or send it somewhere else.

**Example:**

```python
import requests

response = requests.get(
    "https://amerix.com/users/1"
)

data = response.json()

print(data["name"])
```

**Output:**

```text
Spencer Natiri
```

---

## Complete API Flow

```text
+------------------+
| Python Program   |
+------------------+
          |
          | HTTP Request
          v
+--------------------------------+
| API Endpoint (Safaricom Daraja)|
+--------------------------------+
          |
          | Process Request
          v
+------------------+
| Database/Service |
+------------------+
          |
          | Response Data
          v
+------------------+
| Python Program   |
+------------------+
```

---

## Installing the `requests` Library

Python can make HTTP requests using a library called `requests`. It is not included in Python's standard library, so you need to install it once using `pip`.

Open the terminal in VS Code and run:

```bash
pip install requests
```

---

## Your First API Call

We will use the **REST Countries API**. It is free, requires no sign-up, and returns information about countries around the world. It is perfect for learning because you do not need an API key.

Open VS Code and create a new file called `api.py`.

### Code

```python
import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

print("Status code:", response.status_code)
print("Data received:", response.json())
```

### Run the Program

Open the terminal and run:

```bash
python api.py
```

### Expected Output

```text
Status code: 200
Data received: [...]
```

The status code `200` means the request was successful. The API returns a large JSON response containing information about Kenya.

---
---
Today we used free public APIs that require no authentication. In upcoming lessons, we will connect to Safaricom Daraja APIs, where we must first obtain an access token before making requests such as STK Push payments.

---
---
## Todays exercise
Call free public API

You can use REST Countries or pick one of these free APIs that need no sign-up:

-`Open-Meteo (open-meteo.com)`: free weather data, no key needed
-`JSONPlaceholder (jsonplaceholder.typicode.com)`: fake user and post data for testing
-`CoinGecko (api.coingecko.com)`: crypto prices, no key on free tier

---