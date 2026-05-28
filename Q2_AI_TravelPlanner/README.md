# AI Based Travel Planner

## Overview

This project implements an AI Based Travel Planner using Python.

The system reuses existing knowledge bases related to:
- Tourist Places
- Food Recommendations
- Budget Assessment
- Personalized Travel Planning

The application recommends travel destinations based on user interests and budget.

---

## Features

- Tourist Place Recommendation
- Food Recommendation
- Budget Estimation
- Personalized Tour Plan
- Knowledge Base Reuse
- Rule-Based Decision System

---

## AI Concepts Used

### Knowledge Representation

Travel data, food data, and budget information are stored as reusable knowledge bases.

---

### Rule-Based Recommendation System

The system recommends destinations based on:
- User interests
- Budget
- Number of travel days

---

### Personalized Planning

Customized travel plans are generated for each user.

---

## Knowledge Bases Used

### Tourist Places Knowledge Base

Contains:
- Cities
- Tourist attractions
- Place categories

---

### Food Recommendation Knowledge Base

Contains:
- Famous foods for each destination

---

### Budget Knowledge Base

Contains:
- Low budget
- Medium budget
- High budget estimates

---

## Programming Language

- Python 3

---

## Project Structure

```text
AI_Travel_Planner/
│
├── knowledge_base.py
├── recommendation.py
├── budget.py
├── planner.py
├── main.py
├── testcases.txt
└── README.md
```

---

## Requirements

Install Python 3 before running the project.

Official Website:
https://www.python.org

---

## How to Run

Open terminal inside the project folder and run:

```bash
python main.py
```

---

## Sample Input

```text
Interest: Beach
Budget: Medium
Days: 3
```

---

## Sample Output

```text
Recommended City: Goa

Tourist Places:
Day 1 -> Baga Beach
Day 2 -> Calangute Beach
Day 3 -> Fort Aguada

Recommended Food:
- Seafood
- Fish Curry
- Prawn Fry

Estimated Cost: 45000
```

---

## Test Cases

### Test Case 1

Input:
- Interest: Beach
- Budget: Medium
- Days: 3

Expected:
- Goa recommended
- Tour plan generated
- Food recommendations shown

---

### Test Case 2

Input:
- Interest: Historical
- Budget: Low
- Days: 2

Expected:
- Hyderabad or Delhi recommended

---

### Test Case 3

Input:
- Interest: Hill Station
- Budget: High
- Days: 4

Expected:
- Manali recommended

---

### Test Case 4

Input:
- Interest: Desert
- Budget: Medium
- Days: 2

Expected:
- No matching destinations found

---

### Test Case 5

Input:
- Interest: Beach
- Budget: High
- Days: 5

Expected:
- Travel plan generated
- Budget estimation displayed

---

## Conclusion

This project demonstrates the use of Artificial Intelligence concepts in travel recommendation systems.

The planner reuses existing knowledge bases to provide:
- destination recommendations
- food suggestions
- budget assessment
- personalized travel plans

The project successfully combines knowledge representation and rule-based AI techniques.

---
