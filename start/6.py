students =[
{"name" : "xiao min","score" : 55},
{"name" : "xiao hong","score" : 80},
{"name" : "xiao gg","score" : 70}
                            ]

final = sorted(students,key=lambda student : student["score"])

print(final)