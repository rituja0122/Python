def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def lower_triangular(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end=' ')
        for k in range(2 * i + 1):
            print('*', end=' ')
        print()

def main():
    n = int(input("Enter the number of rows: "))
    pattern_type = input("Enter pattern type (upper/lower/pyramid): ").strip().lower()

    if pattern_type == 'upper':
        upper_triangular(n)
    elif pattern_type == 'lower':
        lower_triangular(n)
    elif pattern_type == 'pyramid':
        pyramid(n)
    else:
        print("Invalid pattern type. Please enter 'upper', 'lower', or 'pyramid'.")

if __name__ == "__main__":
    main()
