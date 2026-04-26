A = input()
result = ""
for ch in A :
    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()
print(result)
