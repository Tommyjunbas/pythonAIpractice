def add_student(grades_dict, name, grade):
    if name in grades_dict:
        grades_dict[name].append(grade)
    else:
        grades_dict[name] = [grade]
    return grades_dict