#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

Starting from inner, you do that inner operation once per n
The while operation also checks once for the condition
a = 0 is one

Those are three constants, which we drop, so I think it's O(n) is correct


b)
O(n)

Starting from the inner
j *= 2
sum += 1
Those are each 1, even with the multiple, it isn't doing anything to n
The while loop just checks the condition once
The j=1 is one
sum = 0 is one
for i in range(n) does the operations once per n, so n^2


c)
O(n)

The recursive function returns once per n, so I believe this one is also O(n)


## Exercise II

For this, we'd drop the egg at the middle story of the building
If the egg DOESN'T break at that height, we go half way from the middle to the top floor and drop

If the egg DOES break at that height, we go half way from the middle to the bottom floor and drop

We keep doing this, cutting the number of floors to check in half until we divide the floors up so there's only one possible answer.

This is O(log(n)) since with each pass, the number of possibilities(n) is cut in half
