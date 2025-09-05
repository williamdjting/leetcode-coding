def backtrack(path, choices, n, k, results):
    # Base case: sequence complete
    if len(path) == k:
        results.append(path[:])  # copy current sequence
        return

    # Explore choices
    for choice in choices:
        # Skip if already used
        if choice in path:
            continue

        # Make a choice
        path.append(choice)

        # Recurse with updated state
        backtrack(path, choices, n, k, results)

        # Undo choice (backtrack)
        path.pop()


def generate_sequences(n: int, k: int):
    results = []
    choices = list(range(1, n+1))
    backtrack([], choices, n, k, results)
    return results


print(generate_sequences(4, 2))
# Example output:
# [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], ...]
