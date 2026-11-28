# word = str(input("enter a word:"))
s = "SAND"
result = ""
for ch in s:
    if 65 <= ord(ch) <= 90:
        result = result + chr(ord(ch) + 32)
    else: 
        result = result + ch
print(result) 

