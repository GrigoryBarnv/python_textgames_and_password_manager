with open("story.txt", "r") as f:
    story = f.read()
    
    
words = set() # set because it allows no duplicates 
start_of_word = -1

target_start ="<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] # slice operator 
        words.add(word)
        start_of_word = -1
        
answers = {"<name>": "Tim"}    # ask user to give a calue for each of those woprds 
# to add to dictionary use (answers["key"] = "value")

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer
#now we have all those words entered by user in a dictionary


#now replace the dictionary from above with this words 
for word in words:
   story = story.replace(word, answers[word])
    
print(story)