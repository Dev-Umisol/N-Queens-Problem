# 📁 N-Queens Problem

> A Python solution to the N-Queens problem using Depth First Search, placing N queens on an N×N chessboard so no two queens can attack each other.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Learning](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

The N-Queens problem is a classic computer science puzzle, place N queens on an N×N chessboard so that no two queens share the same row, column, or diagonal. This solution applies the DFS algorithm from the previous project to a constraint satisfaction problem, using a stack to explore all possible queen placements and pruning invalid branches early via a safety check. Built to understand how DFS generalizes beyond graph traversal into backtracking and combinatorial search.

---

## 🧠 What I Learned

- **DFS for constraint satisfaction** — Applying the same LIFO stack approach from the DFS graph traversal project to a completely different problem domain, showing that DFS is a general search strategy — not just a graph tool
- **Backtracking via pruning** — Only adding a new state to the stack when `is_safe()` returns `True`, which eliminates entire invalid branches early rather than generating all combinations and filtering afterward
- **Diagonal attack detection** — Using `abs(len(state) - index) == abs(col - value)` to check if a new queen would be on the same diagonal as any existing queen, a compact formula that checks both up-left and up-right diagonals simultaneously
- **State as a list of column positions** — Representing the board as a list where each index is a row and each value is the column of the queen in that row, which implicitly guarantees no two queens share a row
- **Nested helper function** — Defining `is_safe()` inside `dfs_n_queens()` to keep the safety logic encapsulated and give it clean access to `state` without passing extra arguments
- **Growth of solutions** — Observing that the number of valid solutions grows dramatically with `n`: 1 solution for n=1, 2 for n=4, 10 for n=5, and 92 for n=8, illustrating combinatorial explosion

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core language |

---

## 💡 How It Works

Each state in the stack is a list of column positions for queens placed so far, one per row. At each step the algorithm tries placing a queen in every column of the next row, adds the state to the stack if it's safe, and eventually collects all states of length `n` as valid solutions.

```
n = 4 (4×4 board, 2 solutions)

Solution 1: [1, 3, 0, 2]     Solution 2: [2, 0, 3, 1]

. Q . .                       . . Q .
. . . Q                       Q . . .
Q . . .                       . . . Q
. . Q .                       . Q . .
```

**Example output:**
```python
dfs_n_queens(1)  # [[0]]
dfs_n_queens(4)  # [[1, 3, 0, 2], [2, 0, 3, 1]]
len(dfs_n_queens(5))  # 10
len(dfs_n_queens(8))  # 92
```

---

## 🚀 Future Improvements

- [ ] Visualize each solution as an ASCII chessboard with `Q` and `.` characters
- [ ] Add a solution counter that prints how many valid arrangements exist for each `n`
- [ ] Compare performance against a recursive backtracking version
- [ ] Optimize with symmetry reduction, mirror and rotation duplicates can cut the search space significantly

---

## 📂 Project Structure

```
n-queens/
│
├── NQueensAlgorithm.py    # dfs_n_queens function with example usage
└── README.md
```

---

*Part of my Python learning journey 🐍 — applying DFS to constraint satisfaction and combinatorial search*
