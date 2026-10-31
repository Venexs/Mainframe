import csv
import pickle
import os
import sys
import datetime
from colorama import Fore, init
import random
import MainframeTemplate
init()

def log_check():
    folder=os.path.isdir('Check folder')
    if folder==False:
        os.mkdir('Check folder')

    global address
    main_fold_app='Check folder/Userpref/Userpref.csv'
    main_fold='Check folder/Userpref'
    if os.path.isdir(main_fold)==False:
        os.mkdir(main_fold)
    if os.path.isfile==False:
        pref=open(main_fold_app, 'w', newline='')
        pref_write=csv.writer(pref)
        pref_write.writerow('C:\The Mainframe Program')
        pref.close()
    else:
        pref=open(main_fold_app, 'r')
        pref_read=csv.reader(pref)
        for k in pref_read:
            address=k
        pref.close()

log_check()
n=0

main_folder_path = 'C:/The Mainframe Program'
main_file_path = main_folder_path+'/Files'
main_log_path = main_file_path+'/Logins'

pers_log_path = address+'/PerLog'
if os.path.isdir(pers_log_path)==False:
    os.makedirs(pers_log_path)

perlog_path = pers_log_path+'/PerLog.csv'

def clear():
    os.system('cls')

def multi_test(username,chk_n):
    usr_path_str=main_log_path+f'/Log{chk_n}/User.csv'
    usr_path=open(usr_path_str,'w')
    fw_1=csv.writer(usr_path)
    rec=[username]
    fw_1.writerow(rec)
    usr_path.close()

def logcheck(username, group='NULL'):
    print(0)

    if os.path.isdir(main_log_path):
        print()
    else:
        os.makedirs(main_log_path)

    chk = os.listdir(main_log_path)
    chk_n = 0
    p = 0

    try:
        for k in chk:
            if p == 0:
                temp_log_path = main_log_path+f'Log{chk}/Temp.csv'
                temp_log = open(temp_log_path, 'r')
                fr = csv.reader(temp_log)
                for i in fr:
                    if i[2] == 'Logged':
                        chk_n+=1
                    elif i[1] == username:
                        p+=1
                temp_log.close()
            else:
                break
        
    except:
        p = 1

    log_folder_path = main_log_path+f'/Log{chk_n}'

    if os.path.exists(log_folder_path):
        print()
    else:
        os.makedirs(log_folder_path)

    t_path = main_log_path+f'/Log{chk_n}/Temp.csv'
    temp_log = open(t_path, 'w', newline='')
    fw = csv.writer(temp_log)
    r = [group, username, 'Logged']
    fw.writerow(r)
    temp_log.close()

    usr_path_str = main_log_path+f'/Log{chk_n}/User.csv'
    usr_path = open(usr_path_str, 'w', newline='')
    fw_1 = csv.writer(usr_path)
    rec = [username]
    fw_1.writerow(rec)
    usr_path.close() 

    return chk_n

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

def passwordmain():
    global powers
    global cnp
    powers=False
    clear()
    path=main_file_path
    if os.path.isdir(path):
        print()
    
    else:
        os.makedirs(main_file_path)
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
            if ipt.upper()=='S' or ipt.upper()=='SIGN IN' or ipt.upper()=='SIGN':
                user_true=True
                while user_true==True:
                    false_usr=True
                    fout=open('Files/Password.csv','r')
                    pass_read=csv.writer(fout)
                    username=input("Enter Username: ")
                    for k in pass_read:
                        if username==k[0]:
                            false_usr=False
                    if len(username)>16 and specialcheck(username)==0 and false_usr==True:
                        print('Make sure there are no special Characters and the username is 15 Characters or below')
                    else:
                        user_true=False
                password=input("Enter Password: ")
                re_password=input("Re-type Password: ")
                if password==re_password:
                    cnp=logcheck(username)
                    records=[]
                    fout=open('Files/Password.csv','a', newline='')
                    fw=csv.writer(fout)
                    print("=" * 30)
                    rec = [username, password]
                    records.append(rec)
                    fw.writerows(records)
                    fout.write('\n')
                    fout.close()
                    data=[]
                    logdt = datetime.datetime.now()
                    logdt_str = logdt.strftime('%Y-%m-%d %H:%M:%S')
                    logf=open('Files/Log.dat', 'ab')
                    x="Welcome back", username, "You have", n,"Notifications"
                    print("Welcome back", username, "You have", n,"Notifications")
                    c+=1
                    log = username + ', ' + logdt_str + ' GMT'+' \n'
                    print(log)
                    data.append(log)
                    pickle.dump(data, logf)
                    logf.close()

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

                else:
                    print('Incorrect Password')

            elif ipt.upper()=='L' or ipt.upper()=='LOGIN':
                username=input("Enter Username: ")
                password=input("Enter Password: ")
                c=0

                fout=open('Files/Password.csv','r') 
                fr=csv.reader(fout)
                for k in fr:
                    if (username==k[0]) and (password==k[1]):
                        if username=='Admin':
                            powers=True
                            cnp=logcheck(username)
                            data=[]
                            logdt = datetime.datetime.now()
                            logdt_str = logdt.strftime('%Y-%m-%d %H:%M:%S')
                            logf=open('Files/Log.dat', 'ab')
                            c+=1
                            log = username + ', ' + logdt_str + ' GMT'+' \n'
                            data.append(log)
                            pickle.dump(data, logf)
                            logf.close()
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
                    
                        else:
                            cnp=logcheck(username)
                            data=[]
                            logdt = datetime.datetime.now()
                            logdt_str = logdt.strftime('%Y-%m-%d %H:%M:%S')
                            logf=open('Files/Log.dat', 'ab')
                            c+=1
                            log = username + ', ' + logdt_str + ' GMT'+' \n'
                            data.append(log)
                            pickle.dump(data, logf)
                            logf.close()
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
                if c==0:
                    print('Wrong login')
                    input()
                    sys.exit()
        
    else:   
        data=[]
        ftut=open(perlog_path,'r')
        fr=csv.reader(ftut)
        for k in fr:
            username=k[0]
        ftut.close()
        logdt = datetime.datetime.now()
        logdt_str = logdt.strftime('%Y-%m-%d %H:%M:%S')
        logf=open('Files/Log.dat', 'ab')
        log = username + ', ' + logdt_str + ' GMT'+' \n'
        data.append(log)
        pickle.dump(data, logf)

    clear()
    mainframeview(username)

def mainframeview(usr):
    clear()
    n=0
    c=0
    ftut=open('Mainframes/Mainframe.csv','r')
    fr=csv.reader(ftut)
    one_main=two_main=three_main=four_main=five_main='+'
    access_one=access_two=access_three=access_four=access_five=''
    end_main='Enter + to make a new Server'
    for k in fr:
       if k[2]==usr:
            if n==0:
                one_main=k[1]
                one_code=k[0]
                access_one=k[3]
                n+=1
            elif n==1:
                two_main=k[1]
                two_code=k[0]
                access_two=k[3]
                n+=1
            elif n==2:
                three_main=k[1]
                three_code=k[0]
                access_three=k[3]
                n+=1
            elif n==3:
                four_main=k[1]
                four_code=k[0]
                access_four=k[3]
                n+=1
            elif n==4:
                five_main=k[1]
                five_code=k[0]
                access_five =k[3]
                n+=1
            elif n==5:
                end_main='NO MORE SPACE TO MAKE A SERVER'

    ftut.close()
    usr_noclr=usr
    username_te=Fore.BLUE+usr+Fore.RESET
    spacer=' '*(73-len(usr_noclr))
    exit_btn=Fore.RED+'[X]'+Fore.RESET
    cnp=logcheck(usr_noclr)
    clear()
    mainstr=f'''
============================================================================
{username_te}{spacer}{exit_btn}
============================================================================
  COLUMN    │ MAINFRAME VIEWER 0.756    BETA TESTER VERSION
------------│---------------------------------------------------------------
            │   - {one_main} {Fore.RED+access_one+Fore.RESET}
            │
  -Groups   │   - {two_main} {Fore.RED+access_two+Fore.RESET}
            │ 
  -Mail     │   - {three_main} {Fore.RED+access_three+Fore.RESET}
            │
  -Settings │   - {four_main} {Fore.RED+access_four+Fore.RESET}
            │
            │   - {five_main} {Fore.RED+access_five+Fore.RESET}
            │
            │ {end_main}
============================================================================
    '''
    print(mainstr)

    ipt=input('=>')

    if ipt=='+':
        print('======================================================================')
        print(Fore.RED+'Enter All the information needed to create your own Mainframe')
        print(Fore.RESET)
        main_name=input('Enter name of your Mainframe: ')
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
        rec_num=str(random.randint(100, 99999999))
        os.makedirs('Mainframes/'+rec_num+' '+main_name+' Mainframe')
        os.makedirs('Mainframes/'+rec_num+' '+main_name+' Mainframe/Folders')
        fout=open('Mainframes/'+rec_num+' '+main_name+' Mainframe/'+rec_num+' '+main_name+' Mainframe Main Setings.csv', 'w',newline='')
        fw=csv.writer(fout)
        rec=[main_name,main_desc,clr_main,clr_acce]
        records.append(rec)
        fw.writerows(records)
        fout.close()
        records.clear()
        # Saves Mainframe name and user under Files/Mainframe.csv
        file_namesave=open('Mainframes/Mainframe.csv', 'a',newline='')
        fw=csv.writer(file_namesave)
        rec=[rec_num,main_name,usr_noclr,'Admin']
        records.append(rec)
        fw.writerows(records)
        file_namesave.close()
        # Gets ready to open the Mainframe
        logcheck(usr_noclr,main_name)
        c+=1

    elif ipt.upper()==one_main.upper():
        logcheck(usr_noclr,one_main)
        c+=1

    elif ipt.upper()==two_main.upper():
        logcheck(usr_noclr,two_main)
        c+=1

    elif ipt.upper()==three_main.upper():
        logcheck(usr_noclr,three_main)
        c+=1

    elif ipt.upper()==four_main.upper():
        logcheck(usr_noclr,four_main)
        c+=1

    elif ipt.upper()==five_main.upper():
        logcheck(usr_noclr,five_main)
        c+=1

    elif ipt.upper()=='MAIL':
        MainframeTemplate.mail(cnp)

    elif ipt.upper()=='SETTINGS':
        MainframeTemplate.user_settings(cnp)

    elif ipt.upper()=='X':
        quit(cnp)

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
        
        # Deleting folder
        rm='Mainframes/'+code+' '+rec_name+' '+'Mainframe'
        os.rmdir(rm)

        # Re-opening Mainframe View
        mainframeview(usr)

    if c>0:
        clear()
        MainframeTemplate.mainpro(cnp)

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

clear()
passwordmain()

