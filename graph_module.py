# graph_data.py
# Author: Bat An
# Undirected classmate graph for bfs_batan

GRAPHX = {
    "Adam":   ["Bob", "Bat An", "Ema"],
    "Bob":    ["Adam", "Dolly", "Ema"],
    "Ema":    ["Adam", "Bob", "Frank"],
    "Frank":  ["Ema", "George"],
    "George": ["Frank", "Dolly"],
    "Dolly":  ["Bob", "George"],
    "Bat An": ["Adam"]
}
