#filter

total_marks = [
    {"user": 'john', "marks": 60},
    {"user": 'mike', "marks": 70},
    {"user": 'ken', "marks": 90},
]
print(list( filter(lambda x: x['marks'] > 80, total_marks) ))