# Phase II — AI Masterclass (AI Educator)

This repository is my learning workspace for Phase II of the AI Masterclass, as I work toward becoming an AI Educator. It contains practice exercises, experiments, and small projects that help me build technical skills and explain what I learn.

## Purpose

This folder is for learning and practice. The files document my progress with Python, APIs, Machine learning, JavaScript, data handling, and simple web interfaces. They are learning exercises and may be revised as my understanding grows.

## Learning Goals

- Strengthen Python programming skills.
- Strengthen JavaScript programming skills.
- Understand how to request and use data from APIs.
- Work with JSON responses and save data to files.
- Practice handling user input and errors.
- Connect a simple web interface to a Python server.
- Build lessons to demonstrate and explain technical concepts as an AI Educator.

## Learning Activities

| Files | Practice area |
| --- | --- |
| `day1_api.py`, `day1_api_assignment.py`, `day1_api_assignment2.py` | Python API exercises and assignments |
| `day2_News.py`, `day2_weather.py` | Fetching news and weather data |
| `day3_exchangerate_news.py`, `day3_travel_info.py` | Combining API data in small command-line tools |
| `day4_fetch.html`, `day4_server.py` | A web interface with a local Python server |
| `day5_week1_project.py`, `Conversion_currency_tracker.py` | Currency conversion practice projects |
| `mombasa_weather.json` | Saved weather data used during practice |
| `main.py` | Introductory Python practice |
|`objectives.md` | Writing observable ojectives |

The day numbers reflect the organization of the exercises in this folder, rather than a complete course syllabus.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Natiri-Spencer/Phase-II.git
cd Phase-II
```

### 2. Create a virtual environment

With Python 3 installed, run:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install the shared dependencies

```bash
python -m pip install requests python-dotenv
```

### 4. Configure API keys where needed

Create a `.env` file in the project folder and add the keys required by the exercise you want to run:

```dotenv
OPENWEATHER_API_KEY=your_openweather_key
NEWSAPI_KEY=your_newsapi_key
RESTCOUNTRIES_API_KEY=your_restcountries_key
```

Keep actual keys private. The `.gitignore` excludes `.env` files, virtual environments, and Python cache files.

Some exercises use public exchange-rate requests and do not require a key in their current implementation. API-based exercises need an internet connection, and their behavior depends on the external service.

## Running an Exercise

Run individual scripts from the project folder. For example:

```bash
python day2_weather.py
```

For the currency conversion exercise:

```bash
python day5_week1_project.py
```

For the Day 4 web exercise:

```bash
python day4_server.py
```

Then open `http://localhost:8000` in your browser. The country lookup requires `RESTCOUNTRIES_API_KEY` in your `.env` file. Stop the server with `Ctrl+C`.

## Learning Approach

For each exercise, I aim to understand the code, run it, observe the results, and explain the main ideas in my own words. This repository will grow as I continue learning and practicing during the AI Masterclass.

## Learner

[Natiri Spencer](https://github.com/Natiri-Spencer)

AI Masterclass — AI Educator learning journey.
