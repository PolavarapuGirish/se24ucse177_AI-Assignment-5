# AI Search Algorithms Assignment

## Overview

This project implements the following Artificial Intelligence search algorithms using Python:

- Minimax Search
- Alpha-Beta Pruning
- Heuristic Alpha-Beta Search
- Monte-Carlo Tree Search (MCTS)

The algorithms are implemented using the Tic-Tac-Toe game environment.

---

## Algorithms Implemented

### Minimax Search

Minimax is a recursive decision-making algorithm used in two-player games.  
It assumes one player tries to maximize the score while the opponent tries to minimize it.

---

### Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax by avoiding unnecessary exploration of branches that cannot affect the final result.

---

### Heuristic Alpha-Beta Search

This version uses:
- Depth-limited search
- Heuristic evaluation function

This helps improve performance for larger search spaces.

---

### Monte-Carlo Tree Search (MCTS)

MCTS uses:
1. Selection
2. Expansion
3. Simulation
4. Backpropagation

Random simulations are used to determine the best move.

---

## Programming Language

- Python 3

---

## Project Structure

```text
Q1_AI_SEARCH_ALGORITHMS/
│
├── game.py
├── minimax.py
├── alphabeta.py
├── heuristic_alphabeta.py
├── mcts.py
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

## Sample Output

```text
Initial Board
[' ', ' ', ' ']
[' ', ' ', ' ']
[' ', ' ', ' ']

Minimax Move: 0
Alpha Beta Move: 0
Heuristic Alpha Beta Move: 0
MCTS Move: 4
```

---

## Test Cases

### Test Case 1

Board:

```text
X X _
O O _
_ _ _
```

Expected:
AI should choose winning or blocking move.

---

### Test Case 2

Board:

```text
X O X
O X _
_ _ O
```

Expected:
AI should choose diagonal winning move.

---

### Test Case 3

Compare:
Minimax vs Alpha-Beta

Expected:
Alpha-Beta should explore fewer nodes.

---

### Test Case 4

Depth Limited Heuristic Search

Input:
Depth = 2

Expected:
Move should be generated faster using heuristic evaluation.

---

### Test Case 5

Monte-Carlo Tree Search

Input:
Simulations = 1000

Expected:
Better and more stable move selection after more simulations.

---

## Conclusion

This project demonstrates the implementation and comparison of multiple AI game search algorithms.  
The algorithms were tested using Tic-Tac-Toe to verify correctness and performance.

- Minimax guarantees optimal moves.
- Alpha-Beta improves efficiency.
- Heuristic search reduces computation time.
- MCTS uses simulation-based decision making.

---
