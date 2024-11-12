score = int(input())
if 0 <= score <= 100:
    grade = ["F"] * 6 + ["D", "C", "B", "A","A"]
    print(grade[score // 10])
else:
    print("Invalid score")
