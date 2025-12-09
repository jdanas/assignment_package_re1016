"""
Source code modified from:
How to Solve a Maze using BFS in Python by Timur Bakibayev:
https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1
"""

from PIL import Image, ImageDraw
import maze_data_generated_mazemate as maze_data

images = []
zoom = 20
borders = 6

def solve_bfs(a, start, end):
    """
    Solves the maze 'a' from 'start' to 'end' using BFS.
    Returns the path as a list of coordinates.
    """
    m = []
    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    
    i, j = start
    m[i][j] = 1

    def make_step(k):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i > 0 and m[i - 1][j] == 0 and a[i - 1][j] == 0:
                        m[i - 1][j] = k + 1
                    if j > 0 and m[i][j - 1] == 0 and a[i][j - 1] == 0:
                        m[i][j - 1] = k + 1
                    if i < len(m) - 1 and m[i + 1][j] == 0 and a[i + 1][j] == 0:
                        m[i + 1][j] = k + 1
                    if j < len(m[i]) - 1 and m[i][j + 1] == 0 and a[i][j + 1] == 0:
                        m[i][j + 1] = k + 1

    def draw_matrix(the_path=[]):
        im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        for i in range(len(a)):
            for j in range(len(a[i])):
                color = (255, 255, 255)
                r = 0
                if a[i][j] == 1:
                    color = (0, 0, 0)
                if i == start[0] and j == start[1]:
                    color = (0, 255, 0)
                    r = borders
                if i == end[0] and j == end[1]:
                    color = (0, 255, 0)
                    r = borders
                draw.rectangle((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1), fill=color)
                if m[i][j] > 0:
                    r = borders
                    draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                                 fill=(255, 0, 0))
        for u in range(len(the_path) - 1):
            y = the_path[u][0] * zoom + int(zoom / 2)
            x = the_path[u][1] * zoom + int(zoom / 2)
            y1 = the_path[u + 1][0] * zoom + int(zoom / 2)
            x1 = the_path[u + 1][1] * zoom + int(zoom / 2)
            draw.line((x, y, x1, y1), fill=(255, 0, 0), width=5)
        draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0, 255, 0), width=2)
        images.append(im)

    k = 0
    # BFS Expansion
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)
        draw_matrix()
        
        # Safety break if unreachable
        if k > len(a) * len(a[0]): 
            print("Target unreachable from Start.")
            return []

    # Backtracking to find path
    i, j = end
    k = m[i][j]
    the_path = [(i, j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            the_path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            the_path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            the_path.append((i, j))
            k -= 1
        draw_matrix(the_path)

    for _ in range(10): # Hold final frame
        draw_matrix(the_path)
        
    return the_path

# --- Main Execution ---

if __name__ == "__main__":
    # 1. Setup Data
    maze_grid = maze_data.maze_grid
    start_pos = maze_data.start
    end_pos = maze_data.end
    heart_positions = maze_data.heart_positions

    print(f"Solving Maze from {start_pos} to {end_pos}...")

    # 2. Run Solver (Direct Path)
    path = solve_bfs(maze_grid, start_pos, end_pos)
    print("Path found:", path)

    # 3. Save Animation
    if images:
        images[0].save('maze_sols/default_bfs_sol.gif', save_all=True, append_images=images[1:], optimize=False, duration=50, loop=0)
        print("Animation saved to 'maze_sols/default_bfs_sol.gif'")

    # --- STUDENT CHALLENGE: OPTIONAL GOALS ---
    """
    CHALLENGE: 
    Can you modify the code to visit a 'Heart' before reaching the Goal?
    Hint: You might need to use the solver twice!
    1. Solve from Start -> Heart
    2. Solve from Heart -> Goal
    3. Combine the two paths (be careful not to duplicate the Heart position!)
    """
    print("\n--- Challenge Info ---")
    for idx, h_pos in enumerate(heart_positions):
        print(f"Heart {idx}: located at {h_pos}")

    # Example structure for student implementation:
    # 
    # if len(heart_positions) > 0:
    #     first_heart = heart_positions[0]
    #     print(f"Attempting to visit Heart at {first_heart} first...")
    #     
    #     # Step 1: Start -> Heart
    #     # Note: We clear images if we want a fresh animation, or keep appending to 'images' to show the full journey
    #     # images = [] 
    #     path_to_heart = solve_bfs(maze_grid, start_pos, first_heart)
    #     
    #     # Step 2: Heart -> End
    #     path_to_end = solve_bfs(maze_grid, first_heart, end_pos)
    #     
    #     # Step 3: Combine
    #     full_path = path_to_heart + path_to_end[1:] # Skip the first element of second path
    #     print("Full Path via Heart:", full_path)
