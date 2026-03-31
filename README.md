# 📁 DFS N-Queens Solver

> A Python function that solves the classic N-Queens puzzle by finding all valid board arrangements where no two queens attack each other using a stack-based DFS approach.

---

## 📌 About

This project implements a solver for the N-Queens Problem: placing n chess queens on an n×n chessboard so that no two queens threaten each other. Unlike a traditional 2D array approach, this solution uses a memory-efficient 1D list to represent the board and a stack-based Depth-First Search (DFS) to traverse the state space. It was built to master backtracking logic, coordinate-based collision detection, and lexicographical result ordering.

---

## 🧠 What I Learned

- **Stack-based DFS for state-space trees** — Utilizing a manual stack with `pop()` and `append()` to explore potential queen placements. This mimics the behavior of recursion while providing a clear view of how the search "dives" deep into one branch before backtracking to the next.
- **Memory-efficient 1D board representation** — Representing the board as a list of integers where the index is the row and the value is the column. This avoids the overhead of managing an n×n matrix.
- **Mathematical collision detection** — Implementing an `is_safe` function that detects diagonal threats using the absolute difference formula `∣row1​−row2​∣=∣col1​−col2​∣`, significantly simplifying the "no-attack" logic.
- **Lexicographical sorting of nested lists** — Understanding that Python's `sorted()` function compares lists element-by-element, ensuring the final solutions are returned in the specific order required by standard algorithmic tests.
- **State mutation vs. Concatenation** — Using `current_state + [queen]` during the push to the stack to create localized copies of the board state, ensuring that one branch of the search does not accidentally pollute the data of another.

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

##💡 How It Works

The algorithm starts with an empty board and tries to place a queen in the first available row. For every column in that row, it checks if the position is "safe" from previously placed queens. If safe, it pushes the new state to the stack and moves to the next row. If no columns are safe, it "backtracks" by popping the last state and trying the next column.
```
n = 4 — target length: 4

Start: []
Row 0: [0], [1], [2], [3]
  From [0]:
    Row 1: [0, 2], [0, 3] (0,1 is blocked)
      From [0, 2]:
        Row 2: (All blocked!) ❌ Backtrack...
      From [0, 3]:
        Row 2: [0, 3, 1]
          Row 3: (All blocked!) ❌ Backtrack...
... continues until [1, 3, 0, 2] ✅
```

**Example output:**
```
dfs_n_queens(4)  # [[1, 3, 0, 2], [2, 0, 3, 1]]
dfs_n_queens(1)  # [[0]]
dfs_n_queens(3)  # []
```

---

##🚀 Future Improvements

- [ ] Implement a bitmasking approach to further optimize the diagonal collision checks.
- [ ] Add a visualization module to print the list output as an ASCII chessboard (e.g., [1, 3, 0, 2] → . Q . .).
- [ ] Compare performance between the current Stack-based DFS and a recursive implementation for large n.
- [ ] Add a "First-Solution-Only" mode to terminate the search as soon as one valid arrangement is found.

---


## 📂 Project Structure
```
n-queens-solver/
│
├── DepthFirstSearchAlgorithm.py     # dfs_n_queens function with is_safe helper
└── README.md
```
Part of my Python learning journey 🐍 — exploring DFS, coordinate math, and classic backtracking problems
