#Problem 1 - Multiples of 3 or 5
n=1000
sum=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        sum=sum+i
print('Sum of all multiple of 3 or 5 below 1000 is',sum)

#Problem 6 -Sum Square Difference
sum1=0
sum2=0
for i in range(1,101):
    sum1=sum1+i
sum1=sum1**2
for i in range(1,101):
    sum2=sum2+i*i
print('The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is',sum1-sum2)

