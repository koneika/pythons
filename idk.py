import random

N = 5
NAME = "example.txt"

class data:
    def __init__(self):
        self.name_of_student = ""
        self.faculty_num = 0
        self.av_balls = 0.0
        self.age = 0
        self.gender = ""

def info_from_file_about_students(a):
    with open(NAME, 'r') as f:
        lines = f.readlines()
        for i in range(N):
            line = lines[i].split()
            a[i].name_of_student = line[0]
            a[i].faculty_num = int(line[1])
            a[i].av_balls = float(line[2])
            a[i].age = int(line[3])
            a[i].gender = line[4]

def info_student(a):
    for i in range(N):
        print(a[i].name_of_student, a[i].faculty_num, a[i].av_balls, a[i].age, a[i].gender)

def gui():
    print("MENU\n")
    print("1. input data")
    print("2. output data")
    print("3. overwriting the data for man and woman")
    print("4. sorting by age")
    print("5. the youngest girl")
    print("9. debug(random data)")
    print("0. exit")

def pause_clear():
    input("Press Enter to continue...")
    print("\n" * 100)

def clear():
    print("\n" * 100)

def debug(a):
    with open(NAME, 'w') as f:
        temp_names = ["Aaron", "Abraham", "Adam", "Adrian", "Aidan", "Alan", "Albert", "Alejandro", "Alex", "Alexander", "Alfred", "Andrew", "Angel", "Anthony", "Antonio", "Ashton", "Austin", "Aaliyah", "Abigail", "Ada", "Adelina", "Agatha", "Alexa", "Alexandra", "Alexis", "Alise", "Allison", "Alyssa", "Amanda", "Amber", "Amelia", "Angelina", "Anita", "Ann", "Ariana", "Arianna", "Ashley", "Audrey", "Autumn", "Ava", "Avery", "Benjamin", "Bernard", "Blake", "Brandon", "Brian", "Bruce", "Bryan", "Bailey", "Barbara", "Beatrice", "Belinda", "Brianna", "Bridjet", "Brooke", "Cameron", "Carl", "Carlos", "Charles", "Christopher", "Cole", "Connor", "Caleb", "Carter", "Chase", "Christian", "Clifford", "Cody", "Colin", "Curtis", "Cyrus", "Caroline", "Catherine", "Cecilia", "Celia", "Chloe", "Christine", "Claire", "Daniel", "David", "Dennis", "Devin", "Diego", "Dominic", "Donald", "Douglas", "Dylan", "Daisy", "Danielle", "Deborah", "Delia", "Destiny", "Diana", "Dorothy", "Edward", "Elijah", "Eric", "Ethan", "Evan", "Eleanor"]
        for i in range(N):
            a[i].name_of_student = random.choice(temp_names)
            a[i].gender = "Male" if random.randint(0, 1) == 1 else "Female"
            a[i].age = random.randint(18, 51)
            a[i].av_balls = random.randint(50, 100)
            a[i].faculty_num = 23221000 + random.randint(0, 2000)
            f.write(f"{a[i].name_of_student} {a[i].faculty_num} {a[i].av_balls} {a[i].age} {a[i].gender}\n")

def input_data(a):
    with open(NAME, 'w') as f:
        for i in range(N):
            clear()
            info_student(a)
            a[i].name_of_student = input("please, write name of student here:\n")
            f.write(f"{a[i].name_of_student} ")
        for i in range(N):
            clear()
            info_student(a)
            a[i].faculty_num = int(input("please, write faculty number here:\n"))
            if not isinstance(a[i].faculty_num, int):
                print("Error: write only numbers")
                pause_clear()
                exit(1)
            elif a[i].faculty_num == 0:
                print("Error: dont write 0")
                pause_clear()
                exit(1)
            f.write(f"{a[i].faculty_num} ")
        for i in range(N):
            clear()
            info_student(a)
            a[i].av_balls = float(input("please, write average balls here:\n"))
            if not isinstance(a[i].av_balls, float):
                print("Error: write only numbers or number with comma")
                pause_clear()
                exit(1)
            elif a[i].av_balls == 0:
                print("Error: dont write 0")
                pause_clear()
                exit(1)
            f.write(f"{a[i].av_balls} ")
        for i in range(N):
            clear()
            info_student(a)
            a[i].age = int(input("please, write age here:\n"))
            if not isinstance(a[i].age, int):
                print("Error: write only numbers")
                pause_clear()
                exit(1)
            elif a[i].age == 0:
                print("Error: dont write 0")
                pause_clear()
                exit(1)
            f.write(f"{a[i].age} ")
        for i in range(N):
            clear()
            info_student(a)
            b = input("please, write gender M or F, M - Male, F - Female, here:\n")
            if b in ['M', 'm', 'F', 'f']:
                if b in ['M', 'm']:
                    a[i].gender = "Male"
                elif b in ['F', 'f']:
                    a[i].gender = "Female"
            else:
                print("Error: You are not choose M or F")
                pause_clear()
                exit(1)
            f.write(f"{a[i].gender}\n")

def output(a):
    info_from_file_about_students(a)
    info_student(a)

def owerwriting_the_data_for_man_and_woman(a, a1_rew, a2_rew):
    info_from_file_about_students(a)
    print("Male info:")
    count = 0
    sum = 0
    for i in range(N):
        if a[i].gender == "Male":
            a1_rew[i].name_of_student = a[i].name_of_student
            a1_rew[i].faculty_num = a[i].faculty_num
            a1_rew[i].av_balls = a[i].av_balls
            a1_rew[i].age = a[i].age
            a1_rew[i].gender = a[i].gender
            print(a1_rew[i].name_of_student, a1_rew[i].faculty_num, a1_rew[i].av_balls, a1_rew[i].age, a1_rew[i].gender)
            count += 1
            sum += a1_rew[i].age
    print("avg age by Male(s) =", sum/count)
    sum = 0
    count = 0
    print("Female info:")
    for i in range(N):
        if a[i].gender == "Female":
            a2_rew[i].name_of_student = a[i].name_of_student
            a2_rew[i].faculty_num = a[i].faculty_num
            a2_rew[i].av_balls = a[i].av_balls
            a2_rew[i].age = a[i].age
            a2_rew[i].gender = a[i].gender
            print(a2_rew[i].name_of_student, a2_rew[i].faculty_num, a2_rew[i].av_balls, a2_rew[i].age, a2_rew[i].gender)
            count += 1
            sum += a2_rew[i].age
    print("avg age by Female(s) =", sum/count)

def sorting_by_age(a):
    info_from_file_about_students(a)
    for j in range(N-1):
        for i in range(N-1):
            if a[i].age < a[i + 1].age:
                temp = a[i].age
                a[i].age = a[i + 1].age
                a[i + 1].age = temp

                temp1 = a[i].name_of_student
                a[i].name_of_student = a[i + 1].name_of_student
                a[i + 1].name_of_student = temp1

                temp = a[i].faculty_num
                a[i].faculty_num = a[i + 1].faculty_num
                a[i + 1].faculty_num = temp

                temp2 = a[i].av_balls
                a[i].av_balls = a[i + 1].av_balls
                a[i + 1].av_balls = temp2

                temp1 = a[i].gender
                a[i].gender = a[i + 1].gender
                a[i + 1].gender = temp1
    for i in range(N):
        print(a[i].name_of_student, a[i].faculty_num, a[i].av_balls, a[i].age, a[i].gender)

def the_youngest_girl_by_age(a):
    info_from_file_about_students(a)
    for j in range(N-1):
        for i in range(N-1):
            if a[i].age < a[i + 1].age:
                temp = a[i].age
                a[i].age = a[i + 1].age
                a[i + 1].age = temp

                temp1 = a[i].name_of_student
                a[i].name_of_student = a[i + 1].name_of_student
                a[i + 1].name_of_student = temp1

                temp = a[i].faculty_num
                a[i].faculty_num = a[i + 1].faculty_num
                a[i + 1].faculty_num = temp

                temp2 = a[i].av_balls
                a[i].av_balls = a[i + 1].av_balls
                a[i + 1].av_balls = temp2

                temp1 = a[i].gender
                a[i].gender = a[i + 1].gender
                a[i + 1].gender = temp1
    i = -1
    close = 0
    while close == 0:
        i += 1
        if a[N-1-i].gender == "Female":
            print(a[N-1-i].name_of_student, a[N-1-i].faculty_num, a[N-1-i].av_balls, a[N-1-i].age, a[N-1-i].gender)
            close += 1
        elif N-1-i < 1:
            print("Error, program cannot find a Female")
            close += 1
    close = 0
    i = -1

def main():
    a = [data() for _ in range(N)]
    a1_rew = [data() for _ in range(N)]
    a2_rew = [data() for _ in range(N)]
    while True:
        gui()
        choose = int(input())
        if choose == 0:
            return
        else:
            if choose == 1:
                clear()
                input_data(a)
                pause_clear()
                continue
            elif choose == 2:
                clear()
                output(a)
                pause_clear()
                continue
            elif choose == 3:
                clear()
                owerwriting_the_data_for_man_and_woman(a, a1_rew, a2_rew)
                pause_clear()
                continue
            elif choose == 4:
                clear()
                sorting_by_age(a)
                pause_clear()
                continue
            elif choose == 5:
                clear()
                the_youngest_girl_by_age(a)
                pause_clear()
                continue
            elif choose == 9:
                clear()
                debug(a)
                info_student(a)
                pause_clear()
                continue

main()