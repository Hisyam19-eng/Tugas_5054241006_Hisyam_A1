grade = float(input("Enter desired grade => "))    
min_avg = float(input("minimum average required=>"))  
current_avg = float(input("current average in course"))
exam_percentage = float(input("Enter how much the final counts as a percentage of the course grade"))
exam_percentage /=100
final_score = (min_avg - current_avg*(1-exam_percentage))/exam_percentage

print(final_score)
