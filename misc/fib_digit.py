def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b % 10, (a + b) % 10
    return a

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()