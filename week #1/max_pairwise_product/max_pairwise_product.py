def max_pairwise_product(numbers):
    n = len(numbers)
    a = 0
    b = 0
    for first in range(n):
        if numbers[first] > a:
            a = numbers[first]

    index_max_1 = numbers.index(a)

    for second in range(n):
        if numbers[second] > b and second != index_max_1:
            b = numbers[second]

    max_product = a * b

    return max_product

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
