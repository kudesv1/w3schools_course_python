print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(0))

print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# +	   Addition	        x + y	
# -	   Subtraction	    x - y	
# *	   Multiplication	x * y	
# /	   Division	        x / y	
# %    Modulus	        x % y	
# **   Exponentiation	x ** y	
# //   Floor division	x // y	

#   =	x = 5  	x = 5	
#   +=	x += 3	x = x + 3	
#   -=	x -= 3	x = x - 3	
#   *=	x *= 3	x = x * 3	
#   /=	x /= 3	x = x / 3	
#   %=	x %= 3	x = x % 3	
#   //=	x //= 3	x = x // 3	
#   **=	x **= 3	x = x ** 3	
#   &=	x &= 3	x = x & 3	
#   |=	x |= 3	x = x | 3	
#   ^=	x ^= 3	x = x ^ 3	
#   >>=	x >>= 3	x = x >> 3	
#   <<=	x <<= 3	x = x << 3	
#   :=	print(x := 3)	x = 3
#                       print(x)
	
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#   ==	Equal	x == y	
#   !=	Not equal	x != y	
#   >	Greater than	x > y	
#   <	Less than	x < y	
#   >=	Greater than or equal to	x >= y	
#   <=	Less than or equal to	x <= y	

#   and 	Returns True if both statements are true                    x < 5 and  x < 10	
#   or	    Returns True if one of the statements is true               x < 5 or x < 4	
#   not 	Reverse the result, returns False if the result is true     not(x < 5 and x < 10)	

x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#   is      Returns True if both variables are the same object          x is y	
#   is not  Returns True if both variables are not the same object	    x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#   in      Returns True if a sequence with the specified value is present in the object	    x in y	
#   not in	Returns True if a sequence with the specified value is not present in the object	x not in y

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#   & 	    AND 	                Sets each bit to 1 if both bits are 1   	                                                                x & y	
#   |	    OR  	                Sets each bit to 1 if one of two bits is 1  	                                                            x | y	
#   ^	    XOR 	                Sets each bit to 1 if only one of two bits is 1 	                                                        x ^ y	
#   ~	    NOT 	                Inverts all the bits	                                                                                    ~x	
#   <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
#   >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

#   ()  Parentheses	
#   **	Exponentiation	
#   +x  -x  ~x  Unary plus, unary minus, and bitwise NOT	
#   *  /  //  % Multiplication, division, floor division, and modulus	
#   +  -	Addition and subtraction	
#   <<  >>	Bitwise left and right shifts	
#   &   Bitwise AND	
#   ^	Bitwise XOR	
#   |	Bitwise OR	
#   ==  !=  >  >=  <  <=  is  is not  in  not in  Comparisons, identity, and membership operators	
#   not  Logical NOT	
#   and	 AND	
#   or	 OR	

a = 15
b = 4
print(a % b)
print(a // b)
print(a ** b)
a += 10