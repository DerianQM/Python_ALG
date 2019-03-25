
from memory_profiler import profile


@profile
def main():
    class School:
        __slots__= ['class_room', 'class_label','predmets']
        def __init__(self, class_room, class_label,predmets):
            self.class_room = class_room
            self.class_label = class_label
            self.predmets = predmets
        def get_name(self):
            return  'Класс ' + str(self.class_room)+' '+ self.class_label
        def get_predmet(self):
            return  self.predmets

    class People:
        __slots__= ['name', 'surname', 'second_name']
        def __init__(self, name, surname, second_name):
            self.name = name
            self.surname = surname
            self.second_name = second_name
        def get_full_name(self):
            return self.surname + ' ' + self.name + ' ' + self.second_name

    class Student(People):
        __slots__=['name', 'surname', 'second_name', 'class_room','predmets','father', 'mother']
        def __init__(self, name, surname, second_name, class_room,predmets, father = 'нет', mother = 'нет'):
            People.__init__(self, name, surname, second_name)
            self.class_room = class_room
            self.predmets = predmets
            self.father = father
            self.mother = mother

        def get_class_room(self):
            return self.class_room
        def get_parents(self):
            return self.father.get_full_name(), self.mother.get_full_name()
        def get_predmet(self):
            return self.predmets

    class Teacher(People):
        __slots__=['name', 'surname', 'second_name', 'classes', 'subject']
        def __init__(self, name, surname, second_name, classes, subject):
            People.__init__(self, name, surname, second_name)
            self.classes = classes
            self.subject = subject
        def get_subject(self):
            return self.subject
        def get_classes(self):
            return self.classes



    list1 = [1,2,3,4,5,6,7,8,9,10,11]# всю эту пакость можно и с клавиатуры задать
    list2 = ['A','B','C','D']
    list3 = ['Математика', 'Русский язык', 'География', 'Геометрия']

    mass = [School(list1[5],list2[1],list3[:-1]),  # конструирую обьекты, чтобы применить к ним get_name
            School(list1[9],list2[0],list3[:]),
            School(list1[7],list2[3],list3[:])]
    class_rooms = [i.get_name() for i in mass]
    class_predmets = [i.get_predmet() for i in mass] # а это костыль для предметов

     # ну и тд, можно вообще с клавиатуры в этот список нарезать и все, вообщем создаем список из классов в школе


    father = [People("Алексей", "Машкевич", "Валерьевич"),# конструирую список отцов! (все они люди)
              People("Петр", "Иванов", "Иванович"),
              People("Михаил", "Калинин", "Михайлович")]
    mother = [People("Марина", "Машкевич", "Максимовна"), # конструирую список матерей (все они люди)
              People("Ирина", "Иванова", "Александровна"),
              People("Анна", "Калинина", "Николаевна")]
    students = [Student("Александр", "Машкевич", "Игоревич", class_rooms[0],class_predmets[0], father[0], mother[0]), # конструирую список учеников с данными из списка отцов, матерей и класса обучения
                Student("Петр", "Калинин", 'Иванович', class_rooms[1],class_predmets[1], father[0], mother[0]),
                Student("Иван", "Петров", 'Николаевич', class_rooms[1],class_predmets[1], father[2], mother[2]),
                Student("Алексей", "Иванов", "Игоревич", class_rooms[2],class_predmets[2],father[1], mother[1]),
                Student("Евгений", "Ещекакойто", 'Иванович', class_rooms[2],class_predmets[2], father[0], mother[0]),
                Student("Андрей", "Нуитакойжекакеще", 'Николаевич', class_rooms[2], class_predmets[2],father[2], mother[2])]
    teachers = [Teacher("Петр", "Гавриленко", "Игоревич", [class_rooms[0], class_rooms[1], class_rooms[2]], list3[0]), # конструирую список преподавателей, где classes  - может быть именно список из классов, те принимать сколько угодно значений, тоже можно сделать и с предметами, это в Росс школах обычное явление
                Teacher("Максим", "Хайзи", "Александрович", [class_rooms[1], class_rooms[2]], list3[1]),
                Teacher("Николай", "Беловерцев", "Владимирович", class_rooms[2], list3[2])]


    print("Все классы: ",class_rooms )


    for num, Student in enumerate(students, start=1):
        print("Все ученики в классах: {}) {} {}".format(num, Student.get_class_room(), Student.get_full_name()))

    for num, Parents in enumerate(students, start=1):
        print("Родители всех учеников: {}) Ученик: {} Родители: {}".format(num, Parents.get_full_name(), Parents.get_parents()))

    for num, Teacher in enumerate(teachers, start=1):
        print("Список учителей: {}) Учитель: {} Препадаёт в классе: {}".format(num, Teacher.get_full_name(), Teacher.get_classes()))

    for num, Student in enumerate(students, start=1):
        print("Все предметы ученика: {} {} {}".format(num, Student.get_full_name(),Student.get_predmet()))


    print("Задачу это надо решать через БД а не через вакханалию с классами")


if __name__ == '__main__':
    main()