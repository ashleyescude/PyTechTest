import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # Create the lines
    top    = 'o' + '-' * (x - 2) + 'o' if x > 1 else 'o'
    middle = '|' + ' ' * (x - 2) + '|' if x > 1 else '|'
    bottom = 'o' + '-' * (x - 2) + 'o' if x > 1 else 'o'

    # Print the square
    print(top)
    for _ in range(y - 2):
        print(middle)
    if y > 1:
        print(bottom)


# ==================== MAIN PART (sys.argv usage) ====================
if __name__ == "__main__":
    if len(sys.argv) == 3:           # We expect exactly 3 things: script + x + y
        try:
            x = int(sys.argv[1])     # Convert first argument to number
            y = int(sys.argv[2])     # Convert second argument to number
            rush(x, y)
        except:
            print("Invalid size", file=sys.stderr)
    else:
        print("Usage: python rush.py <width> <height>", file=sys.stderr)