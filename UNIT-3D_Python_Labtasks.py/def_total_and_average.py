def total_and_average(subject_1_marks, subject_2_marks, subject_3_marks):
    total = subject_1_marks+subject_2_marks+subject_3_marks
    average = total/3
    return total, average

m1, m2, m3 = 50, 22, 60
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)
