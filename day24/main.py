
# open a file
t_file = open('day24/text.txt')

# read contents of file
contents = t_file.read()

# print file content
print(contents)

# close file / free up space
t_file.close()

# using with will close the file after being read
with open('day24/text.txt') as file:
  contents = file.read()
  print(contents)

# using 'w' to write to the file
# will overwrite it
with open('day24/text.txt', 'w') as file:
  file.write('\nnewly overwritten text')


# using 'a' to write to the file
# will append the text to file
with open('day24/text.txt', 'a') as file:
  file.write('\nnewly added text with append')

# creating new file with open and 'w' mode
# will create new file if it doesn't exist
with open('day24/new_file.txt', 'w') as file:
  file.write('New file text woo')


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./day24/Input/Names/invited_names.txt') as file:
  for line in file.readlines():
    name = line.strip()
    
    with open('./day24/Input/Letters/starting_letter.txt') as letter:
      contents = letter.read().replace('[name]', name)
  
    with open(f'./day24/Output/ReadyToSend/{name}_letter.txt', 'w') as send:
      send.write(contents)