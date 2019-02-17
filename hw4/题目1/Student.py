"""
Student.py
A program reports all students having the highest GPA.
Modified by SA18225209
"""
class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    # 打开输入文件
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')
    # 设置文件中第一个学生的记录为best
    record=[]
    best = makeStudent(infile.readline())
    record.append(best)
    # 处理文件剩余行数据
    for line in infile:
        # 将每一行数据转换为一个记录
        s = makeStudent(line)
        # 如果该学生是目前GPA最高的，则记录下来
        if s.gpa() > best.gpa():
            best = s
            record.clear()
            record.append(s)
        elif s.gpa()==best.gpa():
            record.append(s)

    infile.close()

    # 打印GPA成绩最高的学生信息
    for stu in record:
        print("One of the best student is:", stu.getName())
        print("hours:", stu.getHours())
        print("GPA:", stu.gpa())


if __name__ == '__main__':
    main()
