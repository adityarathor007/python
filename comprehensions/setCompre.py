# { expression for item in iterable if condition }


# we have list (that contains duplicate) and want to get unique items from it -> that is what set does
student_record=["A","B","C","A","D","C"]

unique_student_record={s for s in student_record}
print(unique_student_record)