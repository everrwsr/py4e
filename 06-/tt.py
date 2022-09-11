str = 'X-DSPAM-Confidence:0.8475'
a=str.find(":")
print(a)
new_str = str[a+1:]
print(new_str)