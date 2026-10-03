"""
AI PRACTICAL HELPER

Quick examples:

DFS:
    dfs(G, 'A')

BFS:
    bfs(G, 'A')

A*:
    astar(G, 'A', 'G')

AO*:
    ao_star(graph, heuristic, 'A')

Minimax:
    minimax(tree, 'A', True)

Water Jug:
    water_jug(4, 3, 2)

N Queens:
    queens(8)
"""

import networkx as nx
from collections import deque
from constraint import Problem


def dfs(G, start):
    """
    DFS - Depth First Search

    Example:
        dfs(G, 'A')

    Returns:
        DFS traversal order.
    """
    return list(nx.dfs_preorder_nodes(G, start))


def bfs(G, start):
    """
    BFS - Breadth First Search

    Example:
        bfs(G, 'A')

    Returns:
        BFS traversal order.
    """
    return list(nx.bfs_tree(G, start).nodes())


def astar(G, start, goal, heuristic):
    """
    A* Search

    Formula:
        f(n) = g(n) + h(n)

    Example:
        h = {'A':6, 'B':4, 'C':3, 'G':0}
        astar(G, 'A', 'G', h)
    """

    def h(a, b):
        return heuristic[a]

    return nx.astar_path(G, start, goal, heuristic=h, weight="weight")


def ao_star(graph, h, node):
    """
    AO* Search

    Rule:
        AND = ADD
        OR  = MIN

    Example:
        ao_star(graph, h, 'A')
    """

    if not graph[node]:
        return h[node]

    costs = []

    for option in graph[node]:
        cost = 0

        for child, edge in option:
            cost += edge + ao_star(graph, h, child)

        costs.append(cost)

    h[node] = min(costs)
    return h[node]


def minimax(tree, node, maximizing=True):
    """
    Minimax

    MAX = maximum
    MIN = minimum

    Example:
        minimax(tree, 'A', True)
    """

    if isinstance(tree[node], int):
        return tree[node]

    values = [
        minimax(tree, child, not maximizing)
        for child in tree[node]
    ]

    return max(values) if maximizing else min(values)


def water_jug(jug1, jug2, target):
    """
    Water Jug Problem

    Example:
        water_jug(4, 3, 2)

    Finds a solution using BFS.
    """

    q = deque([(0, 0, [])])
    visited = set()

    while q:
        a, b, path = q.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            return path

        states = [
            (jug1, b),
            (a, jug2),
            (0, b),
            (a, 0)
        ]

        x = min(a, jug2 - b)
        states.append((a-x, b+x))

        x = min(b, jug1 - a)
        states.append((a+x, b-x))

        for state in states:
            q.append((state[0], state[1], path))


def queens(n):
    """
    N-Queens Problem

    Example:
        queens(8)

    Finds one solution for N queens.
    """

    board = []

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if all(
                col != board[i] and
                abs(col - board[i]) != row - i
                for i in range(row)
            ):
                board.append(col)

                if solve(row + 1):
                    return True

                board.pop()

        return False

    solve(0)

    for row in range(n):
        print(
            " ".join(
                "Q" if board[row] == col else "."
                for col in range(n)
            )
        )


def ai_help():
    """
    Shows the AI practical cheat sheet.
    """

    print("""
========================================
        AI PRACTICAL CHEAT SHEET
========================================

DFS
    dfs(G, 'A')

BFS
    bfs(G, 'A')

A*
    astar(G, 'A', 'G', h)
    Formula: f = g + h

AO*
    ao_star(graph, h, 'A')
    AND = ADD
    OR = MIN

MINIMAX
    minimax(tree, 'A', True)
    MAX = max
    MIN = min

WATER JUG
    water_jug(4, 3, 2)

N QUEENS
    queens(8)

========================================
""")
