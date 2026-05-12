import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # Special case: height = 1 → all '*'
    if y == 1:
        print('*' * x)
        return

    # Normal case (height > 1)
    top    = '/' + '*' * (x - 2) + '\\' if x > 1 else '*'
    middle = '*' + ' ' * (x - 2) + '*' if x > 1 else '*'
    bottom = '\\' + '*' * (x - 2) + '/' if x > 1 else '*'

    print(top)
    for _ in range(y - 2):
        print(middle)
    print(bottom)


# ==================== MAIN PART ====================
if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rush(x, y)
        except:
            print("Invalid size", file=sys.stderr)
    else:
        print("Usage: python rush.py <width> <height>", file=sys.stderr)