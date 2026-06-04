#This is a program to find the highest and lowest numbers i.e. max and min in a list of numbers. 
#assume you are given a list of numbers as below:

#list of numbers


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(f"The list of numbers is: {student_scores}")

user_choice = input("Do you want to find the highest or lowest number in the list? Enter 'h' for highest and 'l' for lowest: ")

highest = 0
if user_choice == "h":
    for score in student_scores:
        if score > highest:
            highest = score
        else:
            continue
    print(f"The highest number in the list is: {highest}")
elif user_choice == "l":
    for score in student_scores:
        if score > highest:
            highest = score
        else:
            continue
    for score in student_scores:
        if score < highest:
            highest = score
        else:
            continue
    print(f"The lowest number in the list is: {highest}")