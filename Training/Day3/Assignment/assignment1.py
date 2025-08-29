#Write a Python program that manages a list of student scores. 
# Perform the following operations step-by-step:
#Create an empty list to store scores.
#Append the scores: 85, 90, 78, 92, 88
#Insert the score 80 at index 5
#Remove the score 92 from the list
#Sort the scores in ascending order
#Reverse the list
#Find and print the maximum and minimum score
#Check if 90 is in the list
#Print the total number of scores
#Slice and print the first three scores

scores = []  # Create an empty list to store scores
print("Initial empty scores list:", scores)

scores.extend([85, 90, 78, 92, 88])  # Append the scores
print("Scores after appending:", scores)

scores.insert(5, 80)  # Insert the score 80 at index 5
print("Scores after inserting 80 at index 5:", scores)

scores.remove(92)  # Remove the score 92 from the list
print("Scores after removing 92:", scores)

scores.sort() # Sort the scores in ascending order
print("Scores after sorting in ascending order:", scores)   

scores.reverse()  # Reverse the list
print("Scores after reversing the list:", scores)

max = max(scores)  # Find the maximum score
min = min(scores)  # Find the minimum score

print("Maximum score:", max)
print("Minimum score:", min)

present = 90 in scores  # Check if 90 is in the list
print("Is 90 in the list?", present)

total_scores = len(scores)  # Print the total number of scores  
print("Total number of scores:", total_scores)


#find the last element from the list
#replace the score with new score on the index 2
#create a new copied list also

last_items = scores[-1] # last item
print("Last item in the scores list:", last_items)

scores[2] = 95 # replace the value at index 2
print("Scores after replacing value at index 2 with 95:", scores)

copy_score = scores.copy() # copy the list
print("Copy of the scores list:", copy_score)

