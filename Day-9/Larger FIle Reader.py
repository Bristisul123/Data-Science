def fake():
    for i in range(10):
        yield f"Line {i}"

for item in fake():
    print(item)
