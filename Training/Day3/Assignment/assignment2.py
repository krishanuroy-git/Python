#Write a program to assign a grade based on the score:
#If score > 90: Grade A
#If score > 80: Grade B
#If score > 70: Grade C
#If score > 60: Grade D
#Else: Grade F
#Use nested if-else.

score = 59 # You can change this value to test different scores

if score > 90:
    grade = 'A'
else:
    if score > 80:
        grade = 'B'
    else:
        if score > 70:
            grade = 'C'
        else:
            if score > 60:
                grade = 'D'
            else:
                grade = 'F'
print(f"Score: {score}, Grade: {grade}")