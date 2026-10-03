"""
AI Practical Master Library
===========================

Experiments included:

1. Simple Chatbot
2. Hangman
3. DFS
4. BFS
5. A*
6. AO*
7. Minimax with Alpha-Beta Pruning
8. Water Jug Problem
9. N-Queens / 8-Queens

Quick start:

    from ai_practical import *

Then:

    help()

For detailed help:

    help(chatbot)
    help(hangman)
    help(dfs)
    help(bfs)
    help(astar)
    help(ao_star)
    help(minimax)
    help(water_jug)
    help(queens)
"""

import builtins
import heapq
import math
import random
from collections import deque
from itertools import count
from numbers import Number


# ============================================================
# MASTER HELP
# ============================================================

MASTER_HELP = """
============================================================
                AI PRACTICAL MASTER HELP
============================================================

IMPORT:

    from ai_practical import *


1. SIMPLE CHATBOT
-----------------
    chatbot()

Custom responses:

    responses = {
        "hello": "Hello!",
        "name": "I am an AI bot."
    }

    chatbot(responses)


2. HANGMAN
----------
    hangman()

Use your own words:

    hangman(["python", "ai", "jupyter"])

Change chances:

    hangman(["python", "computer"], max_wrong=8)


3. DFS - DEPTH FIRST SEARCH
---------------------------
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"]
    }

    dfs(graph, "A")


4. BFS - BREADTH FIRST SEARCH
-----------------------------
    bfs(graph, "A")


5. A* SEARCH
------------
Weighted graph:

    graph = {
        "A": [("B", 1), ("C", 3)],
        "B": [("D", 2)],
        "C": [("E", 1)],
        "D": [("G", 3)],
        "E": [("G", 2)],
        "G": []
    }

Heuristic:

    h = {
        "A": 6,
        "B": 4,
        "C": 3,
        "D": 3,
        "E": 2,
        "G": 0
    }

    astar(graph, "A", "G", h)

Formula:

    f(n) = g(n) + h(n)


6. AO* SEARCH
-------------
AND-OR graph:

    graph = {
        "A": [
            [("B", 2), ("C", 1)],
            [("D", 4)]
        ],
        "B": [],
        "C": [],
        "D": []
    }

Heuristic:

    h = {
        "A": 5,
        "B": 2,
        "C": 1,
        "D": 3
    }

    cost, solution = ao_star(graph, h, "A")

Rule:

    AND = ADD
    OR  = MIN


7. MINIMAX + ALPHA-BETA PRUNING
-------------------------------
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": 3,
        "E": 5,
        "F": 2,
        "G": 9
    }

    minimax(tree, "A", True)

Get best move too:

    minimax(tree, "A", True, return_move=True)

Rule:

    MAX = maximum
    MIN = minimum

Alpha-Beta:

    alpha = best MAX value
    beta  = best MIN value


8. WATER JUG
------------
Classic 4L + 3L -> 2L:

    water_jug(4, 3, 2)

Other problems work too:

    water_jug(5, 3, 4)
    water_jug(8, 5, 6)

Returns the sequence of states and actions.


9. N-QUEENS / 8-QUEENS
----------------------
8 Queens:

    queens(8)

4 Queens:

    queens(4)

10 Queens:

    queens(10)

Get all solutions:

    queens(8, all_solutions=True)

Basic rule:

    No two queens in the same column.
    No two queens on the same diagonal.


============================================================
DETAILED HELP
============================================================

    help(chatbot)
    help(hangman)
    help(dfs)
    help(bfs)
    help(astar)
    help(ao_star)
    help(minimax)
    help(water_jug)
    help(queens)

============================================================
"""


def ai_help():
    """
    Displays the AI practical master cheat sheet.

    Example:
        ai_help()
    """
    print(MASTER_HELP)


# This custom help() allows:
#
#     help()
#
# to show YOUR practical cheat sheet.
#
# But:
#
#     help(dfs)
#
# still uses Python's real help system.
def help(item=None):
    """
    Custom help system for the AI Practical library.

    Examples:
        help()
        help(dfs)
        help(ao_star)
        help(minimax)

    Calling help() with no argument displays the full
    AI practical cheat sheet.
    """
    if item is None:
        print(MASTER_HELP)
    else:
        builtins.help(item)


# ============================================================
# 1. SIMPLE CHATBOT
# ============================================================

def chatbot(responses=None, exit_words=None):
    """
   def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        x = input("You: ").lower()

        if x == "bye":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in x or "hi" in x:
            print("Chatbot: Hello!")
        elif "name" in x:
            print("Chatbot: I am a Python chatbot.")
        elif "how are you" in x:
            print("Chatbot: I am fine!")
        else:
            print("Chatbot: I don't understand.")

chatbot()
    """

    if responses is None:
        responses = {
            "hello": "Hello! How are you?",
            "hi": "Hi! Nice to meet you.",
            "name": "I am a simple Python chatbot.",
            "how are you": "I am doing great!",
            "ai": "AI means Artificial Intelligence.",
            "python": "Python is a popular programming language.",
            "college": "Good luck with your practical!",
            "thank": "You're welcome!"
        }

    if exit_words is None:
        exit_words = {"bye", "exit", "quit"}

    print("CHATBOT")
    print("Type 'bye' to exit.")

    while True:

        message = input("You: ").strip().lower()

        if message in exit_words:
            print("Bot: Goodbye!")
            break

        answer = None

        for keyword, response in responses.items():

            if keyword.lower() in message:

                if isinstance(response, (list, tuple)):
                    answer = random.choice(response)
                else:
                    answer = response

                break

        if answer is None:
            answer = "Sorry, I don't understand that."

        print("Bot:", answer)


# ============================================================
# 2. HANGMAN
# ============================================================

def hangman(words=None, max_wrong=6):
    """
   import random

word = random.choice(["python", "computer", "science"])
guessed = ""
chance = 6

while chance > 0:

    for letter in word:
        print(letter if letter in guessed else "_", end=" ")

    print()

    if all(letter in guessed for letter in word):
        print("You WIN!")
        break

    x = input("Enter a letter: ").lower()

    if x in word:
        guessed += x
    else:
        chance -= 1
        print("Wrong! Chances left:", chance)

else:
    print("You LOST! Word:", word)
    """

    if words is None:
        words = [
            "python",
            "computer",
            "science",
            "algorithm",
            "college",
            "jupyter",
            "artificial"
        ]

    if not words:
        raise ValueError("The word list cannot be empty.")

    if max_wrong <= 0:
        raise ValueError("max_wrong must be greater than 0.")

    word = random.choice(words).strip().lower()

    if not word:
        raise ValueError("Selected word is empty.")

    guessed = set()
    wrong = 0

    print("HANGMAN")

    while wrong < max_wrong:

        print("\nWord:", end=" ")

        for char in word:

            if not char.isalpha():
                print(char, end=" ")

            elif char in guessed:
                print(char, end=" ")

            else:
                print("_", end=" ")

        print()
        print("Wrong guesses:", wrong, "/", max_wrong)

        required = {c for c in word if c.isalpha()}

        if required.issubset(guessed):
            print("You WIN!")
            return word

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter only.")
            continue

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct!")

        else:
            wrong += 1
            print("Wrong!")

    print("\nYou LOST!")
    print("The word was:", word)

    return word


# ============================================================
# GRAPH HELPERS
# ============================================================

def _neighbors(graph, node):
    """
    Internal helper for DFS/BFS.

    Supports:
        - normal dictionary graphs
        - NetworkX graphs
        - weighted adjacency lists
    """

    # NetworkX-like graph
    if hasattr(graph, "neighbors"):
        return list(graph.neighbors(node))

    # Normal dictionary graph
    values = graph.get(node, [])

    # Dictionary adjacency:
    #
    # {'A': {'B': 1, 'C': 2}}
    #
    if isinstance(values, dict):
        return list(values.keys())

    neighbors = []

    for item in values:

        # Weighted edge:
        # ('B', 4)
        if (
            isinstance(item, (tuple, list))
            and len(item) == 2
            and isinstance(item[1], Number)
        ):
            neighbors.append(item[0])

        else:
            neighbors.append(item)

    return neighbors


def _weighted_neighbors(graph, node):
    """
    Internal helper for A*.

    Accepts:
        {'A': [('B', 1), ('C', 3)]}

    or:

        {'A': {'B': 1, 'C': 3}}

    or a NetworkX weighted graph.
    """

    # NetworkX graph
    if hasattr(graph, "neighbors"):

        for neighbor in graph.neighbors(node):

            data = graph.get_edge_data(node, neighbor)

            weight = 1

            if isinstance(data, dict):

                # Normal Graph
                if "weight" in data:
                    weight = data.get("weight", 1)

                # MultiGraph / MultiDiGraph
                elif data and all(
                    isinstance(value, dict)
                    for value in data.values()
                ):
                    weight = min(
                        value.get("weight", 1)
                        for value in data.values()
                    )

            yield neighbor, weight

        return

    values = graph.get(node, [])

    # Dictionary form:
    #
    # {'B': 1, 'C': 3}
    if isinstance(values, dict):

        for neighbor, weight in values.items():
            yield neighbor, weight

        return

    # List form
    #
    # [('B', 1), ('C', 3)]
    for item in values:

        if (
            isinstance(item, (tuple, list))
            and len(item) == 2
            and isinstance(item[1], Number)
        ):
            yield item[0], item[1]

        else:
            # Unweighted edge defaults to 1
            yield item, 1


# ============================================================
# 3. DFS
# ============================================================

def dfs(graph, start, goal=None):
    """
def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    if node not in visited:

        print(node, end=" ")
        visited.add(node)

        for x in graph[node]:
            dfs(graph, x, visited)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

dfs(graph, "A")
    """

    visited = set()
    order = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        if goal is not None and node == goal:
            break

        neighbors = list(_neighbors(graph, node))

        # Reverse so normal left-to-right order is preserved
        stack.extend(reversed(neighbors))

    return order


# ============================================================
# 4. BFS
# ============================================================

def bfs(graph, start, goal=None):
    """
   from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        for x in graph[node]:
            if x not in visited:
                queue.append(x)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

bfs(graph, "A")
    """

    visited = {start}
    order = []
    queue = deque([start])

    while queue:

        node = queue.popleft()
        order.append(node)

        if goal is not None and node == goal:
            break

        for neighbor in _neighbors(graph, node):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return order


# ============================================================
# 5. A*
# ============================================================

def astar(graph, start, goal, heuristic=None):
    """
   import heapq

def astar(graph, start, goal, h):

    queue = [(h[start], 0, start, [start])]
    best = {start: 0}

    while queue:

        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        for next, cost in graph[node]:

            new_g = g + cost

            if new_g < best.get(next, float("inf")):

                best[next] = new_g
                new_f = new_g + h[next]

                heapq.heappush(
                    queue,
                    (new_f, new_g, next, path + [next])
                )

    return None


graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("D", 2), ("E", 4)],
    "C": [("E", 1)],
    "D": [("G", 3)],
    "E": [("G", 2)],
    "G": []
}

h = {
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 3,
    "E": 2,
    "G": 0
}

print(astar(graph, "A", "G", h))
    """

    if heuristic is None:
        heuristic = {}

    def h(node):
        if callable(heuristic):
            return heuristic(node, goal)

        return heuristic.get(node, 0)

    pq = []
    counter = count()

    start_h = h(start)

    heapq.heappush(
        pq,
        (start_h, 0, next(counter), start, [start])
    )

    best_cost = {start: 0}

    while pq:

        f, g, _, node, path = heapq.heappop(pq)

        if g != best_cost.get(node):
            continue

        if node == goal:
            return path, g

        for neighbor, edge_cost in _weighted_neighbors(graph, node):

            if edge_cost < 0:
                raise ValueError(
                    "A* requires non-negative edge costs."
                )

            new_g = g + edge_cost

            if new_g < best_cost.get(neighbor, math.inf):

                best_cost[neighbor] = new_g

                new_f = new_g + h(neighbor)

                heapq.heappush(
                    pq,
                    (
                        new_f,
                        new_g,
                        next(counter),
                        neighbor,
                        path + [neighbor]
                    )
                )

    raise ValueError("No path exists between start and goal.")


# ============================================================
# 6. AO*
# ============================================================

def ao_star(graph, heuristic, start):
    """
   def ao_star(graph, h, node):

    if not graph[node]:
        return h[node]

    best = float("inf")

    for option in graph[node]:

        cost = 0

        for child, edge in option:
            cost += edge + ao_star(graph, h, child)

        best = min(best, cost)

    h[node] = best
    return best


graph = {
    "A": [
        [("B", 2), ("C", 1)],   # B AND C
        [("D", 4)]              # OR D
    ],
    "B": [],
    "C": [],
    "D": []
}

h = {
    "A": 5,
    "B": 2,
    "C": 1,
    "D": 3
}

print("Cost:", ao_star(graph, h, "A"))
    """

    memo = {}
    selected = {}
    visiting = set()

    def solve(node):

        if node in memo:
            return memo[node]

        if node in visiting:
            raise ValueError(
                "AO* graph contains a cycle. "
                "Use an acyclic AND-OR graph."
            )

        # Terminal node
        if node not in graph or not graph[node]:

            cost = heuristic.get(node, 0)
            memo[node] = cost

            return cost

        visiting.add(node)

        best_cost = math.inf
        best_option = None

        # OR:
        # choose the cheapest option
        for option in graph[node]:

            total = 0

            # AND:
            # add every child
            for child, edge_cost in option:

                if edge_cost < 0:
                    raise ValueError(
                        "AO* requires non-negative edge costs."
                    )

                total += edge_cost + solve(child)

            if total < best_cost:

                best_cost = total
                best_option = option

        visiting.remove(node)

        memo[node] = best_cost
        selected[node] = best_option

        return best_cost

    cost = solve(start)

    return cost, selected


# ============================================================
# 7. MINIMAX + ALPHA-BETA PRUNING
# ============================================================

def minimax(tree, node, maximizing=True, return_move=False):
    """
 def minimax(tree, node, maximizing, alpha=float("-inf"), beta=float("inf")):

    if isinstance(tree[node], (int, float)):
        return tree[node]

    if maximizing:

        best = float("-inf")

        for child in tree[node]:

            best = max(
                best,
                minimax(tree, child, False, alpha, beta)
            )

            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:

        best = float("inf")

        for child in tree[node]:

            best = min(
                best,
                minimax(tree, child, True, alpha, beta)
            )

            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}

print("Best value:", minimax(tree, "A", True))
    """

    def search(current, max_turn, alpha, beta):

        if current not in tree:

            if isinstance(current, Number):
                return current, None

            raise ValueError(
                f"Node {current!r} is not in the tree."
            )

        value = tree[current]

        # Leaf
        if isinstance(value, Number):
            return value, None

        children = list(value)

        if not children:
            raise ValueError(
                f"Node {current!r} has no children and "
                f"is not a numeric leaf."
            )

        best_child = None

        if max_turn:

            best_value = -math.inf

            for child in children:

                child_value, _ = search(
                    child,
                    False,
                    alpha,
                    beta
                )

                if child_value > best_value:

                    best_value = child_value
                    best_child = child

                alpha = max(alpha, best_value)

                # Alpha-Beta Pruning
                if alpha >= beta:
                    break

        else:

            best_value = math.inf

            for child in children:

                child_value, _ = search(
                    child,
                    True,
                    alpha,
                    beta
                )

                if child_value < best_value:

                    best_value = child_value
                    best_child = child

                beta = min(beta, best_value)

                # Alpha-Beta Pruning
                if alpha >= beta:
                    break

        return best_value, best_child

    value, move = search(
        node,
        maximizing,
        -math.inf,
        math.inf
    )

    if return_move:
        return value, move

    return value


# Convenient alias
minimax_alpha_beta = minimax


# ============================================================
# 8. WATER JUG
# ============================================================

def water_jug(capacity1, capacity2, target):
    """
 from collections import deque
from math import gcd

def water_jug(a, b, target):

    queue = deque([(0, 0)])
    visited = set()

    while queue:

        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        print((x, y))

        if x == target or y == target:
            print("Goal reached!")
            return

        states = [
            (a, y),                              # Fill A
            (x, b),                              # Fill B
            (0, y),                              # Empty A
            (x, 0),                              # Empty B
            (x - min(x, b-y), y + min(x, b-y)),  # A -> B
            (x + min(y, a-x), y - min(y, a-x))   # B -> A
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("No solution")


water_jug(4, 3, 2)
    """

    if capacity1 <= 0 or capacity2 <= 0:
        raise ValueError(
            "Jug capacities must be positive."
        )

    if target < 0:
        raise ValueError(
            "Target cannot be negative."
        )

    if target > max(capacity1, capacity2):
        raise ValueError(
            "Target is larger than both jug capacities."
        )

    # Mathematical possibility check
    if target % math.gcd(capacity1, capacity2) != 0:
        raise ValueError(
            "Target cannot be measured with these jug sizes."
        )

    start = (0, 0)

    # state -> (previous_state, action)
    parent = {
        start: (None, "Start")
    }

    queue = deque([start])

    goal = None

    while queue:

        a, b = queue.popleft()

        if a == target or b == target:

            goal = (a, b)
            break

        states = []

        # Fill jug 1
        states.append(
            ("Fill Jug 1", (capacity1, b))
        )

        # Fill jug 2
        states.append(
            ("Fill Jug 2", (a, capacity2))
        )

        # Empty jug 1
        states.append(
            ("Empty Jug 1", (0, b))
        )

        # Empty jug 2
        states.append(
            ("Empty Jug 2", (a, 0))
        )

        # Pour Jug 1 -> Jug 2
        amount = min(a, capacity2 - b)

        states.append(
            (
                "Pour Jug 1 -> Jug 2",
                (a - amount, b + amount)
            )
        )

        # Pour Jug 2 -> Jug 1
        amount = min(b, capacity1 - a)

        states.append(
            (
                "Pour Jug 2 -> Jug 1",
                (a + amount, b - amount)
            )
        )

        for action, state in states:

            if state not in parent:

                parent[state] = ((a, b), action)

                queue.append(state)

    if goal is None:
        raise ValueError(
            "No solution exists."
        )

    # Reconstruct path
    path = []
    current = goal

    while current is not None:

        previous, action = parent[current]

        path.append(
            (action, current)
        )

        current = previous

    path.reverse()

    print("\nWATER JUG SOLUTION")

    for action, state in path:
        print(f"{action:25} -> {state}")

    return path


# ============================================================
# 9. N-QUEENS / 8-QUEENS
# ============================================================

def print_board(solution):
    """
    Print an N-Queens solution as a chessboard.

    Parameters
    ----------
    solution : list
        A list where solution[row] gives the column
        containing the queen.

    Example
    -------
        solution = queens(8)
        print_board(solution)
    """

    n = len(solution)

    for row in range(n):

        line = []

        for col in range(n):

            if solution[row] == col:
                line.append("Q")

            else:
                line.append(".")

        print(" ".join(line))


def queens(n=8, all_solutions=False, show=True):
    """
def queens(n):

    board = [-1] * n

    def safe(row, col):

        for r in range(row):

            if board[r] == col:
                return False

            if abs(board[r] - col) == abs(r - row):
                return False

        return True


    def solve(row):

        if row == n:
            return True

        for col in range(n):

            if safe(row, col):

                board[row] = col

                if solve(row + 1):
                    return True

                board[row] = -1

        return False


    solve(0)

    for row in range(n):

        for col in range(n):
            print("Q" if board[row] == col else ".", end=" ")

        print()


queens(8)
    """

    if n <= 0:
        raise ValueError(
            "n must be greater than 0."
        )

    board = [-1] * n

    columns = set()

    diagonal1 = set()
    diagonal2 = set()

    solutions = []

    def solve(row):

        if row == n:

            solutions.append(board.copy())

            # Stop immediately if only one solution is needed
            return not all_solutions

        for col in range(n):

            # Same column
            if col in columns:
                continue

            # Main diagonal
            if row - col in diagonal1:
                continue

            # Other diagonal
            if row + col in diagonal2:
                continue

            # Place queen
            board[row] = col

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            stop = solve(row + 1)

            # Backtrack
            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

            board[row] = -1

            if stop and not all_solutions:
                return True

        return False

    solve(0)

    if not solutions:
        print(f"No solution exists for {n}-Queens.")
        return [] if all_solutions else None

    if show:

        if all_solutions:
            print(
                f"\nFound {len(solutions)} solution(s)."
            )

        else:
            print(f"\n{n}-QUEENS SOLUTION")

        print_board(solutions[0])

    if all_solutions:
        return solutions

    return solutions[0]


# ============================================================
# ALIASES / PUBLIC FUNCTIONS
# ============================================================

n_queens = queens


# ============================================================
# EXPORT LIST
# ============================================================

__all__ = [
    "help",
    "ai_help",
    "chatbot",
    "hangman",
    "dfs",
    "bfs",
    "astar",
    "ao_star",
    "minimax",
    "minimax_alpha_beta",
    "water_jug",
    "queens",
    "n_queens",
    "print_board"
]
