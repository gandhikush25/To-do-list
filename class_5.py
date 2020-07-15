

########## Normal Pop operation #########
# lst = []



# class lstprac:

#     def display(self):
#         num = int(input("No of values to enter"))
#         for value in range(num):
#             val = input()
#             lst.append(val)
#         print(lst)
            

#         print("Do you want to delete an element:(y/n)")
#         choice = input("enter your choice:")
#         if(choice=="y"): 
#             numm = int(input("Total delete:"))
#             for i in range(numm): 
#                 lst.pop()
#             print("Your final list:",lst)

#         elif(choice =="n"):
#             print("Your final list:",lst)



# s1 = lstprac()
# s1.display()






# ********* list.remove(argument) removes argument means it takes an name of elememt to be deleted ********



# # # # # # # # Delete on position of your choice !!! # # # # # # # #



lst = []


class lstprac:

    def display(self):
        num = int(input("No of values to enter"))
        for value in range(num):
            val = input()
            lst.append(val)
        print(lst)
            

        print("Do you want to delete an element:(y/n)")
        choice = input("enter your choice:")
        if(choice=="y"): 
            numm = int(input("total delete:"))
            for i in range(numm): 
                pos = int(input("Position to delete"))
                lst.pop(pos)
            print("Your final list:",lst)

        elif(choice =="n"):
            print("Your final list:",lst)



s1 = lstprac()
s1.display()


# occurence of tuple and list in list with randomcount()
# and normal occurence of anything in list is counted by lst.count()
















