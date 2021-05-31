# my gradebook example

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# New grade for computer science just came in and it is 100
gradebook.append(["computer science", 100])

# New grade for visual arts just came in and it's 93
gradebook.append(["visual arts", 93])

gradebook[-1][-1] = 93 + 5

# Switch the poetry class to pass/fail
grades.remove(85)
grades.append("Pass")
print(grades)
print(gradebook)

full_gradebook = [[last_semester_gradebook], [gradebook]]