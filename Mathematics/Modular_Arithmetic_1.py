'''
We say that two integers are congruent modulo m if a ≡ b mod m
Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m | a) then a ≡ 0 mod m

Calculate the following integers:

11 ≡ x mod 6
8146798528947 ≡ y mod 17

'''

# 11=x mod 6 so x=11 mod 6 
x= 11 % 6

y= 8146798528947 % 17

print(min(x,y))


