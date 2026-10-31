import csv
from PIL import Image
import os
from colorama import Fore, init
import tkinter
from tkinter import filedialog
import shutil
import subprocess

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

log_check()

main_folder_path = 'C:/The Mainframe Program'
main_file_path = main_folder_path+'/Files'
main_log_path = main_file_path+'/Logins'

pers_log_path = address+'/PerLog'
if os.path.isdir(pers_log_path)==False:
    os.makedirs(pers_log_path)

perlog_path = pers_log_path+'/PerLog.csv'

def quit_1(cnp):
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

    import main
    main.passwordmain()

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
    txt_file=open('Mainframes/Mainframe.csv','r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        if k[1]==name_of_main:
            access=k[3]
            rec_num=k[0]
    txt_file.close()
    # Main Settings 3
    fout=open('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/'+rec_num+' '+name_of_main+' Mainframe Main Setings.csv', 'r')
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
    
def open_file():
    win=tkinter.Tk()
    win.withdraw()

    up_file_path = filedialog.askopenfilename()
    return up_file_path

def clear():
    os.system('cls')

def sp_chk(s):
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

def user_settings(chk):
    verify_us_ch(chk)
    clear()
    settings='-Settings'
    hy=Fore.RESET+' - '
    warn=Fore.RED+'UNDERSTAND THAT YOU WILL BE LOGGED OUT IMMEDIATLY!'+Fore.RESET
    mainstr=f'''
============================================================================
{Fore.BLUE+us+Fore.RESET}
============================================================================
            │   
 -Groups    │   USER FILES SETTINGS    
            │   
 -Mail      │   1. Change Main Folder location
            │   {warn}
 {settings}  │
            │   2. Change Password
            │   {warn}
            │   
            │   0. Back
============================================================================
        '''
    print(mainstr)

    set_ipt=input('=> ')

    if set_ipt.upper()=='CHANGE' or set_ipt.upper()=='1':
        fol_win=tkinter.Tk()
        fol_win.withdraw()
        folder_path = filedialog.askdirectory()
        appdata_folder=os.getenv('appdata')

        main_fold_app=appdata_folder+'/Mainframe Program/Userpref/Userpref.csv'
        pref=open(main_fold_app, 'w', newline='')
        pref_write=csv.writer(pref)
        pref_write.writerow([folder_path])
        pref.close()

        quit_1(check_num)

    elif set_ipt.upper()=='PASSWORD' or set_ipt.upper()=='2':
        fout=open('Files/Password.csv','r')
        pass_read=csv.reader(fout)
        old_pass_b=True
        while old_pass_b:
            old_pass=input('Old Password: ')
            for k in pass_read:
                if us==k[0] and old_pass==k[1]:
                    old_pass_b=False
                else:
                    print('You have typed your password wrong, Please try again')
        new_pass_b=True
        while new_pass_b:
            record=[]
            new_pass=input('New Password: ')
            new_pass_re=input('Repeat new Password: ')
            if new_pass==new_pass_re:
                for k in pass_read:
                    if us==k[0] and new_pass==k[1]:
                        print()
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

    elif set_ipt.upper()=='BACK' or set_ipt=='0':
        mainpro(chk)

def verify(check_num):
    global us
    # Main Settings 1
    file_op=main_log_path+f'/Log{check_num}/User.csv'
    txt_file=open(file_op,'r')
    fr_txt=csv.reader(txt_file)
    for k in fr_txt:
        us=k[0]
    txt_file.close()

def mainpro(chk_n):
    global check_num
    check_num=chk_n
    
    global function_has_run
    function_has_run = False
    while True:
        if function_has_run==False:
            verification_0(chk_n)
            function_has_run=True
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
        fldr_lst=os.listdir('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders')
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

        settings='6.Group Settings'
        mainstr=f'''
{clr_main}
============================================================================
{clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{clr_main}
============================================================================
            │   {out_folder_1}
 {files_button}    │
            │   {out_folder_2}
 -Mail      │
            │   {out_folder_3}
 -Settings  │
            │   {out_folder_4}
            │
            │   {out_folder_5}
            │
            │   {settings}
            │ 
            │   {end_main}
============================================================================
        '''
        print(mainstr)

        ipt=input('=> ')

        if ipt=='':
            ipt=ipt+'.'

        if ipt=='+':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                fldr_ipt=input('Enter a new folder name: ')
                fldr_set=open('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/'+rec_num+' '+name_of_main+' Mainframe Folder Setings.csv', 'a',newline='')
                fldr_set.close()
                os.makedirs('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+fldr_ipt.upper())
                first_folder = os.listdir('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+fldr_ipt.upper())
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
        elif ipt=='6' or ipt.upper()=='GROUP SETTINGS':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                setting_function()
            else:
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()
        elif ipt.upper()=='SETTINGS':
            user_settings(chk_n)
        elif ipt.upper()=='MAIL':
            mail(check_num)
        elif ipt.upper()==folder_1.upper() or ipt=='1':
            lister_1 = {}
            path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_1
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
            path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_2
            if os.path.isdir(path)==True:
                second_folder = os.listdir()
                for k in second_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_2)
        elif ipt.upper()==folder_3.upper() or ipt=='3':
            lister_1 = {}
            path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_3
            if os.path.isdir(path)==True:
                third_folder = os.listdir(path)
                for k in third_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_3)
        elif ipt.upper()==folder_4.upper() or ipt=='4':
            lister_1 = {}
            path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_4
            if os.path.isdir(path)==True:
                fourth_folder = os.listdir(path)
                for k in fourth_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_4)
        elif ipt.upper()==folder_5.upper() or ipt=='5':
            lister_1 = {}
            path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+folder_5
            if os.path.isdir(path)==True:
                fifth_folder = os.listdir(path)
                for k in fifth_folder:
                    lister_1[count] = k
                    count+=1
                under_fold_1(count-1,folder_5)
        elif ipt.upper()=='GROUPS':
            import main
            main.mainframeview(us)
        elif ipt.upper()=='X':
            quit_1(chk_n)
        elif ipt.upper()=='/D':
                if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                    print('========================================')
                    print('Please enter the number of the folder that you would like to delete:')
                    num=1
                    for k in fldr_lst:
                        print(num+')', k)
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
                        path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst
                    elif ipt==2:
                        path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+scnd
                    elif ipt==3:
                        path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+thrd
                    elif ipt==4:
                        path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frth
                    elif ipt==5:
                        path='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+ffth
                    os.rmdir(path)
                    print('SUCCESSFULLY DELETED!')
                    print('Press Enter to go back ')
                    input()
                else:
                    print('You dont have enough Clearance!')
                    print('Press Enter to go back ')
                    input()
        elif ipt=='':
            print('Hmm')
            input()
        else:
            print()

def setting_function():
    clear() 
    set_title= 'GROUP SETTINGS'
    invite_str='1.Invite'
    hy = ' - '
    leave_str='0.Back to Datasite'
    setstr=f'''
    {clr_main}
    ============================================================================
    {clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{clr_main}
    ============================================================================
                │
                │   {set_title}
     -Groups    │
                │       {invite_str}
     -Mail      │
                │       {leave_str}
                │
    ============================================================================
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
        pass_file=open("Files/Password.csv",'r')
        fr=csv.reader(pass_file)
        sno=1
        inv_int=usr_nex=suc=0
        for k in fr:
            if invite_user==k[0]:
                suc+=1
                path='Files/Userdata/'+k[0]+' Inbox.csv'
                if path==False:
                    snd_invte_mail=open('Files/Userdata/'+k[0]+' Inbox.csv', 'a')
                    snd_invte_mail.close()
                elif path==True:
                    snd_invte_mail=open('Files/Userdata/'+k[0]+' Inbox.csv', 'r')
                    inv_mail_read=csv.writer(snd_invte_mail)
                    try:
                        for k in inv_mail_read:
                            sno+=1
                    except:
                        sno=1
                    snd_invte_mail.close()
                
                snd_invte_mail=open('Files/Userdata/'+k[0]+' Inbox.csv', 'a', newline='')
                inv_mail_write=csv.writer(snd_invte_mail)
                msg='You have been invited to join '+name_of_main+' as the role of '+invite_user_access
                rec=[sno,'Invitation',msg,'Invite',us,name_of_main,invite_user_access]
                inv_mail_write.writerow(rec)
                print('Sending.....')
                print('==================')
                snd_invte_mail.close()
                print('Mail sent!')
                print('Press Enter to go back')
                input()
            
            elif invite_user==us:
                inv_int+=1

            elif invite_user!=k[0]:
                usr_nex+=1
        
        if suc==0:
            if inv_int>0:
                print('You cannot send an invite to yourself')
            elif usr_nex>0:
                print('Such a username does not exist in the Database. Check the username spelling')
            print('Press Enter to go back')
            input()

        pass_file.close()
        print('----------------------------')

    elif set_inpt.upper()=='GROUPS':
        import main
        main.mainframeview(us)
    
    elif set_inpt.upper()=='MAIL':
        mail(check_num)

    elif set_inpt.upper()=='X':
        quit_1(check_num)

def mail(check_num):
    verify(check_num)
    while True:
        clear()
        mail=Fore.LIGHTWHITE_EX+'-Mail'
        main_mail_str=f'''
        ============================================================================
        {Fore.BLUE}{us}{Fore.RESET}
        ============================================================================
                    │         │
                    │         │
                    │         │
                    │         │
         -Groups    │         │
                    │• Inbox  │
         -Mail      │         │
                    │         │
         -Settings  │• Send   │
                    │         │
                    │         │ 
                    │         │
                    │         │
                    │         │
                    │         │
        ============================================================================
        '''
        print(main_mail_str)
        set_inpt=input('=>')
        if set_inpt.upper()=='INBOX':
            inbox()

        elif set_inpt.upper()=='SEND':
            send()

        elif set_inpt.upper()=='GROUPS':
            import main
            main.mainframeview(us)

        elif set_inpt.upper()=='SETTINGS':
            user_settings(check_num)

        elif set_inpt.upper()=='X':
            quit_1(check_num)

        else:
            print()

def inbox():
    while True:
        clear()
        # Inbox
        mail_open=open('Files/Userdata/'+us+' Inbox.csv', 'r+')
        mail_read_elem=csv.reader(mail_open)
        # We now go into the: The Spacer Problem

        # Defining Varables for later use
        sno=0
        last_del=False
        dict_mail={}
        test_title_plachld1=test_title_plachld2=test_title_plachld3=test_title_plachld4=test_title_plachld5=test_title_plachld6=test_title_plachld7=test_title_plachld8=''
        by_placehld1=by_placehld2=by_placehld3=by_placehld4=by_placehld5=by_placehld6=by_placehld7=by_placehld8=''
        gap_leng1=gap_leng2=gap_leng3=gap_leng4=gap_leng5=gap_leng6=gap_leng7=gap_leng8=' '*25
        g1=g2=g3=g4=g5=g6=g7=g8=' '*25
        for k in mail_read_elem:
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
            elif sno==6:
                # Sixth Mail
                sno+=1
                test_title_plachld6=k[1]
                g6=' '*(25-len(test_title_plachld6))
                by_placehld6='By:'+k[4]
                gap_leng6=' '*(25-len(by_placehld6))
                dict_mail[str(sno)]=k
            elif sno==7:
                # Seventh Mail
                sno+=1
                test_title_plachld7=k[1]
                g7=' '*(25-len(test_title_plachld7))
                by_placehld7='By:'+k[4]
                gap_leng7=' '*(25-len(by_placehld7))
                dict_mail[str(sno)]=k
            elif sno==8:
                # Eighth Mail
                sno+=1
                test_title_plachld8=k[1]
                g8=' '*(25-len(test_title_plachld8))
                by_placehld8='By:'+k[4]
                gap_leng7=' '*(25-len(by_placehld8))
                dict_mail[str(sno)]=k
            elif sno==9:
                last_del=True
        # Now that we have solved the Spacer Problem, We apply  it to this code down here

        # Making sure to delete the oldest Mail since we only have 8 slots
        if last_del==True:
            sno_chk=1
            records=[]
            for k in mail_read_elem:
                if sno_chk==1:
                    sno_chk+=1
                else:
                    try:
                        rec=[sno,k[1],k[2],k[3],k[4],k[5],k[6]]
                    except:
                        rec=[sno,k[1],k[2],k[3],k[4],k[5]]
                    records.append(rec)
                    sno+=1
            mail_open.close()
        
            mail_open=open('Files/Userdata/'+us+' Inbox.csv', 'w', newline='')   
            mail_write_elem=csv.writer(mail_open)
            mail_write_elem.writerows(records)
            inbox()

        mail_open.close() 

        spacer=' '*(73-len(us))
        exit_btn=Fore.RED+'[X]'+Fore.RESET

        mainstr=f'''
        ============================================================================
        {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
        ============================================================================
                    │         │1.                       │2.
                    │         │{test_title_plachld1}{g1}│{test_title_plachld2}{g2}
         -Groups    │         │{by_placehld1}{gap_leng1}│{by_placehld2}{gap_leng2}
                    │         │=====================================================
         -Mail      │         │3.                       │4.
                    │• Inbox  │{test_title_plachld3}{g3}│{test_title_plachld4}{g4}
         -Settings  │         │{by_placehld3}{gap_leng3}│{by_placehld4}{gap_leng4}
                    │         │=====================================================
                    │• Send   │5.                       │6.
                    │         │{test_title_plachld5}{g5}│{test_title_plachld6}{g6}
                    │         │{by_placehld5}{gap_leng5}│{by_placehld6}{gap_leng6}
                    │         │=====================================================
                    │         │7.                       │8.
                    │         │{test_title_plachld7}{g7}│{test_title_plachld8}{g8}
                    │         │{by_placehld7}{gap_leng7}│{by_placehld8}{gap_leng8}
        ============================================================================
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

        elif mail_open_inpt.upper()=='GROUPS':
            import main
            main.mainframeview(us)

        elif mail_open_inpt.upper()=='SEND':
            send()

        elif mail_open_inpt.upper()=='MAIL':
            mail(check_num)

        elif mail_open_inpt.upper()=='X':
            quit_1(check_num)

        elif mail_open_inpt.upper()=='SETTINGS':
            user_settings(check_num)

def invite_mail_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    invite_mail_str=f'''
    ============================================================================
    {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
    ============================================================================
                │         │
                │         │ Invitation to join {applied_var_k[5]}
                │         │ As: {applied_var_k[6]}
                │         │ From:{applied_var_k[4]}
     -Groups    │         │
                │• Inbox  │
     -Mail      │         │ {applied_var_k[2]}     
                │         │
                │• Send   │ 
                │         │-------------------------------- 
                │         │ 
                │         │ Type in [YES] or [Y] to accept
                │         │ 
                │         │ Type in [NO] or [N] to dencline
                │         │
    ============================================================================
    '''
    print(invite_mail_str)
    acc_rej_ipt=input('=>')

    if acc_rej_ipt.upper()=='Y' or acc_rej_ipt.upper()=='YES':
        dup_rec=0
        # Reading file to check Mainframe number
        read_main_data=open('Mainframes/Mainframe.csv', 'r')
        fr=csv.reader(read_main_data)
        # Finding the chk number using this method
        for k in fr:
            if applied_var_k[5]==k[1]:
                chk_num=k[0]
        read_main_data.close()
        rec=[str(chk_num),applied_var_k[5],us,applied_var_k[6]]
        # Reading file for possible duplications
        read_main_data=open('Mainframes/Mainframe.csv', 'r')
        fr=csv.reader(read_main_data)
        for k in fr:
            if k==rec:
                dup_rec=1

        if dup_rec==0:
            # Updating file to add a new user to the mainframe
            update_main_data=open('Mainframes/Mainframe.csv', 'a',newline='')
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
        quit_1(check_num)

def normal_mail_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    invite_mail_str=f'''
============================================================================
    {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
============================================================================
            │         │
            │         │
            │         │ Title:{applied_var_k[1]}
            │         │ 
 -Groups    │         │
            │• Inbox  │ {applied_var_k[2]}
 -Mail      │         │      
            │         │
            │• Send   │ 
            │         │
            │         │ 
            │         │
            │         │ From:{applied_var_k[4]}
            │         │
            │         │
============================================================================
    '''
    print(invite_mail_str)
    print('Press Enter to go back to Mail')
    enter_ipt=input('=>')
    if enter_ipt.upper()=='X':
        quit_1(check_num)
    inbox()

def normal_outbox_temp():
    clear()
    spacer=' '*(73-len(us))
    exit_btn=Fore.RED+'[X]'+Fore.RESET

    invite_mail_str=f'''
============================================================================
    {Fore.BLUE}{us}{Fore.RESET}{spacer}
============================================================================
            │         │
            │         │
            │         │ Title:{applied_var_j[1]}
            │         │ 
 -Groups    │         │
            │• Inbox  │ {applied_var_j[2]}
 -Mail      │         │      
            │         │
            │• Send   │ 
            │         │
            │         │ 
            │         │
            │         │ To:{applied_var_j[4]}
            │         │
            │         │
============================================================================
    '''
    print(invite_mail_str)
    print('Press Enter to go back to Mail')
    enter_ipt=input('=>')
    if enter_ipt.upper()=='X':
        quit_1(check_num)
    send()

def send():
    while True:
        clear()
        # Outbox
        sent_mail_file=open('Files/Userdata/'+us+' Sent.csv', 'a', newline='')
        sent_mail_file.close()
        sent_mail_file=open('Files/Userdata/'+us+' Sent.csv', 'r')
        sent_mail_file_elem=csv.reader(sent_mail_file)

        # Defining Varables for later use
        last_del=False
        sno=0
        dict_mail={}
        test_title_plachld1=test_title_plachld2=test_title_plachld3=test_title_plachld4=test_title_plachld5=test_title_plachld6=test_title_plachld7=test_title_plachld8=''
        by_placehld1=by_placehld2=by_placehld3=by_placehld4=by_placehld5=by_placehld6=by_placehld7=by_placehld8=''
        try:
            for k in sent_mail_file_elem:
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
                elif sno==6:
                    # Sixth Mail
                    sno+=1
                    test_title_plachld6=k[1]
                    by_placehld6='To:'+k[4]
                    dict_mail[str(sno)]=k
                elif sno==7:
                    # Seventh Mail
                    sno+=1
                    test_title_plachld7=k[1]
                    by_placehld7='To:'+k[4]
                    dict_mail[str(sno)]=k
                elif sno==8:
                    # Eighth Mail
                    sno+=1
                    test_title_plachld8=k[1]
                    by_placehld8='To:'+k[4]
                    dict_mail[str(sno)]=k
                elif sno==9:
                    last_del=True
        except:
            print()

        if last_del==True:
            sno_chk=1
            records=[]
            for k in sent_mail_file_elem:
                if sno_chk==1:
                    sno_chk+=1
                else:
                    try:
                        rec=[sno,k[1],k[2],k[3],k[4],k[5],k[6]]
                    except:
                        rec=[sno,k[1],k[2],k[3],k[4],k[5]]
                    records.append(rec)
                    sno+=1
            sent_mail_file.close()
        
            sent_mail_file=open('Files/Userdata/'+us+' Outbox.csv', 'w', newline='')   
            sent_mail_file_elem=csv.writer(sent_mail_file)
            sent_mail_file_elem.writerows(records)
            inbox()

        sent_mail_file.close()

        mail=Fore.LIGHTWHITE_EX+'-Mail'
        spacer=' '*(73-len(us))
        exit_btn=Fore.RED+'[X]'+Fore.RESET

        main_mail_str=f'''
        ============================================================================
        {Fore.BLUE}{us}{Fore.RESET}{spacer}{exit_btn}
        ============================================================================
                    │         │ 1.{test_title_plachld1} │ {by_placehld1}                
                    │         │-----------------------------------------------------
                    │         │ 2.{test_title_plachld2} │ {by_placehld2}     
                    │         │-----------------------------------------------------
         -Groups    │         │ 3.{test_title_plachld3} │ {by_placehld3}    
                    │• Inbox  │-----------------------------------------------------
         -Mail      │         │ 4.{test_title_plachld4} │ {by_placehld4}    
                    │         │-----------------------------------------------------
         -Settings  │• Send   │ 5.{test_title_plachld5} │ {by_placehld5}    
                    │         │-----------------------------------------------------
                    │         │ 6.{test_title_plachld6} │ {by_placehld6}    
                    │         │-----------------------------------------------------
                    │         │ 7.{test_title_plachld7} │ {by_placehld7}    
                    │         │-----------------------------------------------------
                    │         │ 8.{test_title_plachld8} │ {by_placehld8}    
                    │         │-----------------------------------------------------
                    │         │ '+' Compose  │
        ============================================================================
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

        elif outbox_ipt.upper()=='GROUPS':
            import main
            main.mainframeview(us)

        elif outbox_ipt.upper()=='MAIL':
            mail(check_num)

        elif outbox_ipt.upper()=='INBOX':
            inbox()
            
        elif outbox_ipt=='+':
            clear()
            title_fix=content=True
            print('======================================================================')
            print(Fore.RED+'Enter All the information needed to Send a Mail')
            print(Fore.RESET)
            send_user_name=input('Enter Username of the Person: ')
            while title_fix:
                send_mail_title=input('Enter a Title: ')
                sp=sp_chk(send_mail_title)
                if len(send_mail_title)>20 and sp==0:
                    print('Make sure it contains no special characters and is below 21 Characters')
                else:
                    title_fix=False
            while content:
                send_mail_content=input('Enter the Content: ')
                cont_chk=sno_chk(send_mail_content)
                if len(send_mail_content)>50 and cont_chk==0:
                    print('Make sure there are no special Characters and the length is 50 characters or below')
                else:
                    content=False
            pass_file=open("Files/Password.csv",'r')
            fr=csv.reader(pass_file)
            sno=sno_1=0
            inv_int=usr_nex=suc=0
            for k in fr:
                if k[0]==send_user_name:
                    suc+=1
                    # Opening the Sender's Mail Inbox
                    path='Files/Userdata/'+k[0]+' Inbox.csv'
                    path_chker=os.path.isfile(path)
                    if path_chker==False:
                        snd_mail=open(path, 'a', newline='')
                        snd_mail.close()
                    
                    elif path_chker==True:
                        snd_mail=open(path, 'r')
                        snd_mail_read=csv.writer(snd_mail)
                        try:
                            for k in snd_mail_read:
                                sno+=1
                        
                        except:
                            sno=1
                        snd_mail.close()
                    
                    snd_mail=open(path, 'a', newline='')
                    snd_mail_read=csv.writer(snd_mail)
                    rec=[sno,send_mail_title,send_mail_content,'Mail',us]
                    snd_mail_read.writerow(rec)
                    snd_mail.close()

                    # Opening the User's Sent file
                    path='Files/Userdata/'+us+' Sent.csv'
                    path_chker=os.path.isfile(path)
                    if path_chker==False:
                        snd_mail_temp=open(path, 'a', newline='')
                        snd_mail_temp.close()
                    
                    elif path_chker==True:
                        snd_mail_temp=open(path, 'r')
                        snd_mail_temp_elem=csv.writer(snd_mail_temp)
                        try:
                            for k in snd_mail_temp_elem:
                                sno_1+=1
                        
                        except:
                            sno_1=1

                        snd_mail.close()
                    
                    sent_mail_rec=open(path, 'a')
                    sent_mail_rec_elem=csv.writer(sent_mail_rec)
                    rec_snd=[sno_1,send_mail_title,send_mail_content,'Mail',send_user_name]
                    sent_mail_rec_elem.writerow(rec_snd)
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
                if usr_nex>0:
                    print('Such a username does not exist in the Database. Check the username spelling')
                print('Press Enter to go back')
                input()

        elif outbox_ipt.upper()=='X':
            quit_1(check_num)

        elif outbox_ipt.upper()=='SETTINGS':
            user_settings(check_num)

def under_fold_1(und_count_1,frst_folder):
    while True:
        clear()
        end_main='Enter ''/u'' to Upload a file and ''/f'' to create a Sub-folder'
        end_main_2='Enter ''/d'' to delete a file'
        file_1=file_2=file_3=file_4=file_5=file_6='+'
        ck=n=0
        file_lst=os.listdir('Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder)
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
        files_button=Fore.LIGHTWHITE_EX+'-Groups'+clr_main

        mainstr=f'''
    {clr_main}
    ============================================================================
    {clr_acc+name_of_main}{hy}{clr_acc+main_desc}{Fore.RESET}{files_under_str}{clr_main}
    ============================================================================
                │   {file_1}
     {files_button}    │
                │   {file_2}
     -Mail      │
                │   {file_3}
     -Settings  │
                │   {file_4}
                │
                │   {file_5}
                │
                │   {end_main}
                │   {end_main_2}
    ============================================================================
            '''
        print(mainstr)

        ipt=input('=> ')

        if ipt.upper()=='/U':
            if access.upper()=='MANAGER' or access.upper()=='ADMIN':
                print('Please select the file you want to upload to, ',Fore.BLUE+frst_folder,Fore.RESET)
                file_path_0=open_file()
                file_name = os.path.basename(file_path_0)
                file_path_1='Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_name
                shutil.copy(file_path_0, file_path_1)
                print('===================')
                print('DONE! Press Enter to go back')
                input()
                clear()
            else:
                print('You dont have enough Clearance!')
                print('Press Enter to go back ')
                input()
        elif ipt.upper()=='GROUPS' or ipt.upper()=='GROUP':
            import main
            main.mainframeview(us)
        elif ipt.upper()=='BACK':
            mainpro(check_num)
        elif ipt.upper()=='MAIL':
            mail(check_num)
        elif ipt.upper()=='X':
            quit_1(check_num)
        elif ipt.upper()==file_1.upper() or ipt=='1':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_1
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==file_2.upper() or ipt=='2':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_2
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==file_3.upper() or ipt=='3':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_3
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==file_4.upper() or ipt=='4':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_4
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==file_5.upper() or ipt=='5':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_5
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==file_6.upper() or ipt=='6':
            path=f'Mainframes/'+rec_num+' '+name_of_main+' Mainframe/Folders/'+frst_folder+'/'+file_6
            if os.path.isfile(path)==True:
                subprocess.Popen(['start', '', path], shell=True)
        elif ipt.upper()==name_of_main.upper():
            mainpro(check_num)

