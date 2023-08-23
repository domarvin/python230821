#부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("현재 작업중")

    def coding(self):
        print("현재 코딩중")

#자식 클래스 정의
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        #명시적으로 부모것 호출(위처럼 직접 초기화해도되고)
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    #상속받은 메서드재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, subject : {2}, studentID : {3})".format(self.name, self.phoneNumber, self.subject, self.studentID))
        

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__) #__dict__는 딕셔너리 형식으로 멤버변수값 리턴함
# print(s.__dict__)

# 재정의 안하면 부모의 이름/전화번호만 출력됨
p.printInfo()
s.printInfo()
s.working()
s.coding()

