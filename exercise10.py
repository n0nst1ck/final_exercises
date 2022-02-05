# Exercise 10
import re
# Get the text and split it to characters.
name=input("Insert the file name of the ascii text file:")
f=open(name)
text=list(f.read())
# Transform each character to 7 digit long binary number.
binary=[]
for c in range(len(text)):
    binary.append(bin(ord(text[c])).replace("0b",""))
    while(len(binary[c])<7):
        binary[c]="0"+binary[c]
# Keep the first and last two digits of each number.
for i in range(len(binary)):
    word=list(binary[i])
    binary[i]=word[0]+word[1]+word[len(word)-2]+word[len(word)-1]
# Combine all binary numbers to a string.
seq=""
for i in range(len(binary)):
    seq=seq+binary[i]
# Split into 16 digit long numbers.
seq=re.findall('.{1,16}', seq)
# Throw away the last number if it has less than 16 digits.
if(len(seq[-1])<16):
    seq.pop(-1)
# Count
count_even=0; count_three=0; count_five=0; count_seven=0
for i in range(len(seq)):
    if(int(seq[i])%2==0):
        count_even+=1
    if(int(seq[i])%3==0):
        count_three+=1
    if(int(seq[i])%5==0):
        count_five+=1
    if(int(seq[i])%7==0):
        count_seven+=1
print("Percent of even numbers: ", (count_even/len(seq))*100, "%")
print("Percent of numbers that are divided exactly by three: ",
(count_three/len(seq))*100, "%")
print("Percent of numbers that are divided exactly by five: ",
(count_five/len(seq))*100, "%")
print("Percent of numbers that are divided exactly by seven: ",
(count_seven/len(seq))*100, "%")
f.close()
