##Use find and string slicing to extract the portion of the string after the colon character 
## and then use the float function to convert the extracted string into a floating point number.
## result should be 0.8475

str = 'X-DSPAM-Confidence:0.8475'
colonpos = str.find(':')
num = (str[colonpos+1:])
num = num.lstrip()
num = float(num)
print (num)