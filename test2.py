def group_into_nine(lst):
    grouped = [lst[i:i+9] for i in range(0, len(lst), 9)]
    return grouped

# Example usage:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = group_into_nine(original_list)
print(result)
