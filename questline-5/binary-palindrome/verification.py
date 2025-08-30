n1=15
n2=10
bin1=format(n1,'b')
bin2=format(n2,'b')

for i in range(1,len(bin1)//2+1):
    if bin1[i-1] != bin1[-i]:
        print(bin1,"is not a palindrome")
        bin1=0
        break
if bin1!=0:
  print(bin1,"is a palindrome")

for i in range(1,len(bin2)//2+1):
    if bin2[i-1] != bin2[-i]:
        print(bin2,"is not a palindrome")
        bin2=0
        break
if bin2!=0:
  print(bin2,"is a palindrome")
