def hello():
    a = list(map(int, input("Enter the values for a (comma separated): ").split(",")))
    n = list(map(int, input("Enter the values for n (comma separated): ").split(",")))
    print("a:", a)
    print("n:", n)

    if len(a) != len(n):
        print("Enter the numbers for both a and n equal")
        return

    result = []
    for i, j in zip(a, n):
        result.append(i + j)

    print("The sum of the values are:", result)
    break

hello()