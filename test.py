import csv
import pickle
import os
import sys
from colorama import Fore, init, Style
from termcolor import colored
import random
import shutil
from tkinter import filedialog
from datetime import datetime
import tkinter
import subprocess
import time
import face_recognition

init(autoreset=True)

contract_file='Contracts.csv'
rec_num='08888'
name_of_main='ballass'

projects_main_loc='Server/Main Files/Projects'
main_str='MAINFRAME VIEWER'
test_ver='BETA VERSION FOR CLOSED EYES'
us='James Mirakilin'

def print_with_typing(text, delay=0.04, color=None):
    for char in text:
        time.sleep(delay)
        if color:
            print(colored(char, color), end='', flush=True)
        else:
            print(char, end='', flush=True)
    print()

class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def clear():
  os.system('cls')

def user_read(line=1):
  while True:
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
    
    p=f'''
        =============================================================================
        
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
  
def profile(name,acc_no,rel_fac):
  p=f'''
      =============================================================================
       PUBLIC PROFILE
      =============================================================================
      │  COLUMN    │===============================================================
      │------------│
      │ -Groups    │ Name: {name}
      │------------│ Account number: {acc_no}
      │ -Contracts │ 
      │------------│ Relevant Alliances or Factions associated with:
      │ -Mail      │ {rel_fac}
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

def batman():
  clear()
  p='''
  ---------------------------------------------------------------------------
                         INITALIZATION IN PROGRESS
  '''
  print(p)
  cir='██████████████████████████████████████████'
  print('                 ',end='')
  for k in range(len(cir)):
    print(Fore.LIGHTCYAN_EX+(cir[k]),end='')
    time.sleep(0.07)
  print(Fore.RESET)
