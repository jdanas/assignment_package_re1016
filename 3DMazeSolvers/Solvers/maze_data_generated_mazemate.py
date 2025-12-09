# Maze Data - Generated from MazeMate (Unity WebGL)
# Dimensions: 8 x 8

# Grid representation (0 = path/walkable, 1 = wall/obstacle)
maze_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Starting position (x, y)
start = (1, 1)

# End/Goal position (x, y)
end = (4, 5)

# Initial facing direction (N=North, S=South, E=East, W=West)
initial_direction = "S"

# Gem/Collectible positions (0 found)
gem_positions = []

# Heart/Health positions (2 found) - collect to defeat monsters
heart_positions = [(3, 3), (4, 3)]

# Monster/Enemy positions (1 found)
monster_positions = [(2, 3)]

# Monster types for reference
monster_types = {
    (2, 3): "Ghost"
}