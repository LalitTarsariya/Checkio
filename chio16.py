data=[[1, 2, 1, 1],[1, 1, 4, 1],[1, 3, 1, 6],[1, 7, 2, 5]]
"""
cl=column length
rl=row lwngth
"""

direction = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if dx != 0 or dy != 0]

