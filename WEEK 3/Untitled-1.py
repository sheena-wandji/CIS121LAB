#write code to determine how many letter are in a word

word = 'hello world'

count = 0

for letter in word:
    count+=1
    if letter !='':
        count += 1
print(count)


#write code to determine how many vowels are in a given word
#aeiou
#word1=hello world
#word2=appple and banana

word1 ='hello word'
count = 0

for letter in word:
    if letter =='a' or letter == 'e' or letter == 'i' or letter =='o' or letter == 'u':
     count+= 1
     print( f"the vowel in {word1} is {count}" )

word ='apple and banana' 
count = 0  

for letter in word:
    if letter =='a' or letter == 'e' or letter == 'i' or letter =='o' or letter == 'u':
     count+= 1
     print( f"the vowel in {word} is {count}" )

def vowel_counter(passed_word):
   count=0
   for letter in passed_word:
      if letter=="a":
         coun+= 1
      elif  letter == 'e' :
         count+= 1
      if letter == 'i' :
         count+= 1
      if letter =='o':
       count+= 1
      if  letter == 'u':
         count+= 1
         print(f"the vowel count in '{passed_word}' is {count}")

     
#write a function that takes an int adds, multiplies by 4, print the result
def my_fctn(number):
   number +=2
   number *=2
   print(number)
   return number

def add_ten(number):
   number+=10
   return number


#starting with the value 10 , add 2, then multiple it by 4. Take the result and add 2 to it , the  multiple by 4 again 

result1= my_fctn(10)

result2= my_fctn(result2)

#call the function my_fctn 100 times
def my_fctn(number):
   number+=100
   print(number)























    










