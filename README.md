# The-Eight-Puzzle
This project implements an **A* search algorithm** to solve the classic **8-puzzle problem**, efficiently finding the shortest path from any given initial state to the goal state. It supports **dynamic heuristic selection**, including **Manhattan Distance** and **Misplaced Tiles**, to optimize search performance.  

## **Features**  
✅ Supports **custom initial and goal states**  
✅ Implements **A* search algorithm** for optimal pathfinding  
✅ Includes **Manhattan Distance** and **Misplaced Tiles** heuristics  
✅ Uses **priority queue (`heapq`)** for efficient node expansion  


## **How It Works**  
1. The user inputs an **initial puzzle state** or can select from an option of puzzles.  
2. The solver applies **A* search**, evaluating possible moves using the selected heuristic.  
3. The algorithm finds the optimal sequence of moves to reach the **goal state**.  
4. The solution path is displayed, along with the depth, max nodes expanded, and the max queue size.

## **Tech Stack**  
- **Language:** Python  
- **Algorithms:** A* Search, Heuristic Search  
- **Data Structures:** Priority Queue, State-Space Representation  

## **Getting Started**  
Clone the repository and run the solver:  
```bash
git clone https://github.com/roshinira123/The-Eight-Puzzle.git  
cd The-Eight-Puzzle  
python solver.py
```

## Note:
This project was created for the CS170 class (Introduction to Artificial Intelligence) at UC Riverside taught by Eamonn Keogh in Winter 2025. Please see the attached Project write-up for more background about the project and more information.
