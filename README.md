# Maze Solver Using A* Algorithm

This project generates a random maze and solves it using the A* search algorithm, visually displaying the process with animations using Pygame.

## 📌 Libraries Used
- `random` → Used to shuffle moves and generate a random maze.
- `pygame` → Used for visualizing the maze and solving process.
- `heapq` → Used to implement a priority queue for A* search.

---

## 🚀 How the Project Works
### A. Maze Generation (Recursive Backtracking)
The maze is represented as a 2D grid where:
- `1` → Wall
- `0` → Open path

#### Steps:
1. Start with a grid full of walls.
2. The function `generate_maze(x, y)` creates paths by:
   - Marking the current cell as part of the path.
   - Randomly picking a direction (up, down, left, right).
   - Moving two steps in that direction if it leads to a wall.
   - Recursively repeating the process to create a fully connected maze.

### B. A* Search Algorithm (Finding the Shortest Path)
A* is a graph traversal algorithm that finds the shortest path using:
- **G-score**: Cost to reach the current cell.
- **H-score (heuristic)**: Estimated cost to the goal (Manhattan Distance).
- **F-score**: `F = G + H` (Lower values are prioritized).

#### Steps:
1. Start from the initial node and push it to a priority queue.
2. Expand the node with the lowest F-score.
3. Update G-score and F-score for its neighbors.
4. Track the best path using a `came_from` dictionary.
5. If the goal is reached, backtrack to reconstruct the path.
6. If no path exists, return failure.

### C. Visualization (Pygame)
The `draw_maze()` function updates the screen with:
- **Walls** → Black
- **Path** → White
- **Explored Nodes** → Yellow
- **Final Path** → Blue
- **Start & End Points** → Green & Red

Animation speed is controlled using `pygame.time.delay(13)`.

---

## 🔧 Code Execution Steps
1. Generate a random maze.
2. Set the start and end points.
3. Run A* search to find the shortest path.
4. Display the exploration process.
5. Show the final path.
6. Keep running until the user closes the window.

---

## ✨ Key Features & Optimizations
✅ **Adjustable Maze Size** → Change `WIDTH` and `HEIGHT`.
✅ **Smooth Animation** → Uses Pygame for real-time updates.
✅ **Optimized A* Search** → Uses a priority queue for efficiency.
✅ **Recursive Backtracking** → Ensures a solvable maze every time.

---

## 🔥 Possible Improvements
🚀 **Future Enhancements:**
- **Different Heuristics** → Try Euclidean distance or Dijkstra’s algorithm.
- **Maze Size Adjustments** → Add UI elements for grid size selection.
- **Speed Control** → Adjust animation speed dynamically.
- **Multiple Pathfinding Algorithms** → Compare BFS, DFS, A*, and Dijkstra.
- **User Input for Start & End Points** → Let users choose their own locations.

---

## ⚙️ Backend Logic & Mathematical Concepts
### A. Maze Generation - Recursive Backtracking
💡 **Concept Used:** Depth-First Search (DFS) + Randomization
- The maze is a grid-based graph where each cell is a node.
- Walls (`1`) and paths (`0`) define connections between nodes.
- Uses a **recursive DFS** approach:
  1. Mark current cell as visited.
  2. Pick an unvisited neighbor at random.
  3. Remove the wall between the current cell and the neighbor.
  4. Recursively call the function for the new neighbor.
  5. If no neighbors remain, backtrack.

✏️ **Mathematical Representation:**
- The graph is represented as an adjacency matrix where edges exist between neighboring `0`s (paths).
- Ensures a fully connected maze with a single unique path between any two points.

### B. Pathfinding Algorithm - A* Search
💡 **Concept Used:** Graph Search + Heuristics + Priority Queue
- A* chooses the best path based on cost estimation.
- Uses a **priority queue** (`heapq`) for efficiency.
- Calculates scores:
  - **G-score (g)** → Cost from start to current node.
  - **H-score (h)** → Estimated cost from current node to goal.
  - **F-score (f = g + h)** → Total estimated cost.

✏️ **Mathematical Representation:**
- Uses **Manhattan Distance Heuristic**:
  
  `h(x) = |x1 - x2| + |y1 - y2|`
  
- This heuristic works well in a grid-based environment where movement is restricted to 4 directions.

📌 **Efficiency:**
- Runs in `O(b^d)` (exponential in worst case), but priority queue optimizations keep it efficient.
- The heuristic ensures **optimality** (if `h` is admissible & consistent).

---

## 📚 What I’ve Learned from This Project
✅ **Algorithmic Thinking**
- Implemented recursive backtracking for maze generation.
- Understood A* search algorithm and heuristic efficiency.
- Explored priority queues for optimal pathfinding.

✅ **Data Structures in Action**
- Used a 2D list (matrix) to store the maze.
- Implemented sets (for visited nodes) and dictionaries (to track paths).
- Used a heap (priority queue) to optimize A*.

✅ **Mathematical Heuristics & Graph Search**
- Manhattan Distance for estimating shortest paths.
- Graph traversal techniques (DFS & A*) for different applications.

✅ **Pygame for Visualization**
- Learned how to draw grids and animate search algorithms.
- Used event handling (`QUIT` event) to keep the app interactive.

---

## 🛠 Installation & Running the Code
### Prerequisites:
- Python 3.x
- Pygame Library (`pip install pygame`)

### Run the Project:
```bash
python maze.py
```

---

## 🎯 Conclusion
This project provided hands-on experience with graph search algorithms, heuristics, recursion, and visualization using Pygame. It’s a great way to understand real-world AI search problems, and the knowledge gained here can be applied to **robotics, game development, and navigation systems**. 🚀🔥

