from collections import Counter


def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


if __name__ == "__main__":
    scores = [8, 8, 8, 8, 9, 9, 9, 9, 9,
              4, 5, 1, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    modes = calculate_mode(scores)
    for mode in modes:
        print(mode)
