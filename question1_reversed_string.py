#direct reversing
s = "string"
print(s[::-1])


#using length and slicing
s = "string"
reversed_s = s[len(s)::-1] 
print (reversed_s)


#using function call
s = "string"
def reversing_function(x):
  return x[::-1]

print(reversing_function(s))
 

#using join and reversed
s = "string"
s_reversed=''.join(reversed(s))
print(s_reversed)


#using while loop and length
s = "string"
reversed_s = ""
coef_s = len(s)
while coef_s > 0:
    reversed_s += s[coef_s - 1]
    coef_s -= 1
print(reversed_s)