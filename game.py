
import random


human_variable=None
machine_variable=None

list_1=[5]
list_2=[1,3,7,9]
list_3=[2,4,6,8]

list_4=[]


machine_list1=[1,2,3]
machine_list2=[4,5,6]
machine_list3=[7,8,9]
machine_list4=[1,4,7]
machine_list5=[2,5,8]
machine_list6=[3,6,9]
machine_list7=[1,5,9]
machine_list8=[3,5,7]


table = {
    1:'',
    2:'',
    3:'',
    4:'',
    5:'',
    6:'',
    7:'',
    8:'',
    9:''
}


start=True


while start:
    chose_var = input("Alege optiunea X or 0:")
    if chose_var == 'X':
        print("Your chosen key is X")
        human_variable='X'
        machine_variable='0'

        start = False
    elif chose_var == '0':
        print("Your chosen key is 0")
        human_variable='0'
        machine_variable='X'

        start = False
    else:
        print("You chosen another key")
        start=True


print("Print "+human_variable+" "+machine_variable)


first_player=input("First player 1 or 2")

if first_player==1:
   choseen_position=input("Chose your position from 1 to 9:")

   table.update(choseen_position,human_variable)

   list_4.append(choseen_position)

   machine_chose_position= random.randint(1, 9)

if machine_chose_position in machine_list1:
    print("")
elif machine_chose_position in machine_list2:
    print("")






elif first_player==2:
    print("")

# def myFunction():
#     print("")






