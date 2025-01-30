
# O(n) time complexity
s = input("Enter a string and get have it return it backwards: ")

print(s[::-1])



# another way
#  O(n)
rev = ""

for i in range(len(s) -1, -1, -1):
    rev += s[i]

print(rev)

