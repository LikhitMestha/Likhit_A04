try:
    with open("sample.txt") as f:
        content = f.readlines()
        
        Line = 1
        for line in content:
            print(f"Line {Line}: {line.strip()}")
            Line += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")