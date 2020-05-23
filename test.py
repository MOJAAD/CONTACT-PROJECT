#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT  OF CONTACTS                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/05/5                                                    #
#                                                                                                                   # 
#                                                                                                                   #
#################################################### MODULE #########################################################  
import csv
import time,sys,os
from itertools import zip_longest
############################################### FOR CHECKING FILE ################################################### 
filecontact="CONTACTS.csv"
findfilecontact=os.path.isfile(filecontact)
if findfilecontact==True :
    with open(filecontact, 'r') as csvfile:  
        csvcontacts = csv.reader(csvfile)
        csvfile.close()
else :
    findfilecontact=open(filecontact,"x")
    findfilecontact.close()
    fieldcontact=["firstname","lastname","number","emailaddress","address"]
    with open(filecontact,'w',newline='') as csvfile :
        csvcontacts=csv.writer(csvfile)
        csvcontacts.writerow(fieldcontact)
    csvfile.close()
################################################## CLEAN CONSOLE ####################################################
def cls():
    os.system(['clear','cls'][os.name=='nt'])
############################################### ADDING NEW CONTACT ##################################################
def ADD():
    cls()
    contact=['','','','','']
    print("\t\t _______________________________________________________")
    print("\t\t|         !!!!:YOU MUST TO FILL SIGNED(*) ITEMS         |")
    print("\t\t|       FOR SKIP THE UNSIGNED ITEMS PERSS ENTER !!      |")
    contact[0]=input("\t\t|*ENTER FIRST NAME: ")
    while contact[0]=='':
        contact[0]=input("\t\t|ENTERRRRR!: ")
    contact[1]=input("\t\t|*ENTER LAST NAME: ")
    while contact[1]=='':
        contact[1]=input("\t\t|ENTERRRRR!: ")
    contact[2]=input("\t\t|*ENTER PHONE NUMBER: ")
    while contact[2]=='':
        contact[2]=input("\t\t|ENTERRRRR!: ")
    contact[3]=input("\t\t|ENTER E-MAIL ADDRESS: ")
    contact[4]=input("\t\t|ENTER ADDRESS: ")
    print("\t\t|___________________________________________________|\n")
    sureadd=input("\n\n\n\t\tARE YOU SURE ABOUT THIS CONTACT?(YES or NO)")
    checkadd=1
    while checkadd>0:
        if sureadd.upper()=="YES" or sureadd.upper()=='y' :
            checkadd=-1
        elif sureadd.upper()=="NO" or sureadd.upper()=='n' :
             cls()
             print("\n\n\nSORRY!YOU SHOULD LEARN IN YOUR LIFE,SOMETIMES YOU DON'T HAVE TWO CHANCES!")
             time.sleep(3)
             checkadd=-1 
        else :
             checkadd=1
             print("\t\tENTER CORRECTLY!")
             sureadd=input()
    with open(filecontact,"a",newline='') as csvfile :
        csvcontacts=csv.writer(csvfile)
        csvcontacts.writerow(contact)
        csvfile.close()
############################################## SHOWING ALL OF CONTACT ###############################################
def SHOW():
    cls()
    print("\t\t _________________________________________________________________")
    print("\t\t|                      ALL OF YOUR CONTACTS:                      |")
    with open(filecontact,"r") as csvfile :
        csvcontacts=csv.reader(csvfile)
        for row in csvcontacts :
            print("\t\t|",row)
    csvfile.close()
    print("\t\t|_________________________________________________________________|")
################################################### EDIT CONTACT ####################################################
def EDIT():
    loop=1
    counter=0
    while loop==1 :
        cls()
        SHOW()
        print("\t\t|           ENTER PHONE NUMBER OF CONTACT CORRECTLY:              |")
        edit=input("\t\t|")
        cls()
        print("\t\t _________________________________________________________________")
        with open(filecontact,'r') as csvfile:
            csvcontacts=csv.reader(csvfile)
            for row in csvcontacts :
                if row[2]==edit:
                    print("\t\t|",row)
                    print("\t\t|_________________________________________________________________|")
                    loop=0
                    break
                counter+=1
        if loop==1 or row==["firstname","lastname","number","emailaddress","address"]:
            loop=1
            print("\t\t|        PLEASE ENTER CORRECTLY DEAR USER! IT'S TOO EASY!         |")
            print("\t\t|_________________________________________________________________|")
            input()
    print("\t\t|              WHAT DO YOU WANT TO DO?(ENTER NUMBER)              |")
    print("\t\t| 1)DELETE CONTACT                                                |")
    print("\t\t| 2)EDIT   CONTACT                                                |")
    print("\t\t| 3)BACK TO MAIN MENU                                             |")
    print("\t\t|_________________________________________________________________|")
    while loop==0 :
        in_edit=input()
        if in_edit=='1':
            print("\t\t _________________________________________________________________")
            field_delete=input("\t\t|                  ARE YOU SURE?(YES or NO)                       |\n")
            if field_delete.upper()=="YES" or field_delete.upper()=='y' :
                csvfile.close()
                counter_delete=0
                lines=[['']]
                with open(filecontact,'r') as csvfile :
                    csvcontacts=csv.reader(csvfile)
                    for line in csvcontacts :  
                        if counter_delete==0 :
                            lines[0]=line
                            counter_delete +=1
                        elif  row==line:
                            del line                            
                            continue
                        else:
                            lines.append(line)   
                csvfile.close()     
                with open(filecontact,'w',newline='') as csvfile : 
                    csvcontacts=csv.writer(csvfile)
                    csvcontacts.writerows(lines)
                csvfile.close()
                print("\t\t|                     DELETED SUCCESSFULLY!                       |")
                time.sleep(1)
                pass
            elif field_delete.upper()=="NO" or field_delete.upper()=='n' :
                print("\t\t|       COME ON! ARE YOU SERIOUS? YOU JUST WASTED MY TIME!        |")
                time.sleep(3)
            break
        elif in_edit=='2': 
            print("\t\t _________________________________________________________________")
            print("\t\t|                          WHICH ONE?                             |")
            print("\t\t| 1)FIRST NAME                                                    |")
            print("\t\t| 2)LAST  NAME                                                    |")
            print("\t\t| 3)PHONE NUMBER                                                  |")
            print("\t\t| 4)E-MAIL ADDRESS                                                |")
            print("\t\t| 5)ADRESS                                                        |")
            print("\t\t|_________________________________________________________________|")
            field_edit=input()
            if field_edit=='1':
                row[0]=input("\t\t| ENTER NEW FIRST NAME: ")
            elif field_edit=='2':
                row[1]=input("\t\t| ENTER NEW LAST NAME: ")
            elif field_edit=='3':
                row[2]=input("\t\t| ENTER NEW PHONE NUMBER: ")
            elif field_edit=='4':
                row[3]=input("\t\t| ENTER NEW E-MAIL ADDRESS: ")
            elif field_edit=='5':
                row[4]=input("\t\t| ENTER NEW ADDRESS: ")
            print("\t\t|                      CHANGED SUCCESSFULY!                       |")
            print("\t\t|_________________________________________________________________|")
            csvfile.close()
            counter_edit=0
            lines=[['']]
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile)
                for line in csvcontacts :  
                    if counter_edit==0 :
                        lines[0]=line
                    elif  counter==counter_edit:   
                        lines.append(row)    
                    else :
                        lines.append(line) 
                    counter_edit +=1  
            csvfile.close()     
            with open(filecontact,'w',newline='') as csvfile : 
                csvcontacts=csv.writer(csvfile)
                csvcontacts.writerows(lines)
            csvfile.close()
            time.sleep(1)
            break 
        elif in_edit=='3':
            break   
################################################## SEARCH CONTACT ###################################################
def SEARCH():
    cls()
    no_contact=1
    print("\t\t _______________________________________________________")
    edit1=input("\t\t|             PLEASE ENTER THE FIRST NAME :             |\n\t\t|")
    with open(filecontact,'r') as csvfile:
        csvcontacts=csv.reader(csvfile)
        for row in csvcontacts :
            if row[0]==edit1:
                print("\t\t|_______________________________________________________|")
                print("\t\t|                       THERE IS:                       |")
                print("\t\t|",row)
                print("\t\t|_______________________________________________________|")
                no_contact=0
        csvfile.close()
    if no_contact==1 :
        print("\t\t|_______________________________________________________|")
        print("\t\t|         THERE IS NO CONTACT WHIT THIS NUMBER!         |")
        print("\t\t|_______________________________________________________|")
    input("\t\t|PRESS ENTER TO CONTINUE...                             |\n\t\t|_______________________________________________________|")
################################################## SORT  CONTACTS ###################################################
def SORT():
    cls()
    counter_sort=0
    lines=[]
    with open(filecontact,'r') as csvfile :
        csvcontacts=csv.reader(csvfile) 
        for line in csvcontacts :  
            if counter_sort==0 :
                counter_sort +=1
            else :
                lines.append(line) 
                counter_sort +=1
    csvfile.close()
    for counter1 in range(len(lines)):
        for counter2 in range(len(lines)-1):
            if lines[counter2] > lines[counter2 +1 ]:
                lines.insert(counter2,lines[counter2 +1])
                del lines[counter2 +2]
    print("\t\t _________________________________________________________________")
    print("\t\t|          YOUR CONTACTS HAVE BEEN SORTED BY FIRST NAME:          |")
    for row in lines :
        print("\t\t|",row)
    print("\t\t|_________________________________________________________________|")
################################################# EXPORT FROM LISTS #################################################
def EXPORT() :
    cls()
    column_sorter=[0,0,0,0,0]
    lines=[[''],[''],[''],[''],['']]
    print("\t\t _______________________________________________________________")
    if findfilecontact==False :
        print("\t\t|                           WARNING! :                          |")
        print("\t\t| !!!:EVERY TIMES YOU CAN ADD A NEW COLOMN TO YOUR FILE         |")
        print("\t\t| !!!:AT THE END YOU CAN SEE THE SORT FILE                      |")
        print("\t\t| !!!:BE CURTAIN YOU MUST TO HAVE CONTACT LIST                  |")
        print("\t\t|_______________________________________________________________|")
    print("\t\t|                AT LAST TO EXPORT PERSS ENTER!                 |")
    print("\t\t|                       ENTER BY NUMBER:                        |")
    print("\t\t| 1)EXPORT FIRST NAMES                                          |")
    print("\t\t| 2)EXPORT LAST NAMES                                           |")
    print("\t\t| 3)EXPORT PHONE NUMBERS                                        |")    
    print("\t\t| 4)EXPORT E-MAIL ADDRESSES                                     |")
    print("\t\t| 5)EXPORT ADDRESSES                                            |")
    print("\t\t| 6)BACK TO MAIN MENU                                           |")
    print("\t\t|_______________________________________________________________|")
    counter_export=0      
    while True:
        counter_export=0
        list_export=input()
        if  list_export=='1':
            column_sorter[0]=5
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile) 
                for line in csvcontacts :  
                    if counter_export==0 :
                        lines[0][0]=line[0]    
                    else :
                        lines[0].append(line[0]) 
                    counter_export +=1
            csvfile.close()
        elif list_export=='2': 
            column_sorter[1]=4
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile) 
                for line in csvcontacts :  
                    if counter_export==0 :
                        lines[1][0]=line[1]    
                    else :
                        lines[1].append(line[1]) 
                    counter_export +=1
            csvfile.close()
        elif list_export=='3':
            column_sorter[2]=3
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile) 
                for line in csvcontacts :  
                    if counter_export==0 :
                        lines[2][0]=line[2]    
                    else :
                        lines[2].append(line[2]) 
                    counter_export +=1
            csvfile.close()
        elif list_export=='4':
            column_sorter[3]=2
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile) 
                for line in csvcontacts :  
                    if counter_export==0 :
                        lines[3][0]=line[3]    
                    else :
                        lines[3].append(line[3]) 
                    counter_export +=1
            csvfile.close()
        elif list_export=='5':
            column_sorter[4]=1
            with open(filecontact,'r') as csvfile :
                csvcontacts=csv.reader(csvfile) 
                for line in csvcontacts :  
                    if counter_export==0 :
                        lines[4][0]=line[4]    
                    else :
                        lines[4].append(line[4]) 
                    counter_export +=1
            csvfile.close()
        elif list_export=='6':
            counter_export=1
            break
        elif list_export=='':
            break
        else :
            pass   
    if counter_export==0:
        counter=0
        roof=0
        while roof <= 4  :
            if column_sorter[roof]==0 :
                lines.remove(lines[counter])
                roof +=1
            else :
                counter +=1
                roof +=1
        export_data=zip_longest(*lines , fillvalue='')
        with open("export_contacts_list.csv",'w',encoding="ISO-8859-1",newline='') as exporti:
            exportage=csv.writer(exporti)
            exportage.writerows(export_data)
        exporti.close()    
        os.startfile("export_contacts_list.csv")
################################################### WELCOME PART ####################################################
cls()
print("\n\n                HELLO USER!")
time.sleep(1)
cls()
###################################################### MAIN MENU ####################################################
while True:
    cls()
    print("\t\t ______________________________________")
    print("\t\t|             WELCOME USER!            |")
    print("\t\t|      PLEASE  SELECT BY NUMBER:       |")
    print("\t\t|   1) ADD NEW CONTACT                 |")
    print("\t\t|   2) SHOW YOUR CONTACTS              |")
    print("\t\t|   3) EDIT CONTACT                    |")
    print("\t\t|   4) SEARCH CONTACT                  |")
    print("\t\t|   5) ADVANCE                         |")
    print("\t\t|   6) ABOUT US!                       |")
    print("\t\t|   7) EXIT!                           |")
    print("\t\t|______________________________________|")
    selector=input()
    if selector=='1' :
        ADD()
    elif selector=='2' :
        SHOW()
        input("\n\t\t\t                 ENTER TO CONTINUE...")
    elif selector=='3' :
        EDIT()
    elif selector=='4' :
        SEARCH()
    elif selector=='5' :
        cls()
        print("\t\t ______________________________________")
        print("\t\t|      PLEASE  SELECT BY NUMBER:       |")
        print("\t\t|   1) SORT CONTACTS                   |")
        print("\t\t|   2) EXPORT FROM LISTS               |")
        print("\t\t|   3) BACK TO MAIN MENU               |")
        print("\t\t|   4) EXIT FROM APP                   |")
        print("\t\t|______________________________________|")
        advance=input()
        if advance=='1':
            SORT()
            input("\n\t\t\t                 ENTER TO CONTINUE...")
        elif advance=='2':
            EXPORT()
        elif advance=='4':
            sys.exit(0)
        else :
            pass    
    elif selector=='6' :
            cls()
            print("\t\t ______________________________________ ")
            print("\t\t|             CREATED BY:              |")
            print("\t\t|               MOJAAD                 |")
            print("\t\t|        ELECTRONIC ENGINIEER          |")
            print("\t\t|        IN DATE : 2020/05/5           |")
            print("\t\t|                                      |")
            print("\t\t|      1) BACK TO MAIN MENU            |")
            print("\t\t|      2) EXIT FROM APP                |")
            print("\t\t|______________________________________|")
            us=input()
            if us=='2':
                sys.exit(0)
            else :
                pass        
    elif selector=='7' :
        cls()
        exit=input("\n\n\t\tARE YOU SURE?(YES or NO)\n")
        if exit.upper()=="YES" or exit.upper()=='Y' :
            cls()
            print("\n\n                     BYE!\n")
            time.sleep(0.5)
            cls()
            sys.exit(0)
        elif exit.upper()=="NO" or exit.upper()=='N' :
            pass
    
