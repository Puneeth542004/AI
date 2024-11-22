from itertools import permutations

def is_valid_solution(mapping, words, result):
    def word_to_number(word):
        return int(''.join(str(mapping[char]) for char in word))

    total = sum(word_to_number(word) for word in words)
    return total == word_to_number(result)

def solve_cryptarithmetic(words, result):
    unique_chars = set(''.join(words) + result)
    if len(unique_chars) > 10:
        print("No solution exists")
        return

    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if all(mapping[word[0]] != 0 for word in words + [result]):  # Ensure no leading zeros
            if is_valid_solution(mapping, words, result):
                for char in mapping:
                    print(f"{char} = {mapping[char]}")
                return

    print("No solution exists")

# Example usage:
words = ["SEND", "MORE"]
result = "MONEY"
solve_cryptarithmetic(words, result)
