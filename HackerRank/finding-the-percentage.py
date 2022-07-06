if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    def convert(string):
        li = list(string.split(" "))
        return li


    somme = 0
    for name in student_marks:
        if name == query_name:
            score = list(student_marks[name])
            for number in score:
                somme = somme + float(number)
            avredge = somme / len(score)
            print("{:,.2f}".format(avredge))