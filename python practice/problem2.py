# program to fill lette
# r template given below with name and date
letter='''Dear <|Name|>,
       you are selected! 
       <|Date|>>'''

print(letter.replace("<|Name|>","Dhananjay").replace("<|Date|>","23 November 2024"))