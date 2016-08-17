def fib_mod(n, m):
	a = 0
	b = 1
	cached = [a, b]

	for curr in range(1, n):
		c = b
		b = (b + a) % m
		a = c

		if a == 0 and b == 1:
			cached.pop()
			break
		else:
			cached.append(b)

	offset = n % len(cached)
	return cached[offset]

def main():
	n, m = map(int, input().split())
	print(fib_mod(n, m))


if __name__ == "__main__":
	main()
