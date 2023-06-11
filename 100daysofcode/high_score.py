student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score= score
print(f"the highest score is {high_score}")       
