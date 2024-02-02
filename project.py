"""
Project  : Project App
Author   : Rakesh Karmaker
Location : Dhaka, Bangladesh
Github   : Rakesh-6610
EDX      : Rakesh_Karmaker
Date     : 02/02/2024

"""

from tabulate import tabulate
from datetime import datetime
import sys
import calendar
import re
from fpdf import FPDF
import os
import random
import csv
import time




time1 = datetime.now()
path = 'mcqs.csv'


def main():
    headers = ["Number", "Name"]
    table = [[1,"Days Lived"], [2,"Guess the Number"], [3,"Question Answer"], [4,"Rock Paper Scissor"], ["others", "Exit"]]
    chart = (tabulate(table, headers, tablefmt="heavy_outline"))
    while True:
        print("\n", "-"*os.get_terminal_size().columns, chart, sep="")
        if user_input := input("Type the app number you want to use: "):
            main_modes(user_input)


def main_modes(mode):
    if mode == "1":
        days_lived_main()
    elif mode == "2":
        guess_main()
    elif mode == "3":
        mcqs_main()
    elif mode == "4":
        rps_main()
    else:
        sys.exit("Have a nice day")















#--------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Days Lived-------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


def days_lived_main():
    while True:
        #Asking user for their birthdate
        try:
            user_input : str = input('Enter your birthdate (dd/mm/yyyy) : ').lower().strip()
        except:
            print("Invalid Date format")
            pass

        #Validating the user input
        if (tuser_input(user_input)):
            days_lived : int = days(user_input.split('/'))
            break
        else:
            print("Invalid Date format")
            pass

    #Getting the user's age
    age : int = int(days_lived/365)

    #Setting the image
    if birthday(user_input.split('/')):
        print_congrats(days_lived, age,True)
    else:
        print_congrats(days_lived, age)

def print_congrats(day, age, birthday=False):
    width_text = os.get_terminal_size().columns
    text = "!!!congratulations!!!".upper()
    print("\n",text.center(width_text))
    print(f"You are {age} years old".center(width_text))
    print("\n","You Survived".center(width_text), sep="")
    print(f"{day} Days".center(width_text))
    print("\n","An illustration has been created in a PDF file called: days_lived.pdf".center(width_text), sep="")
    image(day, age, birthday)



def birthday(birthdate) -> bool:
    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    x = datetime.now()
    today = int(x.strftime("%d"))
    month = x.strftime("%B")
    if int(birthdate[0]) == today and month_list[int(birthdate[2])-1] == month:
        return True
    else:
        return False


def image(days_lived, age, birthday=False):
    if birthday:
        m1 = 95
        m2 = 111
    else:
        m1 = 100
        m2 = 120

    width = 300
    height = 180
    pdf = FPDF(orientation="L", format=(height, width))
    pdf.add_page()

    pdf.image("days_lived.jpg",x=0,y=0, h=height, w=width)
    pdf.set_margin(60)
    pdf.set_font('helvetica', size=45)
    pdf.set_text_color((255,255,255))
    pdf.cell(text="congratulations".upper(),center=True, new_x="CENTER", new_y="TOP")



    pdf.set_margin(80)
    pdf.set_font('helvetica', size=32)
    pdf.set_text_color((255,255,255))
    pdf.cell(text=f"You are {age} years old.",center=True, new_x="CENTER", new_y="TOP")

    pdf.set_margin(m1)
    pdf.set_font('helvetica', size=42)
    pdf.set_text_color((255,255,255))
    pdf.cell(text=f"You Survived",center=True, new_x="CENTER", new_y="TOP")

    pdf.set_margin(m2)
    pdf.set_font('helvetica', size=42)
    pdf.set_text_color((255,255,0))
    pdf.cell(text=f"{days_lived} Days",center=True, new_x="CENTER", new_y="TOP")

    if birthday:
        pdf.set_margin(125)
        pdf.set_font('helvetica', size=42)
        pdf.set_text_color((255,0,0))
        pdf.cell(text=f"HappyBirthday",center=True, new_x="CENTER", new_y="TOP")

    pdf.output('days_lived.pdf')

def tuser_input(text) -> bool:
    if matches:=re.search(r"^(\d{2})/(\d{2})/(\d{4})", text):
        #Validating the date
        return True if ((31>=int(matches.group(1))>=1) and (12>=int(matches.group(2))>=1)) else False
    else:
        return False


def days(birthdate) -> int:
    day  : int = 0
    count: int = 1
    x = datetime.now()
    year = int(birthdate[2])

    while year!= int(x.strftime("%Y")):
        if count==1:
            day += year_days(birthdate)
            count+=1
        else:
            day += 366 if (calendar.isleap(year)) else 365
        year += 1

    months = filtered_months(int(x.strftime("%Y"))  , (x.strftime("%B")) , 2)
    for month in months:
        day += (int(x.strftime("%d"))) if (month==(x.strftime("%B"))) else months[month]

    return day


def year_days(birthdate) -> int:
    born_year_days = 0
    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    months = filtered_months(int(birthdate[2]),month_list[(int(birthdate[1])) - 1])

    for month in months:
        if month == month_list[(int(birthdate[1]))-1]:
            born_year_days += (months[month] - (int(birthdate[0])))
        else:
            born_year_days += months[month]

    return born_year_days




def is_leap_year(year) -> int:
    return 29 if (calendar.isleap(year)) else 28



def filtered_months(year,month,mode = 1) -> dict:
    months = {
        "January" : 31,
        "February" : is_leap_year(year),
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November": 30,
        "December" : 31
    }

    un_f_months = {}
    f_months = {}
    for m in months:
        if m==month:
            for i in months:
                if i in un_f_months:
                    pass
                else:
                    f_months.update({i : months[i]})
            else:
                if mode==1:
                    return f_months
                else:
                    un_f_months.update({m : months[m]})
                    return un_f_months
        else:
            un_f_months.update({m : months[m]})







#--------------------------------------------------------------------------------------------------------------------
#---------------------------------------------Guess the Number-------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------




class Number:
    def __init__(self):
        self.ans = 0
        self.time = 0
        self.stime = int(time1.strftime("%M")) + self.time

    def easy(self):
        self.ans = random.randint(1, 15)
        self.time = 1

    def medium(self):
        self.ans = random.randint(1,50)
        self.time = 2

    def hard(self):
        self.ans = random.randint(1,100)
        self.time = 2

    def test(self, n):
        if self.ans == n:
            time2 = datetime.now()
            if self.stime >= int(time2.strftime("%M")):
                print("Perfect!!! You guessed the number.\n", "-" * os.get_terminal_size().columns, sep="")
                return True
            else:
                print("Out of time\n", "-" * os.get_terminal_size().columns, sep="")
                return " "

        elif self.ans > n:
            print("Too Small")
            return False
        elif self.ans < n:
            print("Too Big")
            return False
        else:
            return False



def guess_main():
    guess_heading()

    headers = ["Mode" , "Number", "Time(m)"]
    table = [["1","1-15", 1], ["2","1-50", 2], ["3","1-100", 2], ["4", "Exit"]]
    while True:
        game = Number()
        print(tabulate(table, headers, tablefmt="heavy_outline"))
        try:
            mode = int(input("Mode: "))
        except ValueError:
            print("Invalid Input")
            pass
        else:
            if mode == 1:
                game.easy()
            elif mode == 2:
                game.medium()
            elif mode == 3:
                game.hard()
            elif mode == 4:
                os.system('cls')
                print("Exiting Guess the Number")
                time.sleep(1)
                main()
            else:
                print("Invalid Input")
                pass

            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    print("Invalid Input")
                    pass
                else:
                    if game.test(guess):
                        break
                    else:
                        pass
            con = input("Want to play again (y/n)? ").strip().lower()
            if con == "y":
                pass
            elif con == "n":
                print("Exiting Guess the Number")
                time.sleep(1)
                main()
            else:
                print("Invalid Input")
                pass




def guess_heading():
    text = "!!!Guess the number!!!".upper()
    print("\n",text.center(os.get_terminal_size().columns))











#--------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------M.C.Q.S-------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------





class Question:
    def __init__(self, question, answer, option1, option2, option3, option4):
        self.question = question
        self.answer = answer
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4

        self.options = [
            [1,self.option1],
            [2,self.option2],
            [3,self.option3],
            [4,self.option4],
        ]

    def __str__(self):
        self.headers = ["Question: ", self.question]
        return tabulate(self.options, self.headers, tablefmt="heavy_outline")

    def test(self, user_input):
        if user_input == 'exit':
            print("Exiting Question Answers")
            time.sleep(1)
            main()
        elif str(self.answer) == user_input:
            return True
        else:
            return False

def mcqs_main():
    mcqs_heading()
    rows = get_rows()

    while True:
        headers = ['Type', 'Mode']
        table = [[1,"Answer Questions"], [2,"Add Questions"], [3,"Delete Questions"], [4, 'Exit']]
        print("-"*os.get_terminal_size().columns, "\n", tabulate(table, headers, tablefmt="heavy_outline"), sep="")
        try:
            mode = int(input("Type the mode number: "))
        except ValueError:
            print("Invalid Input")
            pass
        else:
            if mode == 1:
                while rows:
                    ques = random.choice(rows)
                    question = Question(**ques)
                    while True:
                        print(question)

                        user_answer = input("Type the answer number: ")

                        if question.test(user_answer):
                            print("Correct Answer!!")
                            break
                        else:
                            print("Wrong Answer!!")
                            pass
                    rows.remove(ques)

                else:
                    print("\nCongrats!! You answerd all the questions.")
                    if input("Wanna add a question (y/n)? ").lower().strip() == 'y':
                        write_question()
                        print("Exiting Question Answers")
                        time.sleep(1)
                        main()
                    else:
                        print("Exiting Question Answers")
                        time.sleep(1)
                        main()
            else:
                if modes(mode, rows):
                    print("Exiting Question Answers")
                    time.sleep(1)
                    main()
                else:
                    print("Exiting Question Answers")
                    time.sleep(1)
                    main()



def modes(mode, rows):
    if mode == 2:
        if write_question():
            print("Completed!!!")
            return True
        else:
            print("\nMatch: There is a similar question in the question list.")
            if input("Wanna see the list (y/n)? ").strip().lower() == 'y':
                print("-"*os.get_terminal_size().columns)
                for qus in get_questions(rows):
                    print(qus)
                return True
            else:
                return True

    elif mode == 3:
        if delete_row(rows):
            print("Completed!!!")
            return True
        else:
            print("\nNo match")
            if input("Wanna see the list (y/n)? ").strip().lower() == 'y':
                print("-"*os.get_terminal_size().columns)
                for qus in get_questions(rows):
                    print(qus)
                return True
            else:
                return True
    elif mode == 4:
        print("Exiting Question Answers")
        time.sleep(1)
        main()
    else:
        return False

def get_questions(rows):
    return [row['question'] for row in rows]


def delete_row(rows):
    question = input("Question: ")
    new_rows = [row for row in rows if row['question'] != question]
    if rows == new_rows:
        return False
    else:
        with open(path, 'w') as header:
            w_header = csv.writer(header)
            w_header.writerow(['question','answer','option1','option2','option3','option4'])

        with open(path, 'a') as w:
            writer = csv.DictWriter(w, fieldnames=['question', 'answer', 'option1', 'option2', 'option3', 'option4'])
            for new_row in new_rows:
                writer.writerow(new_row)



def get_rows():
    questions = []
    with open(path) as r:
        reader = csv.DictReader(r)
        for row in reader:
            questions.append(row)
    return questions

def write_question():
    rows = get_rows()
    question = input("Question: ")
    for row in rows:
        if row['question'] == question:
            return False
    else:
        option1 = input("Option-1: ")
        option2 = input("Option-2: ")
        option3 = input("Option-3: ")
        option4 = input("Option-4: ")
        answer = input("Answer (Type the option no.): ")

        with open(path, 'a') as w:
            writer = csv.DictWriter(w, fieldnames=['question', 'answer', 'option1', 'option2', 'option3', 'option4'])
            writer.writerow({
                'question' : question,
                'answer' : answer,
                'option1' : option1,
                'option2' : option2,
                'option3' : option3,
                'option4' : option4
            })
        return True



def mcqs_heading():
    text = "!!!Question Answers!!!".upper()
    print("\n",text.center(os.get_terminal_size().columns))



#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Rock Paper Scissor------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def rps_main():
    rps_heading()
    options = ['Rock', 'Paper', 'Scissor']
    headers = ['Nmuber', 'Option']
    table = [[1,"Rock"], [2,"Paper"], [3,"Scissor"], [4,"Exit"]]
    chart = (tabulate(table, headers, tablefmt="heavy_outline"))
    while True:
        print(chart)
        computer = random.choice(options)
        try:
            user_choice = input("Type the option number: ")
        except:
            print("Invalid Input")
            pass
        else:
            if user_choice == '4':
                print("Exiting Rock Paper Scissor")
                time.sleep(1)
                main()
            elif user_choice in ['1', '2', '3']:
                user = options[int(user_choice)-1]
                rps_test(computer, user)
            else:
                print("Invalid Input")
                pass


def rps_test(c,u):
    for i in range(3):
        print(f"{i+1}".center(os.get_terminal_size().columns))
        time.sleep(1)
    else:
        if c == u:
            print("Draw".center(os.get_terminal_size().columns))
        elif c == 'Rock':
            if u == "Paper":
                print("WON".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))
            else:
                print("LOST".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))

        elif c == 'Paper':
            if u == "Scissor":
                print("WON".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))
            else:
                print("LOST".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))

        elif c == 'Scissor':
            if u == "Rock":
                print("WON".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))
            else:
                print("LOST".center(os.get_terminal_size().columns))
                print(f"You choosed {u} and the computer choosed {c}".center(os.get_terminal_size().columns))

        if input("Wanna play again (y/n)? ").strip().lower() == 'y':
            print("-"*os.get_terminal_size().columns)
            rps_main()
        else:
            print("Exiting Rock Paper Scissor")
            time.sleep(1)
            main()



def rps_heading():
    text = "!!!Rock Paper Scissor!!!".upper()
    print("\n",text.center(os.get_terminal_size().columns))

if __name__=="__main__":
    main()
