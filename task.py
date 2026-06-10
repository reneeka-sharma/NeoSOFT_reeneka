def flatten_typed(nested):
    buckets = {
        "integers": set(),
        "floats": set(),
        "strings": set(),
        "booleans": set()
    }

    def flatten(item):
        # Recursively traverse nested lists
        if isinstance(item, list):
            for element in item:
                flatten(element)

        elif isinstance(item, bool):
            buckets["booleans"].add(item)

        elif isinstance(item, int):
            buckets["integers"].add(item)

        elif isinstance(item, float):
            buckets["floats"].add(item)

        elif isinstance(item, str):
            buckets["strings"].add(item)

        else:
            raise TypeError(f"Unsupported type: {type(item).__name__}")

    flatten(nested)

    result = {}
    for key, values in buckets.items():
        if values:
            result[key] = sorted(values)

    return result


# Test 1
print(flatten_typed([1, [2, [3, 2]], 1, [4]]))

# Test 2
print(flatten_typed([3, ["apple", 1.5], ["apple", [2, 1.5, "banana"]]]))

# Test 3
print(flatten_typed([True, 1, False, [True, 0, [2, False]]]))

# Test 4
try:
    print(flatten_typed([1, [2, {"key": "val"}]]))
except TypeError as e:
    print("Error:", e)
