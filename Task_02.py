con1 = input("Enter text to write to the file: ")

with open("output.txt", 'w') as f:
    f.write('\n'+con1)
print("Data successfully  written to output.txt.")

con2 = input("Enter additonal text to append: ")

with open("output.txt", 'a') as f:
    f.write('\n'+con2)
print("Data successfully appended.")

with open("output.txt", 'r') as f:
    content = f.read()
print(f'''Final content of output.txt:{content}''')