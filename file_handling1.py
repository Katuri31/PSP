#Write a python code ton read,count-words,lines and characters in a txt file
#"r" - Read - Default value. Opens a file for reading.

#"a" - Append - Opens a file for appending.

#"w" - Write - Opens a file for writing.

f= open("Text1.txt","r") #opens a file for reading
d= f.read()#the data from the txt file will be read
Number_of_characters=len(d)
Number_of_Words=len(d.split())
Number_of_lines=len(d.splitlines())
print("The number of characters in the given file are:",Number_of_characters)
print("The number of words in the given file are:",Number_of_Words)
print("The number of lines in the given file are:",Number_of_lines)

                    


