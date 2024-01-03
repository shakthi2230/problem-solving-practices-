n=153
print("True" if sum(int(digit) ** len(str(n)) for digit in str(n)) == n else "False")
