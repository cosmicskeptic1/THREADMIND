# THREADMIND

### Intelligent Wardrobe Decision Engine

THREADMIND is a Python-based wardrobe recommendation system that generates outfit combinations based on user preferences and clothing attributes.

## Features

* Generates outfit combinations automatically
* Considers color compatibility
* Considers clothing style
* Considers formality
* Considers occasion
* Considers season
* Tracks previously worn combinations
* Provides an explanation for why an outfit was selected
* Built with Python and Tkinter

## How It Works

THREADMIND stores wardrobe data in JSON format and evaluates possible combinations of:

* Tops
* Bottoms
* Shoes

Each combination receives a compatibility score based on multiple factors. The system then selects a suitable unworn combination.

## Project Structure

```text
THREADMIND/
│
├── main.py
├── ui.py
├── wardrobe.py
├── outfit_engine.py
├── scoring.py
├── history.py
├── wardrobe.json
├── history.json
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

## Technologies

* Python
* Tkinter
* JSON
* Object-Oriented Programming
* Rule-based scoring system

## Running the Project

Make sure Python is installed, then run:

bash
python main.py

## Project Concept

THREADMIND demonstrates how a rule-based decision engine can combine multiple attributes and preferences to produce a personalized recommendation.
