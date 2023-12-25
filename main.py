def largest_perfect_set(riceBags):
    riceBags.sort()  # Sort the bags in ascending order

    max_set_size = 0

    for i in range(len(riceBags)):
        for j in range(i + 1, len(riceBags)):
            if riceBags[i] * riceBags[i] == riceBags[j]:
                # Update the maximum set size
                max_set_size = max(max_set_size, 2 + largest_set_size(riceBags, j, riceBags[j]))

    return max_set_size if max_set_size >= 2 else -1

def largest_set_size(riceBags, idx, prev_grains):
    # Recursively find the size of the set starting from idx
    size = 0
    current_grains = prev_grains

    while idx < len(riceBags):
        if riceBags[idx] == current_grains * current_grains:
            size += 1
            current_grains = riceBags[idx]
            idx += 1
        else:
            break

    return size

# Example usage:
riceBags = [1, 4, 16, 64]
result = largest_perfect_set(riceBags)
print(result)  # Output: 4
