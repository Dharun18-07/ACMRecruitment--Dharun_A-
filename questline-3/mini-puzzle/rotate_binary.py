#rotate_binary
str=input()
k=int(input())
k=k%len(str)
rotated=str[k:]+str[:k]
n=int(rotated, 2)
print(n)

