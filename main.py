def calculate_class_averages(classrooms):
    """
    input: dict class{class_name{{name: score}, {name: score}}
    return: dict {classnames: average exam scores}
    """
    
    average_class = {}
    
    for class_name, students_scores in classrooms.items():
        if not students_scores:
            average_class[class_name] = 0
            continue
        
        scores = 0 
        num_grades = 0
        
        for grade in students_scores.values():
            student_avarage = sum(grade) / len(grade)
            scores += student_avarage
            num_grades += 1
        
        if num_grades > 0:    
            average_class[class_name] = round(scores / num_grades, 2)
        else:
            average_class[class_name] = 0
    print(average_class)   
    return average_class

calculate_class_averages({
        "Math": {
            "Alice": [85, 90, 78],
            "Bob": [72, 88, 91],
            "Charlie": [95, 100, 92]
        },
        "Science": {
            "Alice": [80, 85, 88],
            "Bob": [78, 82, 85],
            "Diana": [90, 91, 89]
        },
        "History": {
            "Charlie": [70, 75, 80],
            "Diana": [88, 92, 84]
        }
    })