import csv
import pickle
import os
import sys
from colorama import Fore, init
import random
import shutil
from tkinter import filedialog
import tkinter
import subprocess
from datetime import datetime

class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

pers_log_path = 'Client/PerLog'
if os.path.isdir(pers_log_path)==False:
    os.makedirs(pers_log_path)
contract_file='Open Files/Contracts.csv'
userdata_loc='Server/Main Files/userdata.csv'
main_file_path = 'Client/Files'
main_log_path = main_file_path+'/Logins'
perlog_path = pers_log_path+'/PerLog.csv'
projects_main_loc='Server/Main Files/Projects'


# TODO / MAKE BETTER ROLES AND CUSTOM ROLES
# TODO / MAKE A FACTION CREATION SYSTEM
# TODO / MAKE HIDDEN FRONT END
# TODO / MAKE LIVE CHATTING
# ! ADD ENCRYPTION TO ALL HUMAN READABLE TEXTS
# ? ADD MORE FEATURES IN GROUP SYSTEMS
# ? - ADD GROUP ACCOUNTING PAGE
# ? - ADD DATA/FILE ENCRYPTION
# ? - STRUCTURED TIMELINE
#
#
#




# ? ======================================================================
# *            MISC FUNCTIONS
# ? ======================================================================

# ? NEEDS BETTER ENCRYPTION SYSTEM
def hashcust(u,p):
    ceas1=ceas2=''
    p1=u1=''
    for k in p:
        ceas1+=chr(ord(k)-len(p))
    for k in u:
        ceas2+=chr(ord(k)+len(u))
    for k in ceas1:
        p1+=str(ord(k))
    for k in ceas2:
        u1+=str(ord(k))
    p1=int(p1)
    u1=int(u1)
    has=p1*u1
    fin=has*has
    return fin

def clear():
    os.system('cls')

# * SERVER SIDE LOG-OUT SYSTEM
def quit(cnp): 
    path_temp=main_log_path+f'/Log{cnp}/Temp.csv'
    temp=open(path_temp, 'w', newline='')
    fw=csv.writer(temp)
    rec=[]
    fw.writerow(rec)
    temp.close()
    
    path_user=main_log_path+f'/Log{cnp}/User.csv'
    temp_1=open(path_user, 'w', newline='')
    fw_1=csv.writer(temp_1)
    rec=[]
    fw_1.writerow(rec)
    temp_1.close()

    temp_1=open(perlog_path, 'w', newline='')
    fw_1=csv.writer(temp_1)
    rec=[]
    fw_1.writerow(rec)
    temp_1.close()

    passwordmain()

# * GROUP USERNAME AND GROUP VERIFICATION
def verify_us_ch(chk_n):
    global us
    global name_of_main
    str_1=main_log_path+f'/Log{chk_n}/Temp.csv'
    txt_file=open(str_1,'r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        name_of_main=k[0]
        us=k[1]
    txt_file.close()

# * GROUP USERNAME AND GROUP ACCESSORY VERIFICATION 
def verification_0(chk_n):
    global name_of_main
    global us
    global main_desc
    global clr_acc
    global clr_main
    global rec_num
    global access
    # Main Settings 1
    str_1=main_log_path+f'/Log{chk_n}/Temp.csv'
    txt_file=open(str_1,'r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        name_of_main=k[0]
        us=k[1]
    txt_file.close()
    # Main Settings 2
    txt_file=open('Server/Mainframe.csv','r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        if k[1]==name_of_main and k[2]==us:
            access=k[3]
            rec_num=k[0]
    txt_file.close()
    # Main Settings 3
    fout=open('Server/'+rec_num+' '+name_of_main+' Mainframe/'+rec_num+' '+name_of_main+' Mainframe Main Setings.csv', 'r')
    fr=csv.reader(fout)
    for k in fr:
        main_desc=k[1]
        clr_main_str=k[2]
        clr_acc_str=k[3]
    # Main Color Chooser
    if clr_main_str.upper()=='BLUE':
        clr_main=Fore.BLUE
    elif clr_main_str.upper()=='GREEN':
        clr_main=Fore.GREEN
    elif clr_main_str.upper()=='RED':
        clr_main=Fore.RED
    elif clr_main_str.upper()=='CYAN':
        clr_main=Fore.CYAN
    elif clr_main_str.upper()=='YELLOW':
        clr_main=Fore.YELLOW
    elif clr_main_str.upper()=='WHITE':
        clr_main=Fore.WHITE
    else:
        clr_main=Fore.RESET
    # Accent Color Chooser
    if clr_acc_str.upper()=='BLUE':
        clr_acc=Fore.BLUE
    elif clr_acc_str.upper()=='GREEN':
        clr_acc=Fore.GREEN
    elif clr_acc_str.upper()=='RED':
        clr_acc=Fore.RED
    elif clr_acc_str.upper()=='CYAN':
        clr_acc=Fore.CYAN
    elif clr_acc_str.upper()=='YELLOW':
        clr_acc=Fore.YELLOW
    elif clr_acc_str.upper()=='WHITE':
        clr_acc=Fore.WHITE
    else:
        clr_acc=Fore.RESET

# * FILE LOCATION WINDOW
def open_file():
    win=tkinter.Tk()
    win.withdraw()

    up_file_path=filedialog.askopenfilename()
    return up_file_path

# * VERSION CONTROL
def log_check():
    global main_str
    global test_ver

    ver_path='Client/Files/Ver_control.csv'
    ver_open=open(ver_path, 'r')
    ver_read=csv.reader(ver_open)
    for k in ver_read:
        main_str=k[0]
        test_ver=k[1]
    ver_open.close()    

# * MADE TO CONTAIN GLOBAL INPUTS
def centeral_main_input(ipt):
  if ipt.upper()=='GROUPS':
    mainframeview(us)
  elif ipt.upper()=='X':
    quit(check_num)
  elif ipt.upper()=='HELP' or ipt=='?':
    help(us)
  elif ipt.upper()=='RETURN' or ipt=='-':
    mainframeview(us)
  elif ipt.upper()=='PLAYERS' or ipt.upper()=='PLAYER':
    user_read()
  elif ipt.upper()=='CONTRACTS' or ipt.upper()=='CONTRACT':
    contracts()
  elif ipt.upper()=='PROFILE':
    user_settings(check_num)
  elif ipt.upper()=='MAIL':
    mail(check_num)
  elif ipt.upper()=='BACK':
    mainframeview(us)
  else:
      print()

# * VERIFY CLIENT AND SERVER USERNAME
def verify(check_num):
    global us
    # Main Settings 1
    file_op=main_log_path+f'/Log{check_num}/User.csv'
    txt_file=open(file_op,'r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        us=k[0]
    txt_file.close()

# ! Find Elegant solution to multiple Server usages
def logcheck(username, group='NULL'):

    if not os.path.isdir(main_log_path):
        os.makedirs(main_log_path)

    chk=os.listdir(main_log_path)
    chk_n=0
    for k in chk:
        try:
            temp_log_path=main_log_path+f'/Log{chk_n}/Temp.csv'
            temp_log=open(temp_log_path,'r')
            fr=csv.reader(temp_log)
            for k in fr:
                if k[2]=='Logged':
                    chk_n+=1
                elif k[1]==username:
                    break
                else:    
                    break
                temp_log.close()
        
        except:
            break
    if os.path.isdir(main_log_path+f'/Log{chk_n}')==False:
        os.makedirs(main_log_path+f'/Log{chk_n}')
    
    t_path=main_log_path+f'/Log{chk_n}/Temp.csv'
    temp_log=open(t_path,'w', newline='')
    fw=csv.writer(temp_log)
    r=[group,username,'Logged']
    fw.writerow(r)
    temp_log.close()
    usr_path_str=main_log_path+f'/Log{chk_n}/User.csv'
    usr_path=open(usr_path_str,'w', newline='')
    fw_1=csv.writer(usr_path)
    rec=[username]
    fw_1.writerow(rec)
    usr_path.close() 

    return chk_n

# ! Make it multiple usage worth
def specialcheck(s):
    u=lv=d=sp=0
    l=s.strip()
    for k in l:
        for i in k:
            if i>='A' and i<='Z':
                u+=1
            elif i>='a' and i<='z':
                lv+=1
            elif i>='0' and i<='9':
                d+=1
            else:
                sp+=1
    return sp  

# * ADD ANY AND ALL DOCUMENTATION HERE
def help(username_te):
    spacer=' '*(73-len(username_te))
    exit_btn=Fore.RED+'[X]'+Fore.RESET
    usr=username_te+Fore.RESET
    clear()
    pg1=f'''
    =========================================================================================
    {usr}{spacer}{exit_btn}
    =========================================================================================
      {main_str}    {test_ver}
    -----------------------------------------------------------------------------------------
        {Fore.LIGHTBLUE_EX}HELP!{Fore.RESET}                                                                             Pg1

        You are using {main_str} {test_ver}, There are some rules to 
        Remember in each of the sections.

        Enter 'RETURN' or '-' to go back to HOME

        In any point in the software, Enter 'X' to Log Out, You can change this later

        {Fore.LIGHTBLUE_EX}MAIL:{Fore.RESET}  
        - You have 8 Active mail outbox and Inbox slots, Which means, if you send
          or recieve more than 8 Mails, the oldest mail is deleted, regardless of
          the read/unread status

        {Fore.LIGHTBLUE_EX}GROUPS:{Fore.RESET}  
        - In this verision of the Mainframe Software, the limit of groups you can
          join or make are 5, this may or may not change in the coming updates.

        - To Join/create a new group in an account which has already reached the
          Group limit, you must delete/exit from a group to allow more space.

                                                                Press ENTER to go to page 2 ->
    ==========================================================================================
    '''
    print(pg1)
    s=input()
    clear()
    if s.upper()=='X':
        quit(cnp)
    elif s.upper()=='RETURN' or s.upper()=='-':
        mainframeview(username_te)


    pg2=f'''
    =========================================================================================
    {username_te}{spacer}{exit_btn}
    =========================================================================================
      {main_str}    {test_ver}
    -----------------------------------------------------------------------------------------
        {Fore.LIGHTBLUE_EX}HELP!{Fore.RESET}                                                                             Pg2    
    
        {Fore.LIGHTBLUE_EX}ROLES:{Fore.RESET}  
        - In any group there are 3 Roles a User may get, these are as follows;

            a){Fore.RED}Admin{Fore.RESET} - This role is only given to the User who made the Group
            b){Fore.YELLOW}Manager{Fore.RESET} - This role is given to Users by the Admins, allowing
                        them to upload and edit files
            c){Fore.BLUE}Normal{Fore.RESET} - This role is given to Users by Admins/Managers and
                       allows them to only view files

        {Fore.LIGHTBLUE_EX}Commands:{Fore.RESET}  
        - When you are in the Home Page, You can press '+' to create a new group. 
        - When you want to view a group, you can either;
            a) Enter the name of group (Not Case Sensitive)
            b) Enter the number value of the group, shown to the left of the group name,
               For example:

                1) EXAMPLE-NAME

            (To access this Group, EXAMPLE-NAME, we can enter the number 1 to access it)

                                                                Press ENTER to go to page 3 ->
    ==========================================================================================
    '''
    print(pg2)
    s=input()
    clear()
    if s.upper()=='X':
        quit(cnp)
    elif s.upper()=='RETURN' or s.upper()=='-':
        passwordmain(username_te)

    pg3=f'''
    =========================================================================================
    {username_te}{spacer}{exit_btn}
    =========================================================================================
      {main_str}    {test_ver}
    -----------------------------------------------------------------------------------------
        {Fore.LIGHTBLUE_EX}HELP!{Fore.RESET}                                                                             Pg3    

        {Fore.LIGHTBLUE_EX}Commands:{Fore.RESET} 
        - When you open a folder, you can use commands '/u' and '/d' to upload and
          delete files respectivly, if you have the Authroity to do so.
        - To open a file or folder, you can either;
            a) Enter the name of the file/folder (Not Case Sensitive)
            b) Enter the number value of the file/folder, shown to the left of the 
               group name, For example:

               1) EXAMPLE-THING

            (To open this file/folder, EXAMPLE-THING, we can enter the number 1 to access it)

        - To open the Pages on the Coloums such as, Groups, Mail and Settings, just enter the
          name of the Page such as 'Groups', 'Mail', 'Settings'. (Not Case Sensitive)

                                                                Press ENTER to go to page 4 ->
    ==========================================================================================
    '''
    print(pg3)
    s=input()
    clear()
    if s.upper()=='X':
        quit(cnp)
    elif s.upper()=='RETURN' or s.upper()=='-':
        passwordmain(username_te)

    pg4=f'''
    =========================================================================================
    {username_te}{spacer}{exit_btn}
    =========================================================================================
      {main_str}    {test_ver}
    -----------------------------------------------------------------------------------------
        {Fore.LIGHTBLUE_EX}HELP!{Fore.RESET}                                                                             Pg4    

        {Fore.LIGHTBLUE_EX}Commands:{Fore.RESET} 
        - If you are an Admin, you can promote/demote any user who has access to your Server
          by typing in any of the following commands,
            a) 'UPDATE'
            B) 'ROLES'
            C) 'UP'
        
        - To exit a Group you do not own, you can use the '/R' command to remove that group
          from your home page

        - To delete a group that you are an Admin of from the Main Server, Enter the command,
          '/d' in the Home Page 

        - In a group that you are a manager/Admin, you can use the '/l' command to see the list
          of users who have joined/use your group.

        - To back to a previous page, enter 'RETURN' or '-'. 

        {Fore.LIGHTBLUE_EX}Remember:{Fore.RESET} 
        - If you want to delete your account, just remember that its irreversible and that 
          the groups which you own and have no Admins, will be deleted.

                                                                Press ENTER to go to HOME ->
    ==========================================================================================
'''
    print(pg4)
    s=input()
    clear()
    if s.upper()=='X':
        quit(cnp)
    elif s.upper()=='RETURN' or s.upper()=='-':
        passwordmain(username_te)




# ? ======================================================================
# *            MAIN SCREEN FUNCTIONS
# ? ======================================================================

# TODO / Make Better Analog UI
def passwordmain():
    global cnp
    clear()
    path=main_file_path
    if os.path.isdir(path):
        print()
    else:
        os.makedirs(main_file_path)
    if not os.path.isdir(pers_log_path):
        os.makedirs(pers_log_path)
    login=''
    try:
        fk=open(perlog_path,'r')
    except:
        print()
    try:
        fw=csv.reader(fk)
        for k in fw:
            login=k[0]
        fk.close()    
    except:
        print()
    if login=='':
        while True:
            clear()
            print('''
            ====================================================

                                The Mainframe
                            ----------------------
                              Sign up or Log in
            ---------------------------------------------------

            ====================================================
                ''')
            
            print(Fore.GREEN+'Enter S to Sign up ', end='')
            print(Fore.GREEN+'Enter L to Log in ')
            print(Fore.RESET)
            ipt=input('=> ')
            if ipt.upper()=='S' or ipt.upper()=='SIGN UP' or ipt.upper()=='SIGN':
                user_true=True
                while user_true==True:
                    false_usr=True
                    fout=open('Server/Main Files/Password.csv','r')
                    pass_read=csv.reader(fout)
                    print('We recommend using Fake names')
                    print('---------------------------------------')
                    first_name=input('Please Enter your First name: ')
                    last_name=input('Please Enter your Last name: ')
                    username=first_name+' '+last_name
                    for k in pass_read:
                        if username==k[0]:
                            false_usr=False
                    if len(username)>16 and specialcheck(username)==0 and false_usr==True:
                        print('Make sure there are no special Characters and the full name is 15 Characters or below')
                    else:
                        user_true=False
                pass_chker=False
                password=input("Enter Password: ")
                re_password=input("Re-type Password: ")
                if password==re_password:
                    pass_chker=True
                    cnp=logcheck(username)
                    records=[]
                    fin=hashcust(username,password)
                    fout=open('Server/Main Files/Password.csv','a', newline='')
                    fw=csv.writer(fout)
                    print("=" * 30)
                    rec = [username, fin]
                    records.append(rec)
                    fw.writerows(records)
                    fout.close()

                    if os.path.isdir(pers_log_path)==False:
                        os.makedirs(pers_log_path)
                        creation_file=open(perlog_path, 'a', newline='')
                        creation_file.close()

                    temp_file=open(perlog_path, 'w', newline='')
                    temp_read=csv.writer(temp_file)
                    temp_read.writerow([username])
                    temp_file.close()

                    extrarec(username)

                if pass_chker==False:
                    print('Incorrect Password')
            
            elif ipt.upper()=='L' or ipt.upper()=='LOGIN':
                username=input("Enter Username: ")
                password=input("Enter Password: ")
                c=0
                final_pass=hashcust(username,password)

                fout=open('Server/Main Files/Password.csv','r') 
                fr=csv.reader(fout)
                for k in fr:
                    if (username==k[0]) and (str(final_pass)==k[1]):
                        cnp=logcheck(username)
                        if os.path.isdir(pers_log_path):
                            print()
                        else:
                            os.makedirs(pers_log_path)
                            creation_file=open(perlog_path, 'a', newline='')
                            creation_file.close()

                        temp_file=open(perlog_path, 'w', newline='')
                        temp_read=csv.writer(temp_file)
                        temp_read.writerow([username])
                        temp_file.close()
                        mainframeview(username)
                if c==0:
                    print('Username or Password is Incorrect!')
                    input()
                    sys.exit()  
    
    else:   
        data=[]
        ftut=open(perlog_path,'r')
        fr=csv.reader(ftut)
        for k in fr:
            username=k[0]
        ftut.close()
        mainframeview(username)
    clear()

# TODO / More information on Banking and more
def extrarec(username):
    clear()
    p='''
    ======================================================================
        Some Extra Information that we require before signing you in
    ======================================================================

    '''
    print(p)
    print()


    gen=input('      -Please Enter your Gender (M/F/Other): ')
    print()
    profes=input('      -Please Enter your Profession: ')
    print()
    acc_no=random.randint(10000,99999)
    acc_ck=open(userdata_loc,'r')
    fr=csv.reader(acc_ck)
    tes_chk=True
    while tes_chk:
        acc_exists=False
        for k in fr:
            if str(acc_no)==k[1]:
                acc_exists=True
                break
        if not acc_exists:
            tes_chk=False
        else:
            acc_no=random.randint(10000, 99999)
    acc_ck.close()
    print('      -Your Account number is ',acc_no)
    print('======================================================================')
    print('Thank you for choosing us')

    acc_op=open(userdata_loc,'a',newline='')
    fr=csv.writer(acc_op)
    rec=[username,acc_no,'Active','None',gen,profes]
    fr.writerow(rec)
    acc_op.close()
    print('======================================================================')
    print('            Press Enter to go to Main Page')
    input(' =>')
    mainframeview(username)

# * MAIN SCREEN
# TODO / MAKE BETTER GROUP ARRANGMENT SYSTEMS TO MAXIMSE MORE SPACE FOR GROUPS 
def mainframeview(usr):
    while True:
        global us
        global check_num
        us=usr
        clear()
        n=0
        c=0
        ftut=open('Server/Mainframe.csv','r')
        fr=csv.reader(ftut)
        one_main=two_main=three_main=four_main=five_main='+'
        access_one=access_two=access_three=access_four=access_five=''
        ac_clr_1=ac_clr_2=ac_clr_3=ac_clr_4=ac_clr_5=''
        help_str=Fore.LIGHTRED_EX+'Enter ''HELP'' or ''?'' if you need the list of commands'+Fore.RESET
        end_main='Enter + to make a new Server'
        for k in fr:
            if k[2]==usr:
                if n==0:
                    one_main=k[1]
                    one_code=k[0]
                    access_one=k[3]
                    if access_one.upper()=='ADMIN':
                        ac_clr_1=Fore.RED
                    elif access_one.upper()=='MANAGER':
                        ac_clr_1=Fore.YELLOW
                    elif access_one.upper()=='NORMAL':
                        ac_clr_1=Fore.BLUE
                    n+=1
                elif n==1:
                    two_main=k[1]
                    two_code=k[0]
                    access_two=k[3]
                    if access_two.upper()=='ADMIN':
                        ac_clr_2=Fore.RED
                    elif access_two.upper()=='MANAGER':
                        ac_clr_2=Fore.YELLOW
                    elif access_two.upper()=='NORMAL':
                        ac_clr_3=Fore.BLUE
                    n+=1
                elif n==2:
                    three_main=k[1]
                    three_code=k[0]
                    access_three=k[3]
                    if access_three.upper()=='ADMIN':
                        ac_clr_3=Fore.RED
                    elif access_three.upper()=='MANAGER':
                        ac_clr_3=Fore.YELLOW
                    elif access_three.upper()=='NORMAL':
                        ac_clr_3=Fore.BLUE
                    n+=1
                elif n==3:
                    four_main=k[1]
                    four_code=k[0]
                    if access_four.upper()=='ADMIN':
                        ac_clr_4=Fore.RED
                    elif access_four.upper()=='MANAGER':
                        ac_clr_4=Fore.YELLOW
                    elif access_four.upper()=='NORMAL':
                        ac_clr_4=Fore.BLUE
                    access_four=k[3]
                    n+=1
                elif n==4:
                    five_main=k[1]
                    five_code=k[0]
                    if access_five.upper()=='ADMIN':
                        ac_clr_5=Fore.RED
                    elif access_five.upper()=='MANAGER':
                        ac_clr_5=Fore.YELLOW
                    elif access_five.upper()=='NORMAL':
                        ac_clr_5=Fore.BLUE
                    access_five=k[3]
                    n+=1
                elif n==5:
                    end_main='NO MORE SPACE TO MAKE A SERVER'
        ftut.close()
        usr_noclr=usr
        username_te=Fore.BLUE+usr+Fore.RESET
        spacer=' '*(73-len(usr_noclr))
        exit_btn=Fore.RED+'[X]'+Fore.RESET
        cnp=logcheck(usr_noclr)
        check_num=cnp
        clear()
        grps=Fore.MAGENTA+'Groups'+Fore.RESET
        mainstr=f'''
    =============================================================================
     {username_te}{spacer}{exit_btn}
    =============================================================================
    │   COLUMN    │ {main_str}    {test_ver}
    │-------------│==============================================================
    │  -{grps}    │   1) {one_main} {ac_clr_1+'('+access_one+')'+Fore.RESET}
    │-------------│
    │  -Contracts │   2) {two_main} {ac_clr_2+'('+access_two+')'+Fore.RESET}
    │-------------│ 
    │  -Mail      │   3) {three_main} {ac_clr_3+'('+access_three+')'+Fore.RESET}
    │-------------│
    │  -Settings  │   4) {four_main} {ac_clr_4+'('+access_four+')'+Fore.RESET}
    │-------------│
    │  -Profile   │   5) {five_main} {ac_clr_5+'('+access_five+')'+Fore.RESET}
    │-------------│
    │  -Chats     │ {end_main}
    │-------------│ 
    │  -Players   │ {help_str}
    =============================================================================
            '''
        print(mainstr)

        ipt=input('=>')

        if ipt=='':
            ipt=ipt+'.'

        if ipt=='+':
            if n!=5:
                print('======================================================================')
                print(Fore.RED+'Enter All the information needed to create your own Mainframe')
                print(Fore.RESET)
                name_ch=True
                fout=open('Server/Mainframe.csv')
                while name_ch:
                    c=0
                    fr=csv.reader(fout)
                    main_name=input('Enter name of your Mainframe: ')
                    for k in fr:
                        if k[1]==main_name:
                            c+=1
                    if c!=0:
                        print('GROUP NAME EXISTS!')
                        print('------------------------------------')
                    else:
                        name_ch=False
                main_desc=input('Enter a Short Description: ')
                print('----------------------------')
                print('Please choose your Color theme')
                print('----------------------------')
                print()
                print('Choose your Main Color')
                print(Fore.BLUE + 'Blue','      ', Fore.GREEN+'Green','      ',Fore.CYAN+'Cyan','      ',Fore.RED+'Red','      ',Fore.YELLOW+'Yellow','      ',Fore.WHITE+'White')
                print()
                clr_main=input('Enter Color name: ')
                print('-----------------------------------')
                print('Choose your Accent Color')
                print(Fore.BLUE + 'Blue','      ', Fore.GREEN+'Green','      ',Fore.CYAN+'Cyan','      ',Fore.RED+'Red','      ',Fore.YELLOW+'Yellow','      ',Fore.WHITE+'White')
                print()
                clr_acce=input('Enter Color name: ')
                print()
                # Saves Mainframe Settings to be used later
                records=[]
                rec_tr=True
                rec_num=str(random.randint(100, 99999999))
                os.makedirs('Server/'+rec_num+' '+main_name+' Mainframe')
                os.makedirs('Server/'+rec_num+' '+main_name+' Mainframe/Folders')
                fout=open('Server/'+rec_num+' '+main_name+' Mainframe/'+rec_num+' '+main_name+' Mainframe Main Setings.csv', 'w',newline='')
                fw=csv.writer(fout)
                rec=[main_name,main_desc,clr_main,clr_acce]
                records.append(rec)
                fw.writerows(records)
                fout.close()
                records.clear()
                # Saves Mainframe name and user under Files/Mainframe.csv
                file_namesave=open('Server/Mainframe.csv', 'a',newline='')
                fw=csv.writer(file_namesave)
                rec=[rec_num,main_name,usr_noclr,'Admin']
                records.append(rec)
                fw.writerows(records)
                file_namesave.close()
                # Gets ready to open the Mainframe
                ck=logcheck(usr_noclr,main_name)
                c+=1
            else:
                print('YOU HAVE REACHED THE LIMIT ON THE NUMBER OF GROUPS!')
                print('Press Enter to go back')
                input()

        elif ipt.upper()==one_main.upper() or (ipt=='1' and one_main!=''):
            logcheck(usr_noclr,one_main)
            c+=1

        elif ipt.upper()==two_main.upper() or (ipt=='2' and two_main!=''):
            logcheck(usr_noclr,two_main)
            c+=1

        elif ipt.upper()==three_main.upper() or (ipt=='3' and three_main!=''):
            logcheck(usr_noclr,three_main)
            c+=1

        elif ipt.upper()==four_main.upper() or (ipt=='4' and four_main!=''):
            logcheck(usr_noclr,four_main)
            c+=1

        elif ipt.upper()==five_main.upper() or (ipt=='5' and five_main!=''):
            logcheck(usr_noclr,five_main)
            c+=1

        elif ipt.upper()=='/D':
            rec_name=input('Enter the Name of the Mainframe to Delete: ')

            if rec_name==one_main and access_one.upper()=='ADMIN':
                code=one_code
                name=one_main         
            elif rec_name==two_main and access_two.upper()=='ADMIN':
                code=two_code
                name=two_main
            elif rec_name==three_main and access_three.upper()=='ADMIN':
                code=three_code
                name=three_main
            elif rec_name==four_main and access_four.upper()=='ADMIN':
                code=four_code
                name=four_main
            elif rec_name==five_main and access_five.upper()=='ADMIN':
                code=five_code
                name=five_main
            else:
                print('No such Mainframe found or you dont have the authority to delete')
                print('Press Enter to go back')
                input()
                # Re-opening Mainframe View
                mainframeview(usr)

            # Reading Records
            del_rec=open('Mainframes/Mainframe.csv', 'r')
            del_rec_reader=csv.reader(del_rec)
            records=[]
            for k in del_rec_reader:
                if k[0]==code and k[1]==name:
                    print()
                else:
                    rec=[k[0],k[1],k[2],k[3]]
                    records.append(rec)
            del_rec.close()

            # Deleting Records
            del_rec=open('Mainframes/Mainframe.csv', 'w', newline='')
            del_rec_writer=csv.writer(del_rec)
            del_rec_writer.writerows(records)
            del_rec.close()
            
            # Deleting folder
            remmove='Mainframes/'+code+' '+name+' '+'Mainframe'
            shutil.rmtree(remmove)

            # Re-opening Mainframe View
            mainframeview(usr)

        elif ipt.upper()=='/R':
            rec_name=input('Enter the Name of the Mainframe to Delete: ')

            # Reading Records
            del_rec=open('Mainframes/Mainframe.csv', 'r')
            del_rec_reader=csv.reader(del_rec)
            records=[]
            for k in del_rec_reader:
                if k[0]==code and k[1]==rec_name:
                    print()
                else:
                    rec=[k[0],k[1],k[2],k[3]]
                    records.append(rec)
            del_rec.close()
            
            # Deleting Records
            del_rec=open('Mainframes/Mainframe.csv', 'w', newline='')
            del_rec_writer=csv.writer(del_rec)
            del_rec_writer.writerows(records)
            del_rec.close()

            # Re-opening Mainframe View
            mainframeview(usr)

        else:
            centeral_main_input(ipt)

        if c>0:
            clear()
            mainpro(cnp)

# * MAIN GROUP VIEW TEMPLATE
def mainpro(chk_n):
    global check_num
    check_num=chk_n
    
    global run_once
    run_once = False
    while True:
        if run_once==False:
            verification_0(chk_n)
            run_once=True
        m_path='Server/Main Files/Userdata/'+us+' Inbox.dat'
        s_path='Client/Userdata/'+us+' Sent.dat'
        if not os.path.isfile(m_path):
            mail_open=open(m_path, 'wb')
            pickle.dump([''],mail_open)
            mail_open.close()
        if not os.path.isfile(s_path):
            mail_open=open(s_path, 'wb')
            pickle.dump([''],mail_open)
            mail_open.close()
        clear()
        # Main Program
        global lister_1
        lister_1 = {}
        end_main='Use ''+'' to add folders and use ''/d'' to delete a folder'
        hy=' - '
        files_button=Fore.LIGHTWHITE_EX+'-Groups'+clr_main
        out_folder_1=out_folder_2=out_folder_3=out_folder_4=out_folder_5='+'
        folder_1=folder_2=folder_3=folder_4=folder_5=''
        fldr_chk=0
        count=1
        fldr_lst=os.listdir('Server/'+rec_num+' '+name_of_main+' Mainframe/Folders')
        for k in fldr_lst:
            try:
                if fldr_chk==0:
                    folder_1=k
                    out_folder_1='1.'+k
                    fldr_chk+=1
                elif fldr_chk==1:
                    folder_2=k
                    out_folder_2='2.'+k
                    fldr_chk+=1
                elif fldr_chk==2:
                    folder_3=k
                    out_folder_3='3.'+k
                    fldr_chk+=1
                elif fldr_chk==3:
                    folder_4=k
                    out_folder_4='4.'+k
                    fldr_chk+=1
                elif fldr_chk==4:
                    folder_5=k
                    out_folder_5='5.'+k
                    fldr_chk+=1
            except:
                print()
        grps=Fore.MAGENTA+'Groups'+Fore.RESET
        settings='6.Group Settings'
        mainstr=f'''
    {clr_main}
   =============================================================================
    {clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{clr_main}
   =============================================================================
   │   COLUMN    │ {main_str}    {test_ver}
   │-------------│---------------------------------------------------------------
   │  -{grps}    │   {out_folder_1}
   │-------------│
   │  -Contracts │   {out_folder_2}
   │-------------│
   │  -Mail      │   {out_folder_3}
   │-------------│
   │  -Settings  │   {out_folder_4}
   │-------------│
   │  -Profile   │   {out_folder_5}
   │-------------│
   │  -Chats     │   
   │-------------│   {settings} 
   │  -Players   │   {end_main}
   =============================================================================
       {Fore.RESET} '''
        print(mainstr)

        ipt=input('=> ')

        if ipt=='':
            ipt=ipt+'.'
        if ipt=='+':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                fldr_tr=True
                fldrs=os.listdir('Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/')
                while fldr_tr:
                    c=0
                    fr=csv.reader(fldrs)
                    fldr_ipt=input('Enter a new folder name: ')
                    for k in fr:
                        if fldr_ipt==k:
                            c+=1
                    if c>0:
                        print('Please enter a new folder name, this folder already exists!')
                    else:
                        fldr_tr=False
                fldr_set=open('Server/'+rec_num+' '+name_of_main+' Mainframe/'+rec_num+' '+name_of_main+' Mainframe Folder Setings.csv', 'a',newline='')
                fldr_set.close()
                os.makedirs('Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+fldr_ipt.upper())
                first_folder = os.listdir('Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+fldr_ipt.upper())
                und_count_1 = 1
                lister_1 = {}
                for k in first_folder:
                    lister_1[und_count_1] = k
                    und_count_1+=1
                under_fold_1(und_count_1-1,fldr_ipt)
            else:
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()
            mainframeview(us)
        elif ipt=='6' or ipt.upper()=='GROUP SETTINGS':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                setting_function()
            else:
                print(access)
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()

            mail(check_num)
        elif ipt.upper()==folder_1.upper() or ipt=='1':
            lister_1 = {}
            path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_1
            print(path)
            if os.path.isdir(path):
                print('test 2')
                first_folder = os.listdir(path)
                for k in first_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_1)           
        elif ipt.upper()==folder_2.upper() or ipt=='2':
            lister_1 = {}
            path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_2
            if os.path.isdir(path)==True:
                second_folder = os.listdir()
                for k in second_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_2)
        elif ipt.upper()==folder_3.upper() or ipt=='3':
            lister_1 = {}
            path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_3
            if os.path.isdir(path)==True:
                third_folder = os.listdir(path)
                for k in third_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_3)
        elif ipt.upper()==folder_4.upper() or ipt=='4':
            lister_1 = {}
            path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_4
            if os.path.isdir(path)==True:
                fourth_folder = os.listdir(path)
                for k in fourth_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_4)
        elif ipt.upper()==folder_5.upper() or ipt=='5':
            lister_1 = {}
            path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_5
            if os.path.isdir(path)==True:
                fifth_folder = os.listdir(path)
                for k in fifth_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_5)
            quit(chk_n)
        elif ipt.upper()=='/D':
                if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                    print('========================================')
                    print('Please enter the number of the folder that you would like to delete:')
                    num=1
                    for k in fldr_lst:
                        print(str(num)+')', k)
                        if num==1:
                            frst=k
                        elif num==2:
                            scnd=k
                        elif num==3:
                            thrd=k
                        elif num==4:
                            frth=k
                        elif num==5:
                            ffth=k
                        num+=1
                    ipt=input('=> ')
                    if ipt=='1':
                        path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst
                    elif ipt==2:
                        path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+scnd
                    elif ipt==3:
                        path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+thrd
                    elif ipt==4:
                        path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frth
                    elif ipt==5:
                        path='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+ffth
                    os.rmdir(path)
                    print('SUCCESSFULLY DELETED!')
                    print('Press Enter to go back ')
                    input()
                else:
                    print('You dont have enough Clearance!')
                    print('Press Enter to go back ')
                    input()
        elif ipt.upper()=='UPDATE' or ipt.upper()=='ROLES' or ipt.upper()=='UP':
            if access.upper()=='ADMIN':
                print('=========================================================')
                print('Enter the name of the User you want to promote/demote')
                fout=open('Server/Mainframe.csv', 'r')
                fr=csv.reader(fout)
                confir=True
                ch=0
                while confir:
                    records=[]
                    usern=input('=> ')
                    for k in fr:
                        if k[1]==name_of_main and k[0]==rec_num and k[2]==usern:
                            confir=False
                            ch=1
                        else:
                            records.append(k)
                    if ch==0:
                        yn=True
                        while yn:
                            print('This Person does not belong in your Mainframe')
                            print('Do you want to go back home?')
                            print('YES [Y]---------NO [N]')
                            fq=input('=> ')
                            if fq.upper()=='Y' or fq.upper()=='YES':
                                mainpro(check_num)
                            elif fq.upper()=='N' or fq.upper()=='NO':
                                yn=False
                            
                            
                print()
                print('-------------------')
                print(Fore.RED+'Enter the new Access granted to the person')
                print(Fore.BLUE + 'Normal','      ', Fore.YELLOW+'Manager','      ',Fore.RED+'Admin' ,Fore.RESET)
                print()
                new_acc=input('=> ')
                acc_con=True
                while acc_con:
                    if new_acc.upper()=='ADMIN':
                        rec=[rec_num,name_of_main,usern,new_acc]
                        records.append(rec)
                        acc_con=False
                    elif new_acc.upper()=='MANAGER':
                        rec=[rec_num,name_of_main,usern,new_acc]
                        records.append(rec)
                        acc_con=False
                    elif new_acc.upper()=='NORMAL':
                        rec=[rec_num,name_of_main,usern,new_acc]
                        records.append(rec)
                        acc_con=False
                print('RECORDS UPDATED!')
            else:
                print('Access denied, You dont have admin Access')
        elif ipt.upper()=='RETURN' or ipt=='-':
            mainframeview(us)
        elif ipt.upper()=='LIST' or ipt.upper()=='/L':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                fout=open('Server/Mainframe.csv', 'r')
                fr=csv.reader(fout)
                adm=man=norm=name=[]
                print('========================================')
                print('USERS IN THE GROUP')
                print('========================================')
                for k in fr:
                    if k[0]==rec_num and k[1]==name_of_main:
                        if k[3].upper()=='ADMIN':
                            adm.append([k[2],k[3]])
                            print(Fore.RED+k[2], '('+k[3]+')')
                        elif k[3].upper()=='MANAGER':
                            man.append([k[2],k[3]])
                            print(Fore.YELLOW+k[2], '('+k[3]+')')
                        elif k[3].upper()=='NORMAL':
                            norm.append([k[2],k[3]])
                            print(Fore.BLUE+k[2], '('+k[3]+')')
                        name.append([k[2],k[3]])
                print(Fore.RESET)
                print('========================================')
                print('1) Sort on Access')
                print('2) Sort on Name')
                print('0) BACK')

                r=int(input('=> '))
                if r==1:
                    try:
                        print(Fore.RESET)
                        print('===================================')
                        print('Users sorted on Roles')
                        print('===================================')
                        c1=c2=c3=''
                        for k in adm:
                            if k[1].upper()=='ADMIN' and k[0]!=c1:
                                print(Fore.RED+k[0], '(ADMIN)')
                                c1=k[0]
                        for k in man:
                            if k[1].upper()=='MANAGER' and k[0]!=c2:
                                print(Fore.YELLOW+k[0], '(MANAGER)')
                                c2=k[0]
                        for k in norm:
                            if k[1].upper()=='NORMAL' and k[0]!=c3:
                                print(Fore.BLUE+k[0], '(NORMAL)')
                                c3=k[0]
                        print(Fore.RESET)
                    except:
                        print()
                    print('PRESS ENTER TO GO BACK!')
                    input()

                elif r==2:
                    new_name=[]
                    c1=' '
                    for k in name:
                        if c1!=k[0]:
                            new_name.append(k)
                            c1=k[0]
                    new_name=sorted(new_name)
                    print(Fore.RESET)
                    print('===================================')
                    print('Users sorted on Name')
                    print('===================================')
                    for k in new_name:
                        print(k[0], '('+k[1]+')')
                        c1=k[0]
                    print(Fore.RESET)
                    print('PRESS ENTER TO GO BACK!')
                    input()
                
                else:
                    print()
            else:
                print('You do not have enough access')
                print('Press Enter to go back')
                input()
            contracts()
        else:
            centeral_main_input(ipt)

# * GROUP ADMIN SETTING FUNCTION
def setting_function():
    clear() 
    set_title= 'GROUP SETTINGS'
    grps=Fore.MAGENTA+'Groups'+Fore.RESET
    invite_str='1.Invite'
    hy = ' - '
    leave_str='0.Back to Datasite'
    setstr=f'''
    {clr_main}
   =============================================================================
    {clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{clr_main}
   =============================================================================
   │  COLUMN    │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ -{grps}    │
   │------------│   {set_title}
   │ -Contracts │
   │------------│       {invite_str}
   │ -Mail      │
   │------------│       {leave_str}
   │ -Settings  │
   │------------│
   │ -Profile   │
   │------------│
   │ -Chats     │
   │------------│
   │ -Players   │
   =============================================================================
        '''
    print(setstr)

    set_inpt=input('=>')

    if set_inpt=='1':
        clear()
        print('======================================================================')
        print(Fore.RED+'Enter the Username you want to Invite')
        print(Fore.RESET)
        invite_user=input('Username: ')
        print('-------------------')
        print(Fore.RED+'Enter the Access granted to the person')
        print(Fore.BLUE + 'Normal','      ', Fore.YELLOW+'Manager','      ',Fore.RED+'Admin' ,Fore.RESET)
        print()
        invite_user_access=input('Access: ')
        pass_file=open("Server/Main Files/Password.csv",'r')
        fr=csv.reader(pass_file)
        sno=1
        inv_int=usrt_nex=suc=0
        for k in fr:
            if invite_user==k[0]:
                suc+=1
                path='Server/Main Files/Userdata/'+k[0]+' Inbox.dat'
                if os.path.isfile(path)==False:
                    snd_invte_mail=open('Server/Main Files/Userdata/'+k[0]+' Inbox.dat', 'ab')
                    snd_invte_mail.close()
                snd_invte_mail=open('Server/Main Files/Userdata/'+k[0]+' Inbox.dat', 'rb')
                while True:
                    try:
                        inv_mail_read=pickle.load(snd_invte_mail)
                        sno+=1
                    except:
                        sno=1
                        break
                snd_invte_mail.close()
                
                snd_invte_mail=open('Server/Main Files/Userdata/'+k[0]+' Inbox.dat', 'ab')
                msg='You have been invited to join '+name_of_main+' as the role of '+invite_user_access
                rec=[sno,'Invitation',msg,'Invite',us,name_of_main,invite_user_access]
                pickle.dump(rec,snd_invte_mail)
                print('Sending.....')
                print('==================')
                snd_invte_mail.close()
                print('Mail sent!')
                print('Press Enter to go back')
                input()
            
            elif invite_user==us:
                inv_int+=1

            elif invite_user!=k[0]:
                usrt_nex+=1
        
        if suc==0:
            if inv_int>0:
                print('You cannot send an invite to yourself')
            elif usrt_nex>0:
                print('Such a username does not exist in the Database. Check the username spelling')
            print('Press Enter to go back')
            input()

        pass_file.close()
        print('----------------------------')

    else:
        centeral_main_input(set_inpt)

# * USER PROFILE TEMPLATE
def user_settings(chk):
    verify_us_ch(chk)
    while True:
        fdp=open('userdata.csv', 'r')
        fr_pl=csv.reader(fdp)
        for k in fr_pl:
            if k[0]==us:
                c_rec=k
        sp_n=us.split()
        f_name=sp_n[0]
        l_name=sp_n[1]
        acc_no=c_rec[1]
        fact=c_rec[3]
        gen=c_rec[4]
        prof=c_rec[5]
        clear()
        settin=Fore.MAGENTA+'Settings'+Fore.RESET
        warn=Fore.RED+'UNDERSTAND THAT YOU WILL BE LOGGED OUT IMMEDIATLY!'+Fore.RESET
        warn_1=Fore.RED+'THIS IS IRREVERSIBLE'+Fore.RESET
        mainstr=f'''
    =============================================================================
     USER PROFILE
    =============================================================================
    │   COLUMN    │
    │-------------│ First Name: {Fore.LIGHTBLUE_EX}{f_name}{Fore.RESET}
    │  -Groups    │ Last Name: {Fore.LIGHTBLUE_EX}{l_name}{Fore.RESET}
    │-------------│ Account Number: {Fore.LIGHTBLUE_EX}{acc_no}{Fore.RESET}
    │  -Contracts │ Gender: {Fore.LIGHTBLUE_EX}{gen}{Fore.RESET}
    │-------------│
    │  -Mail      │ Faction Joined: {Fore.LIGHTBLUE_EX}{fact}{Fore.RESET}
    │-------------│
    │  -{settin}  │ Denomination: X$
    │-------------│
    │  -Profile   │ Occuptation: {Fore.LIGHTBLUE_EX}{prof}{Fore.RESET}
    │-------------│
    │  -Chats     │------------------│--------------------│
    │-------------│  Delete Account  │   Urgent Removal   │
    │  -Players   │     (DELETE)     │      (REMOVE)      │
    =============================================================================
'''
        print(mainstr)

        set_ipt=input('=> ')

        if set_ipt.upper()=='PASSWORD' or set_ipt.upper()=='1':
            fout=open('Server/Main Files/Password.csv','r')
            pass_read=csv.reader(fout)
            old_pass_b=True
            while old_pass_b:
                passing_chker=False
                old_pass=input('Old Password: ')
                for k in pass_read:
                    final_pass=hashcust(us,old_pass)
                    if us==k[0] and final_pass==k[1]:
                        old_pass_b=False
                        passing_chker=True
                if passing_chker==False:
                    print('You have typed your password wrong, Please try again')
            new_pass_b=True
            while new_pass_b:
                record=[]
                new_pass=input('New Password: ')
                new_pass_re=input('Repeat new Password: ')
                if new_pass==new_pass_re:
                    final_pass_2=hashcust(us,new_pass)
                    for k in pass_read:
                        if us==k[0] and final_pass==k[1]:
                            rec=[k[0],final_pass_2]
                            record.append(rec)
                        else:
                            rec=[k[0],k[1]]
                            record.append(rec)
                    fout.close()
                    fout_1=open('Files/Password.csv','w', newline='')
                    pass_write=csv.writer(fout_1)
                    pass_write.writerows(record)
                    new_pass_b=False
                else:
                    print('Your new password and Old Password are not Matching!')

        elif set_ipt.upper()=='DELETE' or set_ipt.upper()=='2':
            print('==================================')
            print('Are you sure? This will result in all of your data being discarded')
            print('Also Understand that deleting your account will result in all Groups')
            print('without an Admin (Other than you) being deleted, Do you Understand?')
            print('YES [Y] ---- NO [N]')
            sure=input('=> ')
            if sure.upper()=='YES' or sure.upper()=='Y':
                # Password deleter
                record=[]
                fout=open('Server/Main Files/Password.csv','r')
                chk_read=csv.reader(fout)
                for k in chk_read:
                    if us!=k[0]:
                        record.append(k)
                fout.close()
                fout=open('Server/Main Files/Password.csv','w',newline='')
                chk_write=csv.writer(fout)
                chk_write.writerows(record)
                fout.close()

                # Mainframe record deleter
                # We take out ALL the groups our user is an Admin in
                main_name_rec=[]
                admin_rec=[]
                fout=open('Server/Mainframe.csv','r')
                chk_read=csv.reader(fout)
                for k in chk_read:
                    if k[2]!=us:
                        main_name_rec.append(k)
                    elif k[2]==us and k[3].upper()=='ADMIN':
                        admin_rec.append(k)
                fout.close()

                fout=open('Server/Mainframe.csv','w', newline='')
                chk_write=csv.writer(fout)
                chk_write.writerows(main_name_rec)
                fout.close()

                # Mainframe record reader
                # We take out ALL the groups our user is an Admin in
                fout=open('Server/Mainframe.csv','r')
                chk_read=csv.reader(fout)
                final_rec=[]
                for k in chk_read:
                    reader=False
                    for i in admin_rec:
                        if k[0]==i[0] and k[1]==i[1] and k[2]!=i[2] and k[3].upper()=='ADMIN':
                            reader=True
                        elif k[0]==i[0] and k[1]==i[1] and k[2]==i[2] and k[3].upper()=='ADMIN':
                            main_remove='Server/'+k[0]+' '+k[1]+' Mainframe'
                            shutil.rmtree(main_remove)

                    if reader==False:
                        final_rec.append(k)
                fout.close()

                # Final edition
                fout=open('Server/Main Files/Password.csv','w',newline='')
                chk_write=csv.writer(fout)
                chk_write.writerows(final_rec)
                fout.close()
                
                quit(chk)

        elif set_ipt.upper()=='BACK' or set_ipt=='0':
            mainpro(chk)

        elif set_ipt.upper()=='HELP' or set_ipt=='?':
            help(us)

        elif set_ipt.upper()=='GROUPS':
            mainframeview(us)
        
        elif set_ipt.upper()=='MAIL':
            mail(check_num)
       
        elif set_ipt.upper()=='PLAYERS' or set_ipt.upper()=='PLAYER':
            user_read()
        
        elif set_ipt.upper()=='CONTRACTS' or set_ipt.upper()=='CONTRACT':
            contracts()

# * BLAND MAIL TEMPLATE
# ? MAKE IT LOOK INTERESTING
def mail(check_num_1):
    global check_num
    check_num=check_num_1
    verify(check_num_1)
    ml=Fore.MAGENTA+'Mail'+Fore.RESET
    while True:
        clear()
        main_mail_str=f'''
       =============================================================================
        {Fore.BLUE}{us}{Fore.RESET}
       =============================================================================
       │  COLUMN    │ {main_str}    {test_ver}
       │------------│---------------------------------------------------------------
       │ -Groups    │         │
       │            │         │
       │ -Contracts │         │
       │            │         │
       │ -Groups    │         │
       │            │• Inbox  │
       │ -{ml}      │         │
       │            │         │
       │ -Settings  │• Send   │
       │            │         │
       │ -Profile   │         │ 
       │            │         │
       │ -Chats     │         │
       │            │         │
       │ -Players   │         │
       =============================================================================
        '''
        print(main_mail_str)
        set_inpt=input('=>')
        if set_inpt.upper()=='INBOX':
            inbox()

        elif set_inpt.upper()=='SEND':
            send()

        else:
            centeral_main_input(set_inpt)

# * USER INBOX
# TODO / HAVE PAGE TRANSFER, MORE LINES FOR TEXT AND BETTER UI
# ? ADD CUSTOMIZATION
def inbox():
    clear()
    # Inbox
    try:
        mail_path='Server/Main Files/Userdata/'+us+' Inbox.dat'
        if os.path.isfile(mail_path)==True:
            mail_open=open(mail_path, 'rb')
            mail_read_elem=pickle.load(mail_open)
        else:
            mail_open=open(mail_path, 'wb')
            mail_open.close()
            mail_open=open(mail_path, 'rb')
            mail_read_elem=pickle.load(mail_open)
    except:
        print()

    record_new=[]
    mail_read_elem=[]
    while True:
        try:
            mail_read_elem=pickle.load(mail_open)
            record_new.append(mail_read_elem)
        except:
            break
    

    # We now go into the: The Spacer Problem

    # Defining Varables for later use
    sno=0
    last_del=False
    dict_mail={}
    test_title_plachld1=test_title_plachld2=test_title_plachld3=test_title_plachld4=test_title_plachld5=test_title_plachld6=test_title_plachld7=test_title_plachld8=''
    by_placehld1=by_placehld2=by_placehld3=by_placehld4=by_placehld5=by_placehld6=by_placehld7=by_placehld8=''
    gap_leng1=gap_leng2=gap_leng3=gap_leng4=gap_leng5=gap_leng6=gap_leng7=gap_leng8=' '*25
    g1=g2=g3=g4=g5=g6=g7=g8=' '*25

    try:
        for k in record_new:
            if sno==0:
                # First Mail
                sno+=1
                test_title_plachld1=k[1]
                g1=' '*(25-len(test_title_plachld1))
                by_placehld1='By:'+k[4]
                gap_leng1=' '*(25-len(by_placehld1))
                dict_mail[str(sno)]=k
            elif sno==1:
                # Second Mail
                sno+=1
                test_title_plachld2=k[1]
                g2=' '*(25-len(test_title_plachld2))
                by_placehld2='By:'+k[4]
                gap_leng2=' '*(25-len(by_placehld2))
                dict_mail[str(sno)]=k
            elif sno==2:
                # Third Mail
                sno+=1
                test_title_plachld3=k[1]
                g3=' '*(25-len(test_title_plachld3))
                by_placehld3='By:'+k[4]
                gap_leng3=' '*(25-len(by_placehld3))
                dict_mail[str(sno)]=k
            elif sno==3:
                # Fourth Mail
                sno+=1
                test_title_plachld4=k[1]
                g4=' '*(25-len(test_title_plachld4))
                by_placehld4='By:'+k[4]
                gap_leng4=' '*(25-len(by_placehld4))
                dict_mail[str(sno)]=k
            elif sno==4:
                # Fifth Mail
                sno+=1
                test_title_plachld5=k[1]
                g5=' '*(25-len(test_title_plachld5))
                by_placehld5='By:'+k[4]
                gap_leng5=' '*(25-len(by_placehld5))
                dict_mail[str(sno)]=k
            elif sno==5:
                # Sixth Mail
                sno+=1
                test_title_plachld6=k[1]
                g6=' '*(25-len(test_title_plachld6))
                by_placehld6='By:'+k[4]
                gap_leng6=' '*(25-len(by_placehld6))
                dict_mail[str(sno)]=k
            elif sno==6:
                # Seventh Mail
                sno+=1
                test_title_plachld7=k[1]
                g7=' '*(25-len(test_title_plachld7))
                by_placehld7='By:'+k[4]
                gap_leng7=' '*(25-len(by_placehld7))
                dict_mail[str(sno)]=k
            elif sno==7:
                # Eighth Mail
                sno+=1
                test_title_plachld8=k[1]
                g8=' '*(25-len(test_title_plachld8))
                by_placehld8='By:'+k[4]
                gap_leng8=' '*(25-len(by_placehld8))
                dict_mail[str(sno)]=k

    
    except:
        print()
    # Now that we have solved the Spacer Problem, We apply  it to this code down here

    # Making sure to delete the oldest Mail since we only have 8 slots
    if last_del==True:
        inbox_mail_file=open(mail_path, 'rb')  
        record_new=[]
        while True:
            try:
                inbox_mail_file_elem=pickle.load(inbox_mail_file)
                for k in inbox_mail_file_elem:
                    record_new.append(k)
            except:
                break
        f_chk=0
        records=[]
        for k in record_new:
            if f_chk==0:
                f_chk+=1
            else:
                if len(k)==7:
                    rec=[sno,k[1],k[2],k[3],k[4],k[5],k[6]]
                    records.append(rec)
                elif len(k)==5:
                    rec=[sno,k[1],k[2],k[3],k[4]]
                    records.append(rec)
        inbox_mail_file.close()
    
        inbox_mail_file=open(mail_path, 'wb')   
        pickle.dump(records,inbox_mail_file)
        inbox_mail_file.close()
        last_del=False
        inbox()

    mail_open.close() 
    ml=Fore.MAGENTA+'Mail'+Fore.RESET
    inb=Fore.MAGENTA+'Inbox'+Fore.RESET
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    mainstr=f'''
   =============================================================================
    {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
   =============================================================================
   │  COLUMN    │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ -Groups    │         │1.                       │2.
   │------------│         │{test_title_plachld1}{g1}│{test_title_plachld2}{g2}
   │ -Contracts │         │{by_placehld1}{gap_leng1}│{by_placehld2}{gap_leng2}
   │------------│         │=====================================================
   │ -{ml}      │         │3.                       │4.
   │------------│• {inb}  │{test_title_plachld3}{g3}│{test_title_plachld4}{g4}
   │ -Settings  │         │{by_placehld3}{gap_leng3}│{by_placehld4}{gap_leng4}
   │------------│         │=====================================================
   │ -Profile   │• Send   │5.                       │6.
   │------------│         │{test_title_plachld5}{g5}│{test_title_plachld6}{g6}
   │ -Chats     │         │{by_placehld5}{gap_leng5}│{by_placehld6}{gap_leng6}
   │------------│         │=====================================================
   │ -Players   │         │7.                       │8.
   │------------│         │{test_title_plachld7}{g7}│{test_title_plachld8}{g8}
   │------------│         │{by_placehld7}{gap_leng7}│{by_placehld8}{gap_leng8}
   =============================================================================
    '''
    print(mainstr)
    mail_open_inpt=input('=>')
    global applied_var_k

    if mail_open_inpt=='1':
        try:
            applied_var_k=dict_mail['1']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='2':
        try:
            applied_var_k=dict_mail['2']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='3':
        try:
            applied_var_k=dict_mail['3']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='4':
        try:
            applied_var_k=dict_mail['4']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='5':
        try:
            applied_var_k=dict_mail['5']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='6':
        try:
            applied_var_k=dict_mail['6']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='7':
        try:
            applied_var_k=dict_mail['7']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif mail_open_inpt=='8':
        try:
            applied_var_k=dict_mail['8']
            if applied_var_k[3]=='Invite':
                invite_mail_temp()
            elif applied_var_k[3]=='Mail':
                normal_mail_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    else:
        centeral_main_input(mail_open_inpt)

# ! TRY TO COMBINE ALL THE MAIL TEMPLATES INTO ONE FOR BETTER DEBUGGING
# * GROUP INVITE MAIL INBOX TEMPLATE
def invite_mail_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    while True:
        invite_mail_str=f'''
        =============================================================================
        {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
        =============================================================================
        │  COLUMN    │ {main_str}    {test_ver}
        │------------│---------------------------------------------------------------
        │ -Groups    │         │
        │------------│         │ Invitation to join {applied_var_k[5]}
        │ -Contracts │         │ As: {applied_var_k[6]}
        │------------│         │ From:{applied_var_k[4]}
        │ -Mail      │         │
        │------------│• Inbox  │ 
        │ -Settings  │         │ {applied_var_k[2]}        
        │------------│         │ 
        │ -Profile   │• Send   │ 
        │------------│         │--------------------------------
        │ -Chats     │         │ 
        │------------│         │ Type in [YES] or [Y] to accept
        │ -Players   │         │ 
        │------------│         │ Type in [NO] or [N] to decline/Accept later
        │------------│         │
        │------------│         │ Type in Return or '-' to go back to inbox
        =============================================================================
            '''
        print(invite_mail_str)
        acc_rej_ipt=input('=>')

        if acc_rej_ipt.upper()=='Y' or acc_rej_ipt.upper()=='YES':
            dup_rec=0
            # Reading file to check Mainframe number
            read_main_data=open('Server/Mainframe.csv', 'r')
            fr=csv.reader(read_main_data)
            # Finding the chk number using this method
            for k in fr:
                if applied_var_k[5]==k[1]:
                    chk_num=k[0]
            read_main_data.close()
            rec=[str(chk_num),applied_var_k[5],us,applied_var_k[6]]
            # Reading file for possible duplications
            read_main_data=open('Server/Mainframe.csv', 'r')
            fr=csv.reader(read_main_data)
            for k in fr:
                if k==rec:
                    dup_rec=1

            if dup_rec==0:
                # Updating file to add a new user to the mainframe
                update_main_data=open('Server/Mainframe.csv', 'a',newline='')
                fw=csv.writer(update_main_data)
                fw.writerow(rec)
                update_main_data.close()
                # Print response
                print('============================================================================')
                print('Invitation Accepted!')
                print('Press Enter to go back')
                input()
                inbox()
            elif dup_rec==1:
                print('============================================================================')
                print('YOU ARE ALREADY A PART OF IT!')
                print('Press Enter to Go back......')
                input('=> ')
                inbox()

        elif acc_rej_ipt.upper()=='N' or acc_rej_ipt.upper()=='NO':
            inbox()

        elif acc_rej_ipt.upper()=='X':
            quit(check_num)

        elif acc_rej_ipt()=='RETURN' or acc_rej_ipt=='-':
            inbox()

# * NORMAL MAIL INBOX TEMPLATE
def normal_mail_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    while True:
        invite_mail_str=f'''
   =============================================================================
   {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
   =============================================================================
   │  COLUMN    │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ -Groups    │         │
   │------------│         │
   │ -Contracts │         │ Title:{applied_var_j[1]}
   │------------│         │ 
   │ -Mail      │         │
   │------------│• Inbox  │ {applied_var_j[2]}
   │ -Settings  │         │      
   │------------│         │
   │ -Profile   │• Send   │ 
   │------------│         │
   │ -Chats     │         │ 
   │------------│         │
   │ -Players   │         │ From:{applied_var_j[4]}
   │------------│         │
   │------------│         │
   =============================================================================
    '''
        print(invite_mail_str)
        print('Press Enter to go back to Mail')
        enter_ipt=input('=>')
        if enter_ipt.upper()=='X':
            quit(check_num)
        else:
            inbox()

# * USER OUTBOX
def send():
    clear()
    # Outbox
    path_chker_mailid='Client/Userdata/'+us+' Sent.dat'
    if os.path.isfile(path_chker_mailid)==False:
        sent_mail_file=open(path_chker_mailid, 'ab')
        sent_mail_file.close()
    
    record_new=[]
    sent_mail_file=open(path_chker_mailid, 'rb')
    record_new=[]
    sent_mail_file_elem=[]
    while True:    
        try:
            sent_mail_file_elem=pickle.load(sent_mail_file)
            record_new.append(sent_mail_file_elem)
        except:
            break

    # Defining Varables for later use
    last_del=False
    sno=0
    dict_mail={}
    test_title_plachld1=test_title_plachld2=test_title_plachld3=test_title_plachld4=test_title_plachld5=test_title_plachld6=test_title_plachld7=test_title_plachld8=''
    by_placehld1=by_placehld2=by_placehld3=by_placehld4=by_placehld5=by_placehld6=by_placehld7=by_placehld8=''
    try:
        for k in record_new:
            if sno==0:
                # First Mail
                sno+=1
                test_title_plachld1=k[1]
                by_placehld1='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==1:
                # Second Mail
                sno+=1
                test_title_plachld2=k[1]
                by_placehld2='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==2:
                # Third Mail
                sno+=1
                test_title_plachld3=k[1]
                by_placehld3='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==3:
                # Fourth Mail
                sno+=1
                test_title_plachld4=k[1]
                by_placehld4='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==4:
                # Fifth Mail
                sno+=1
                test_title_plachld5=k[1]
                by_placehld5='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==5:
                # Sixth Mail
                sno+=1
                test_title_plachld6=k[1]
                by_placehld6='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==6:
                # Seventh Mail
                sno+=1
                test_title_plachld7=k[1]
                by_placehld7='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==7:
                # Eighth Mail
                sno+=1
                test_title_plachld8=k[1]
                by_placehld8='To:'+k[4]
                dict_mail[str(sno)]=k
            elif sno==8:
                last_del=True
                sent_mail_file.close()

    except:
        print()

    if last_del==True:
        sent_mail_file=open(path_chker_mailid, 'rb')   
        while True:
            try:
                sent_mail_file_elem=pickle.load(sent_mail_file)
                for k in sent_mail_file_elem:
                    record_new.append(k)
            except:
                break
        f_chk=0
        records=[]
        for k in record_new:
            if f_chk==0:
                f_chk+=1
            else:
                if len(k)==7:
                    rec=[sno,k[1],k[2],k[3],k[4],k[5],k[6]]
                    records.append(rec)
                elif len(k)==5:
                    rec=[sno,k[1],k[2],k[3],k[4]]
                    records.append(rec)
        sent_mail_file.close()
    
        sent_mail_file=open(path_chker_mailid, 'wb')   
        pickle.dump(records,sent_mail_file)
        sent_mail_file.close()
        last_del=False
        send()

    ml=Fore.MAGENTA+'Mail'+Fore.RESET
    sn=Fore.MAGENTA+'Inbox'+Fore.RESET
    mail=Fore.LIGHTWHITE_EX+'-Mail'
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    main_mail_str=f'''
   =============================================================================
    {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
   =============================================================================
   │   COLUMN   │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ -Groups    │         │ 1.{test_title_plachld1} │ {by_placehld1}                
   │------------│         │-----------------------------------------------------
   │ -Contracts │         │ 2.{test_title_plachld2} │ {by_placehld2}     
   │------------│         │-----------------------------------------------------
   │ -{ml}      │         │ 3.{test_title_plachld3} │ {by_placehld3}    
   │------------│• Inbox  │-----------------------------------------------------
   │ -Settings  │         │ 4.{test_title_plachld4} │ {by_placehld4}    
   │------------│         │-----------------------------------------------------
   │ -Profile   │• {sn}   │ 5.{test_title_plachld5} │ {by_placehld5}    
   │------------│         │-----------------------------------------------------
   │ -Chats     │         │ 6.{test_title_plachld6} │ {by_placehld6}    
   │------------│         │-----------------------------------------------------
   │ -Players   │         │ 7.{test_title_plachld7} │ {by_placehld7}    
   │------------│         │-----------------------------------------------------
   │------------│         │ 8.{test_title_plachld8} │ {by_placehld8}    
   │------------│         │-----------------------------------------------------
   │------------│         │ '+' Compose  │
    ============================================================================{Fore.RESET}
    '''
    print(main_mail_str)

    outbox_ipt=input('=>')
    global applied_var_j

    if outbox_ipt=='1':
        try:
            applied_var_j=dict_mail['1']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='2':
        try:
            applied_var_j=dict_mail['2']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='3':
        try:
            applied_var_j=dict_mail['3']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='4':
        try:
            applied_var_j=dict_mail['4']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='5':
        try:
            applied_var_j=dict_mail['5']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='6':
        try:
            applied_var_j=dict_mail['6']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='7':
        try:
            applied_var_j=dict_mail['7']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()

    elif outbox_ipt=='8':
        try:
            applied_var_j=dict_mail['8']
            if applied_var_j[3]=='Mail':
                normal_outbox_temp()
        except:
            print('No mail exists in Slot')
            print('Press Enter to go back')
            input()
        
    elif outbox_ipt=='+':
        clear()
        title_fix=content=True
        print('======================================================================')
        print(Fore.RED+'Enter All the information needed to Send a Mail')
        print(Fore.RESET)
        send_user_name=input('Enter Username of the Person: ')
        while title_fix:
            send_mail_title=input('Enter a Title: ')
            sp=specialcheck(send_mail_title)
            if len(send_mail_title)>20 and sp==0:
                print('Make sure it contains no special characters and is below 21 Characters')
            else:
                title_fix=False
        while content:
            send_mail_content=input('Enter the Content: ')
            cont_chk=specialcheck(send_mail_content)
            if len(send_mail_content)>50 and cont_chk==0:
                print('Make sure there are no special Characters and the length is 50 characters or below')
            else:
                content=False
        pass_file=open("Server/Main Files/Password.csv",'r')
        fr=csv.reader(pass_file)
        sno=sno_1=0
        inv_int=usrt_nex=suc=0
        for k in fr:
            if k[0]==send_user_name:
                suc+=1
                # Opening the Sender's Mail Inbox
                path='Server/Main Files/Userdata/'+k[0]+' Inbox.dat'
                path_chker=os.path.isfile(path)
                if path_chker==False:
                    snd_mail=open(path, 'ab')
                    snd_mail.close()
                
                elif path_chker==True:
                    snd_mail=open(path, 'rb')
                    snd_mail_read=pickle.load(snd_mail)
                    try:
                        for k in snd_mail_read:
                            sno+=1
                    
                    except:
                        sno=1
                    snd_mail.close()
                
                snd_mail=open(path, 'ab')
                rec=[sno,send_mail_title,send_mail_content,'Mail',us]
                pickle.dump(rec,snd_mail)
                snd_mail.close()

                # Opening the User's Sent file
                path='Client/Userdata/'+us+' Sent.dat'
                path_chker=os.path.isfile(path)
                if path_chker==False:
                    snd_mail_temp=open(path, 'ab')
                    snd_mail_temp.close()
                
                elif path_chker==True:
                    snd_mail_temp=open(path, 'rb')
                    while True:
                        try:
                            snd_mail_temp_elem=pickle.load(snd_mail_temp)
                            sno_1+=1
                        
                        except:
                            sno_1=1
                            break

                    snd_mail.close()
                
                sent_mail_rec=open(path, 'ab')
                rec_snd=[sno_1,send_mail_title,send_mail_content,'Mail',send_user_name]
                pickle.dump(rec_snd,sent_mail_rec)
                print('Sending.....')
                print('==================')
                print('Press Enter to go back')
                input()
                sent_mail_rec.close()
                print('Mail sent!')
                print('======================================================================')

        if suc==0:
            if inv_int>0:
                print('You cannot send an invite to yourself')
            if usrt_nex>0:
                print('Such a username does not exist in the Database. Check the username spelling')
            print('Press Enter to go back')
            input()

    else:
        centeral_main_input(outbox_ipt)

# * NORMAL MAIL OUTBOX TEMPLATE
def normal_outbox_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    invite_mail_str=f'''
   =============================================================================
   {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
   =============================================================================
   │  COLUMN    │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ -Groups    │         │
   │------------│         │
   │ -Contracts │         │ Title:{applied_var_j[1]}
   │------------│         │ 
   │ -Mail      │         │
   │------------│• Inbox  │ {applied_var_j[2]}
   │ -Settings  │         │      
   │------------│         │
   │ -Profile   │• Send   │ 
   │------------│         │
   │ -Chats     │         │ 
   │------------│         │
   │ -Players   │         │ To:{applied_var_j[4]}
   │------------│         │
   │------------│         │
   =============================================================================
    '''
    print(invite_mail_str)
    print('Press Enter to go back to Mail')
    enter_ipt=input('=>')
    if enter_ipt.upper()=='X':
        quit(check_num)
    else:
        inbox()

# * ALL USER INFO TEMPLATE
# TODO / IMPLEMENT SEARCHING INTO USER INFO
def user_read(line=1):
  while True:
    clear()
    fdp=open('userdata.csv', 'r')
    fr_pl=csv.reader(fdp)
    c=0
    name_1=name_2=name_3=name_4=name_5='N/A'
    acc_no_1=acc_no_2=acc_no_3=acc_no_4=acc_no_5='N/A'
    col_1=col_2=col_3=col_4=col_5=''
    activ1=activ2=activ3=activ4=activ5='N/A'
    cm_no=0
    if (line//5)!=0:
      p=(line//5)+1
    else:
      p=(line//5)
    plyer=Fore.MAGENTA+'Players'+Fore.RESET
    if line!=1:
        for j in range(line):
            next(fr_pl)

    for k in fr_pl:
      try:
        cm_no+=1
        if c==0:
          name_1=k[0]
          acc_no_1=k[1]
          activ1=k[2]
          if k[2].upper()=='ACTIVE':
            col_1=Fore.LIGHTGREEN_EX
          elif k[2].upper()=='INACTIVE':
            col_1=Fore.LIGHTRED_EX
          elif k[2].upper()=='REMOVED':
            col_1=Fore.LIGHTWHITE_EX 
          fac_1=k[3]
          c+=1
        elif c==1:
          name_2=k[0]
          acc_no_2=k[1]
          activ2=k[2]
          if k[2].upper()=='ACTIVE':
            col_2=Fore.LIGHTGREEN_EX
          elif k[2].upper()=='INACTIVE':
            col_2=Fore.LIGHTRED_EX
          elif k[2].upper()=='REMOVED':
            col_2=Fore.LIGHTWHITE_EX
          fac_2=k[3] 
          c+=1
        elif c==2:
          name_3=k[0]
          acc_no_3=k[1]
          activ3=k[2]
          if k[2].upper()=='ACTIVE':
            col_3=Fore.LIGHTGREEN_EX
          elif k[2].upper()=='INACTIVE':
            col_3=Fore.LIGHTRED_EX
          elif k[2].upper()=='REMOVED':
            col_3=Fore.LIGHTWHITE_EX
          fac_3=k[3] 
          c+=1
        elif c==3:
          name_4=k[0]
          acc_no_4=k[1]
          activ4=k[2]
          if k[2].upper()=='ACTIVE':
            col_4=Fore.LIGHTGREEN_EX
          elif k[2].upper()=='INACTIVE':
            col_4=Fore.LIGHTRED_EX
          elif k[2].upper()=='REMOVED':
            col_4=Fore.LIGHTWHITE_EX 
          fac_4=k[3]
          c+=1
        elif c==4:
          name_5=k[0]
          acc_no_5=k[1]
          activ5=k[2]
          if k[2].upper()=='ACTIVE':
            col_5=Fore.LIGHTGREEN_EX
          elif k[2].upper()=='INACTIVE':
            col_5=Fore.LIGHTRED_EX
          elif k[2].upper()=='REMOVED':
            col_5=Fore.LIGHTWHITE_EX
          fac_5=k[3] 
          c+=1
      except:
        print()

    if (cm_no//5)!=0:
      tp=(cm_no//5)+1
    else:
      tp=(cm_no//5)
    
    exit_btn=Fore.RED+'[X]'+Fore.RESET
    spacer=' '*(73-len(us))
    fdp.close()
    
    p=f'''
        =============================================================================
         {us}{spacer}{exit_btn}
        =============================================================================
        │  COLUMN    │===============================================================
        │------------│ {name_1} - Account number: {acc_no_1}
        │ -Groups    │ {col_1}{color.BOLD}• {activ1}{color.END}{Fore.RESET}
        │------------│===============================================================
        │ -Contracts │ {name_2} - Account number: {acc_no_2}
        │------------│ {col_2}{color.BOLD}• {activ2}{color.END}{Fore.RESET}
        │ -Mail      │===============================================================
        │------------│ {name_3} - Account number: {acc_no_3}
        │ -Settings  │ {col_3}{color.BOLD}• {activ3}{color.END}{Fore.RESET}
        │------------│===============================================================
        │ -Profile   │ {name_4} - Account number: {acc_no_4}
        │------------│ {col_4}{color.BOLD}• {activ4}{color.END}{Fore.RESET}
        │ -Chats     │===============================================================
        │------------│ {name_5} - Account number: {acc_no_5}
        │ -{plyer}   │ {col_5}{color.BOLD}• {activ5}{color.END}{Fore.RESET}
        =============================================================================
        Total records:{cm_no}           Page {p}/{tp}          Enter '/S' to search
        =============================================================================
    '''

    print(p)
    sch = input('=> ')

    # Check if sch is a digit and greater than 0
    if sch.isdigit() and int(sch) > 0 and (int(sch) - 1) <= tp:
        ln = (int(sch) - 1) * 5
        user_read(ln)
    if sch.upper() == name_1.upper():
        profile(name_1, acc_no_1, fac_1)
    elif sch.upper() == name_2.upper():
        profile(name_2, acc_no_2, fac_2)
    elif sch.upper() == name_3.upper():
        profile(name_3, acc_no_3, fac_3)
    elif sch.upper() == name_4.upper():
        profile(name_4, acc_no_4, fac_4)
    elif sch.upper() == name_5.upper():
        profile(name_5, acc_no_5, fac_5)
    elif sch.upper()=='/s':
      name_se=input('[SEARCH NAME] : ')
    else:
        centeral_main_input(sch)

#  * USER PROFILE FROM 
# TODO / ADD PRIVATE MESSAGING SYSTEM
def profile(name,acc_no,rel_fac):
  clear()
  p=f'''
      =============================================================================
       PUBLIC PROFILE
      =============================================================================
      │  COLUMN    │===============================================================
      │------------│
      │ -Groups    │ Name: {Fore.LIGHTGREEN_EX}{name}{Fore.RESET}
      │------------│ Account number: {Fore.LIGHTGREEN_EX}{acc_no}{Fore.RESET}
      │ -Contracts │ 
      │------------│ Relevant Alliances or Factions associated with:
      │ -Mail      │ {Fore.LIGHTGREEN_EX}{rel_fac}{Fore.RESET}
      │------------│
      │ -Settings  │ Readable Denomination:
      │------------│ X$
      │ -Profile   │
      │------------│==================
      │ -Chats     │                 │
      │------------│    (MESSAGE)    │
      │ -Players   │                 │
      =============================================================================
  '''
  print(p)
  ipt=input('=> ')
  if ipt.upper()=='CONTRACTS' or ipt.upper()=='CONTRACT':
    contracts()
  else:
      centeral_main_input(ipt)  

# * GLOBAL CONTRACTS LIST
# TODO / IMPLEMENT SEARCHING INTO GLOBAL CONTRACTS
# ? ADD FILTERS AND LOCATION
# ? ADD SKILL BASED CONTRACT OPENINGS
def contracts(line=1): 
  while True:
    clear()
    tp1=tp2=tp3=tp4=tp5=tp6=tp7='N/A'
    p1=p2=p3=p4=p5=p6=p7='0'
    st1=st2=st3=st4=st5=st6=st7='N/A'
    n1=n2=n3=n4=n5=n6=n7='N/A'
    c1=c2=c3=c4=c5=c6=c7=''
    lim1=lim2=lim3=lim4=lim5=lim6=lim7=''
    ad1=ad2=ad3=ad4=ad5=ad6=ad7=''
    c=0
    cm_no=0

    cont_file=open(contract_file,'r')
    fr=csv.reader(cont_file)
    for k in fr:
      try:
        cm_no+=1
        if c==0:
          tp1=k[0]
          p1=k[1]
          st1=k[2]
          n1=k[3]
          lim1=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad1=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st1.upper()=='OPEN':
            c1=Fore.LIGHTGREEN_EX
        elif c==1:
          tp2=k[0]
          p2=k[1]
          st2=k[2]
          n2=k[3]
          lim2=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad2=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st2.upper()=='OPEN':
            c2=Fore.LIGHTGREEN_EX
        elif c==2:
          tp3=k[0]
          p3=k[1]
          st3=k[2]
          n3=k[3]
          lim3=k[4]
          if k[3].upper()==us.upper():
            ad3=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st2.upper()=='OPEN':
            c3=Fore.LIGHTGREEN_EX
        elif c==3:
          tp4=k[0]
          p4=k[1]
          st4=k[2]
          n4=k[3]
          lim4=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad4=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st4.upper()=='OPEN':
            c4=Fore.LIGHTGREEN_EX
        elif c==4:
          tp5=k[0]
          p5=k[1]
          st5=k[2]
          n5=k[3]
          lim5=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad5=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st5.upper()=='OPEN':
            c5=Fore.LIGHTGREEN_EX
        elif c==5:
          tp6=k[0]
          p6=k[1]
          st6=k[2]
          n6=k[3]
          lim6=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad6=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st6.upper()=='OPEN':
            c6=Fore.LIGHTGREEN_EX
        elif c==6:
          tp7=k[0]
          p7=k[1]
          st7=k[2]
          n7=k[3]
          lim7=k[4]
          c+=1
          if k[3].upper()==us.upper():
            ad7=Fore.LIGHTBLUE_EX+'🜲'+Fore.RESET
          if st7.upper()=='OPEN':
            c7=Fore.LIGHTGREEN_EX
      except:
        print()

    if (line//7)!=1 or (line//7)!=0:
      p=(line//7)+1
    else:
      p=(line//7)
    contrac=Fore.MAGENTA+'Contracts'+Fore.RESET
    try:
      if line!=1 or line!=0:
        for j in range(line):
          next(fr)
    except:
      print()

    if (cm_no//7)!=1 or (cm_no//7)!=0:
      tp=(cm_no//7)+1
    else:
      tp=(cm_no//7)

    cont_file.close()
    pr1=f'''
      =============================================================================
        {Fore.MAGENTA}CONTRACTS{Fore.RESET}
      =============================================================================
      │  COLUMN    │===============================================================
      │------------│ 1) {tp1} │ ${p1} - {c1}{st1}{Fore.RESET} - By: {n1} {color.BOLD}{ad1}
      │ -Groups    │===============================================================
      │------------│ 2) {tp2} │ ${p2} - {c2}{st2}{Fore.RESET} - By: {n2} {color.BOLD}{ad2}
      │ -{contrac} │===============================================================
      │------------│ 3) {tp3} │ ${p3} - {c3}{st3}{Fore.RESET} - By: {n3} {color.BOLD}{ad3}
      │ -Mail      │===============================================================
      │------------│ 4) {tp4} │ ${p4} - {c4}{st4}{Fore.RESET} - By: {n4} {color.BOLD}{ad4}
      │ -Settings  │===============================================================
      │------------│ 5) {tp5} │ ${p5} - {c5}{st5}{Fore.RESET} - By: {n5} {color.BOLD}{ad5}
      │ -Profile   │===============================================================
      │------------│ 6) {tp6} │ ${p6} - {c6}{st6}{Fore.RESET} - By: {n6} {color.BOLD}{ad6}
      │ -Chats     │===============================================================
      │------------│ 7) {tp7} │ ${p7} - {c7}{st7}{Fore.RESET} - By: {n7} {color.BOLD}{ad7}
      │ -Players   │===============================================================
      │------------│ Please Enter '+' to Start your own contract
      │------------│ Please enter 'My Contracts' or 'MC' to see your contarcts
      =============================================================================
                                         {p}/{tp}
      =============================================================================
    '''
    print(pr1)

    ipt=input('=> ')
    if ipt.upper()=='CHANGE':
      print('Enter new Page number')
      ipt=input('=> ')
      if ipt.isdigit() and int(ipt) > 0 and (int(ipt) - 1) <= tp:
        ln = (int(ipt) - 1) * 5
        contracts(ln)

    elif ipt=='+':
      clear()
      print_test='''
    =============================================================================
                        ENTER IMPORTANT CONTRACT INFORMATION
    =============================================================================
      '''
      print(print_test)
      cont_file=open(contract_file,'a',newline='')
      fr=csv.writer(cont_file)
      print()
      topic=input('Enter a Short and Simple headline of what you want: ')
      print()
      price=input('Enter Denomination in USD: ')
      print()
      dt_true=input('Do you want to set a time limit (Y/N): ')
      print()
      user_date='No Limit'
      if dt_true.upper()=='Y':
        date_correct=True
        while date_correct:
          today_date = datetime.now().date()
          date_time=input('Enter time limit in YYYY-MM-DD: ')
          user_date = datetime.strptime(date_time, "%Y-%m-%d").date()

          if user_date > today_date:
            date_correct = False
            print("Contract Processing.......")
          else:
            date_correct = True
            print("User input date is not greater than today's date. Please choose a different date")

      rec=[topic,price,'Open',us,user_date]
      fr.writerow(rec)
      cont_file.close()
      print('Contract Added. Thank you for Chosing us')
      print('=============================================================================')
      print('Enter any key to go back')
      input('=> ')

    elif ipt=='1':
      admin_acc=False
      if ad1!='':
        admin_acc=True
      cont_prac(tp1,p1,st1,n1,lim1,admin_acc)

    elif ipt=='2':
      admin_acc=False
      if ad2!='':
        admin_acc=True
      cont_prac(tp2,p2,st2,n2,lim2,admin_acc)

    elif ipt=='3':
      admin_acc=False
      if ad3!='':
        admin_acc=True
      cont_prac(tp3,p3,st3,n3,lim3,admin_acc)

    elif ipt=='4':
      admin_acc=False
      if ad4!='':
        admin_acc=True
      cont_prac(tp4,p4,st4,n4,lim4,admin_acc)

    elif ipt=='5':
      admin_acc=False
      if ad5!='':
        admin_acc=True  
      cont_prac(tp5,p5,st5,n5,lim5,admin_acc)

    elif ipt=='6':
      admin_acc=False
      if ad6!='':
        admin_acc=True
      cont_prac(tp6,p6,st6,n6,lim6,admin_acc)
    
    elif ipt=='7':
      admin_acc=False
      if ad7!='':
        admin_acc=True
      cont_prac(tp7,p7,st7,n7,lim7,admin_acc)

    else:
        centeral_main_input(ipt)

# * CONTRACT INFO 
def cont_prac(topic,price,stat,contractor,limit,admin):
  if stat.upper()=='OPEN':
    c1=Fore.LIGHTGREEN_EX
  else:
    c1=Fore.LIGHTRED_EX
  
  if admin!=False:
    adm_info=Fore.LIGHTRED_EX+'Please Enter /d to remove contract'+Fore.RESET
  else:
    adm_info=''

  clear()
  p=f'''
  =============================================================================
    CONTRACT INFO
  =============================================================================

    Contract Info: {topic}

    Price on Contract: {price}

    Status: {stat}
    Limit: {c1}{limit}{Fore.RESET}

    Contractor: {contractor}

    {adm_info}

  =============================================================================
    -Press Enter to go back
  =============================================================================
  '''
  print(p)
  input('=> ')




# ? ======================================================================
# *            SUB SCREEN FUNCTIONS
# ? ======================================================================

# * GROUP FOLDER TEMPLATE
# TODO / ADD MORE FOLDERS SLOTS / BETTER FOMRATTING
def under_fold_1(und_count, frst_folder):
    while True:
        clear()
        end_main='Enter ''/u'' to Upload a file'
        end_main_2='Enter ''/d'' to delete a file'
        file_1=file_2=file_3=file_4=file_5=file_6='+'
        ck=n=0
        file_lst=os.listdir('Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder)
        for k in file_lst:
            try:
                if ck==0:
                    file_1=k
                    ck+=1
                elif ck==1:
                    file_2=k
                    ck+=1
                elif ck==2:
                    file_3=k
                    ck+=1
                elif ck==3:
                    file_4=k
                    ck+=1
                elif ck==4:
                    file_5=k
                    ck+=1
                elif ck==5:
                    end_main='NO MORE SPACE! USE ''/D'' TO DELETE AND GAIN SPACE!'
            except:
                print()

        hy=' - '
        files_under_str=' (Files under Database)'
        files_button=Fore.MAGENTA+'-Groups'+clr_main

        mainstr=f'''
    {clr_main}
   =============================================================================
    {clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{files_under_str}{clr_main}
   =============================================================================
   │  COLUMN    │ {main_str}    {test_ver}
   │------------│---------------------------------------------------------------
   │ {files_button}           │   {file_1}
   │------------│
   │ -Contracts │   {file_2}
   │------------│
   │ -Mail      │   {file_3}
   │------------│
   │ -Settings  │   {file_4}
   │------------│
   │ -Profile   │   {file_5}
   │------------│
   │ -Chats     │   {end_main}
   │------------│
   │ -Players   │   {end_main_2}
   ============================================================================={Fore.RESET}
            '''
        print(mainstr)

        ipt=input('=> ')

        if ipt.upper()=='/U':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                print('Please select the file you want to upload to, ',clr_main+frst_folder,Fore.RESET)
                file_path_0=open_file()
                file_name = os.path.basename(file_path_0)
                file_path_1='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_name
                shutil.copy(file_path_0, file_path_1)
                print('===================')
                print('DONE! Press Enter to go back')
                input()
                clear()
            else:
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()
        
        elif ipt.upper()=='/D':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                print('Please select the file you want to Delete ',Fore.BLUE+frst_folder,Fore.RESET)
                file_path_0=open_file()
                file_name = os.path.basename(file_path_0)
                file_path_1='Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_name
                os.remove(file_path_1)
                print('===================')
                print('DONE! Press Enter to go back')
                input()
                clear()
            else:
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()
     
        elif ipt.upper()==file_1.upper() or ipt=='1':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_1
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
       
        elif ipt.upper()==file_2.upper() or ipt=='2':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_2
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        
        elif ipt.upper()==file_3.upper() or ipt=='3':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_3
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        
        elif ipt.upper()==file_4.upper() or ipt=='4':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_4
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        
        elif ipt.upper()==file_5.upper() or ipt=='5':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_5
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        
        elif ipt.upper()==file_6.upper() or ipt=='6':
            path=f'Server/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_6
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        
        elif ipt.upper()==name_of_main.upper():
            mainpro(check_num)

        else:
            centeral_main_input(ipt)

# * USED FOR PRIVATE GROUP TIMLELINES
# TODO / ADD ONLY MANAGER AND ADMIN ADDITIONS AS BARS
# TODO / ADD PROGECT FILEING SYSTEM
# ! DO NOT ADD INTO MAIN YET
def timeline():
  date_format='%Y-%m-%d'
  year=datetime.now().year
  grp_priv_loc=projects_main_loc+'/'+rec_num+' '+name_of_main
  grp_monthly_file=grp_priv_loc+'/Monthly '+str(year)+'.csv'
  if os.path.isdir(grp_priv_loc)==False:
    os.makedirs(grp_priv_loc)
  if os.path.isfile(grp_monthly_file)==False:
    project_file=open(grp_monthly_file,'a',newline='')
    project_file.close()

  c=0
  bar='║'
  b1=b2=b3=b4=b5=b6=b7=b8=''
  gp1=gp2=gp3=gp4=gp5=gp6=gp7=gp8=''

  project_file=open(grp_monthly_file,'r')
  fr=csv.reader(project_file)

  for k in fr:
    try:
      if c==0:
        t1=k[0]
        d1=k[1]
        st1=k[2]
        et1=k[3]
        fr1=k[4]
        br1=int(k[5])
        gl1=int(k[6])
        b1=bar*br1
        gp1=' '*gl1
        c+=1
      elif c==1:
        t2=k[0]
        d2=k[1]
        st2=k[2]
        et2=k[3]
        fr2=k[4]
        br2=int(k[5])
        gl2=int(k[6])
        b2=bar*br2
        gp2=' '*gl2
        c+=1
      elif c==2:
        t3=k[0]
        d3=k[1]
        st3=k[2]
        et3=k[3]
        fr3=k[4]
        br3=int(k[5])
        gl3=int(k[6])
        b3=bar*br3
        gp3=' '*gl3
        c+=1
      elif c==3:
        t4=k[0]
        d4=k[1]
        st4=k[2]
        et4=k[3]
        fr4=k[4]
        br4=int(k[5])
        gl4=int(k[6])
        b4=bar*br4
        gp4=' '*gl4
        c+=1
      elif c==4:
        t5=k[0]
        d5=k[1]
        st5=k[2]
        et5=k[3]
        fr5=k[4]
        br5=int(k[5])
        gl5=int(k[6])
        b5=bar*br5
        gp5=' '*gl5
        c+=1
      elif c==5:
        t6=k[0]
        d6=k[1]
        st6=k[2]
        et6=k[3]
        fr6=k[4]
        br6=int(k[5])
        gl6=int(k[6])
        b6=bar*br6
        gp6=' '*gl6
        c+=1
      elif c==6:
        t7=k[0]
        d7=k[1]
        st7=k[2]
        et7=k[3]
        fr7=k[4]
        br7=int(k[5])
        gl7=int(k[6])
        b7=bar*br7
        gp7=' '*gl7
        c+=1
      elif c==7:
        t8=k[0]
        d8=k[1]
        st8=k[2]
        et8=k[3]
        fr8=k[4]
        br8=int(k[5])
        gl8=int(k[6])
        b8=bar*br8
        gp8=' '*gl8
        c+=1
    except:
      print()
    
  project_file.close()

  year_begin=str(year)+'-01-01'
  year_begin_dt=datetime.strptime(year_begin, date_format)
  curs_gap_count=(abs(((datetime.now()) - year_begin_dt).days))//5
  curs_gap=' '*curs_gap_count

  cur=Fore.LIGHTGREEN_EX+'║'+Fore.RESET

  pr1=f'''
  ==================================================================================================
  │ {Fore.MAGENTA}GROUPS - TIMELINE{Fore.RESET}
  ==================================================================================================
  │  COLUMN    │------------│ MONTHLY BASED WORK
  │------------│            │=======================================================================
  │ -Groups    │            │{curs_gap}{cur}
  │------------│ •Timeline  │{Fore.LIGHTYELLOW_EX} JAN   FEB   MAR   APR   MAY   JUN   JUL   AUG   SEP   OCT   NOV   DEC   {Fore.RESET}
  │ -Contracts │            │{gp1}{Fore.LIGHTBLUE_EX}{b1}{Fore.RESET}
  │------------│            │{gp2}{Fore.LIGHTRED_EX}{b2}{Fore.RESET}
  │ -Mail      │            │{gp3}{Fore.LIGHTBLACK_EX}{b3}{Fore.RESET}
  │------------│            │{gp4}{Fore.LIGHTWHITE_EX}{b4}{Fore.RESET}
  │ -Settings  │            │{gp5}{Fore.LIGHTGREEN_EX}{b5}{Fore.RESET}
  │------------│            │{gp6}{Fore.LIGHTMAGENTA_EX}{b6}{Fore.RESET}
  │ -Profile   │            │{gp7}{Fore.LIGHTCYAN_EX}{b7}{Fore.RESET}
  │------------│            │{gp8}{b8}{Fore.LIGHTYELLOW_EX}{Fore.RESET}
  │ -Chats     │            │
  │------------│            │
  │ -Players   │            │
  │------------│            │=======================================================================
  │------------│------------│
  ==================================================================================================
  '''

  print(pr1)

  ipt=input('=> ')
  
  if ipt=='+':
    print('====================================================')
    print('ADDING NEW PROJECT TIMELINE')
    print('====================================================')
    print()
    name=input('Please Enter Timeline bar name: ')
    print()
    print('Please enter a Brief Description below')
    description=input(':')

    year=datetime.now().year
    date_format='%Y-%m-%d'
    startdate_in=input('Enter Starting Date in (YYYY-MM-DD): ')
    startdate=datetime.strptime(startdate_in, date_format)
    print()

    enddate_in=input('Enter End Date in (YYYY-MM-DD): ')
    enddate=datetime.strptime(enddate_in, date_format)
    day_diff=abs((enddate - startdate).days)

    stop_count=day_diff//5
    year_begin=str(year)+'-01-01'
    year_begin_dt=datetime.strptime(year_begin, date_format)
    gap_count_ch1=abs((startdate - year_begin_dt).days)
    gap_count=gap_count_ch1//5

    assigned_to=input('Enter User who this is assigned to: ')
    
    project_file=open(grp_monthly_file,'a',newline='')
    fr=csv.writer(project_file)
    rec=[name,description,startdate,enddate,assigned_to,stop_count,gap_count]
    fr.writerow(rec)
    project_file.close()
    print()
    print('PROCESSING COMEPLETE! THANK YOU FOR USING US')
    print('====================================================')
    print('Press Enter to go back')
    input('=> ')



init()
log_check()
clear()
passwordmain()
