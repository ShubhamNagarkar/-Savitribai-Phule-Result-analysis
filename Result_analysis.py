from collections import Counter
import pandas as pd
df=pd.read_csv("SE2.csv")

def calc_result (name1,fail_count):
    data1=df[name1].tolist()
    absent_count=0
    present_count=0
    total_count=0
    
    for item in data1:
        item1=str(item)
        
        if item1=="AB":
            absent_count+=1
        else:
            present_count=present_count+1   
        total_count+=1
      
    passed_stud=float(present_count-(fail_count-absent_count) )
    passpercent=float((passed_stud*100)/present_count)
    x=round(passpercent,2)
    return(x,present_count,passed_stud)

def failcount(name1):
    fcount =0
    data1=df[name1].tolist()
    grades={}
    grades.update(Counter(data1))

    if 'O' not in grades.keys():
        grades.update({"O":0})
    if 'P' not in grades.keys():
        grades.update({"P":0})
    if 'F' not in grades.keys():
        grades.update({"F":0})
    cnt=grades['F']    
    return cnt,grades

def totalresult(name):
    fail=pas=0
    dist=fc=hc=sc=pss=0
    for val in df[name]:
        if val=="SS":
            fail+=1;
        else:
            pas+=1;
            if val>="7.75":
                dist+=1
            elif val>="6.75" and val<"7.74":
                fc+=1
            elif val>="6.25" and val<"6.74":
                hc+=1
            elif val>="5.5" and val<"6.25":
                sc+=1
            elif  val<"5.5":
                pss+=1
                    
        
    return pas,fail,dist,fc,hc,sc,pss

def checkback(th,pr):
    t1=t2=t3=p1=p2=p3=0
    for i in df[th]:
        if i==1:
            t1+=1;
        elif i==2:
            t2+=1;
        elif i==3:
            t3+=1;
            
    for i in df[pr]:
        if i==1:
            p1+=1;
        elif i==2:
            p2+=1;
        elif i==3:
            p3+=1;
            
    return t1,t2,t3,p1,p2,p3

def count_pass_atkt(name):
    pss1=atkt=0
    for val in df[name]:
        if val >=50:
            pss1+=1;
        elif val >= 25 and val <=49:
            atkt+=1;
    return  pss1,atkt       
        
#--------------------------------------------------------------------------------------------------------
#("---------------------------Result For TOC--------------------------------- ")
fcnt,t=failcount('207003_Grd')
Tpp,Tpres,Tpass=calc_result('207003_TH',fcnt)
print(Tpp,Tpres,Tpass)
"""
#("---------------------------Result For DBMS--------------------------------- ")

fcnt,d=failcount('210251_Grd')
Dpp,Dpres,Dpass=calc_result('210251_TH',fcnt)

#("---------------------------Result For SEPM--------------------------------- ")
fcnt,s=failcount('210252_GRD')
Spp,Spres,Spass=calc_result('210252_TH',fcnt)

#("---------------------------Result For ISEE--------------------------------- ")
fcnt,i=failcount('210253_GRD')
Ipp,Ipres,Ipass=calc_result('210253_TH',fcnt)

#("---------------------------Result For CN--------------------------------- ")
fcnt,c=failcount('210254_GRD')
Cpp,Cpres,Cpass=calc_result('210254_TH',fcnt)

#("---------------------------Result For SDL--------------------------------- ")

fcnt,l=failcount('210255_GRD')
Lpp,Lpres,Lpass=calc_result('210255_PR',fcnt)

#("---------------------------Result For DBMSL--------------------------------- ")

fcnt,dl=failcount('210256_GRD')
DLpp,DLpres,DLpass=calc_result('210256_PR',fcnt)

#("---------------------------Result For CNL--------------------------------- ")

fcnt,cl=failcount('210257_GRD')
CLpp,CLpres,CLpass=calc_result('210257_PR',fcnt)

t_count=float(df['210248_Grd'].count())
t_appr=max(Cpres,Dpres,Tpres,Ipres,Lpres,DLpres,Spres)
t_pass,t_fail,dis,fc,hc,sc,pss=totalresult('SGPA')
t_result=round(float(t_pass*100/t_count),2)
pss1,atkt = count_pass_atkt("Total Credits Earned")
t_result_atkt = round(float((atkt+pss1)*100/t_count),2)
t1,t2,t3,p1,p2,p3=checkback('th down','PR DOWN')
fp = open("SE2_Result.doc",'w')
fp.write("SINHGAD COLLEGE OF ENGINEERING ,PUNEDEPARTMENT OF COMPUTER ENGINEERING\n\n\n")
fp.write("RESULT ANALYSIS FOR YEAR  [ 2017 - 2018 ]\n\n\n")
fp.write("CLASS  : S.E. (  SEMESTER I)\n\n\n")
fp.write("No. of students appeared  : "+repr(int(t_count))+"  No. of students failed  :   "+repr(t_fail)+"\n")
fp.write("No. of students passed    : "+repr(t_pass)+"\n")  
fp.write("\n\n")    
fp.write("1) First Class with distinction: "+repr(dis)+ " 1) No. of students failed in 1 Th.Sub  : "+repr(t1)+"\n")
fp.write("2) First Class                 : "+repr(fc)+  " 2) No. of students failed in 2 Th.Subs : "+repr(t2)+"\n")
fp.write("3) Higher Second Class         : "+repr(hc)+  " 3) No. of students failed in 3 Th.Subs : "+repr(t3)+"\n")
fp.write("4) Second Class                : "+repr(sc)+  " 4) No. of students failed in 1 Pr/Or   : "+repr(p1)+"\n")
fp.write("5) Pass Class                  : "+repr(pss)+ " 5) No. of students failed in 2 Pr/Or   : "+repr(p2)+"\n")
fp.write("                                 "            " 6) No. of students failed in 3 Pr/Or   : "+repr(p3)+"\n")
fp.write("\n\n")
fp.write("All clear passing Percentage    : "+repr(t_result)+"%\n\n")
fp.write("with ATKT Percentage    : "+repr(t_result_atkt)+"%\n\n")
fp.write("\n\n")

fp.write("Subject wise Result Analysis :\n\n\n")
fp.write(" Sr.no  Th./Pr  Name of subject     Name of the    No. of    No. of      %Pass \n")
fp.write("                Theory/Practical   Staff Member    Students  Students          \n")
fp.write("                                                   Appeared  Passed            \n")
fp.write("\n\n")
fp.write("  1     Th1     Design & Analysis of Algorithms  D.D.Gatade  "+repr(Tpres)+"        "+repr(Tpass)+"      "+repr(Tpp)+"\n")
fp.write("                                                 V.R. Manga\n")
fp.write("                                                 K.G.Shinde\n")
fp.write("  2     Th2     Systems Programming & Operating System  C.A.Laulkar       "+repr(Dpres)+"        "+repr(Dpass)+"      "+repr(Dpp)+"\n")
fp.write("                                                        H.A.Bhute\n")
fp.write("                                                        D.N.Patil\n")
fp.write("\n\n")
fp.write("  3     Th3/E   Embedded Systems & Internet of Things       M.P.Wankhade     "+repr(Spres)+"        "+repr(Spass)+"      "+repr(Spp)+"\n")
fp.write("        L1               G.T.Chavan \n")
fp.write("                           S.S.Suryawanshi \n")
fp.write("\n\n")
fp.write("  4     Th4/E   Software Modeling and Design  J.R.Prasad      "+repr(Ipres)+"        "+repr(Ipass)+"      "+repr(Ipp)+"\n")
fp.write("    L1                   S.R.Hiray \n")
fp.write("                           A.R.JOshi \n")
fp.write("\n\n")
fp.write("  5     Th5/E   Web Technology             G.G.Chiddarwar      "+repr(Cpres)+"        "+repr(Cpass)+"      "+repr(Cpp)+"\n")
fp.write("        L1                     M.R.Dhage  \n")
fp.write("                                     D.P.Salapurkar \n")
fp.write("\n\n")
fp.write("  6     Th5/E   Web Technology Lab            G.G.Chiddarwar  "+repr(Lpres)+"        "+repr(Lpass)+"      "+repr(Lpp)+"\n")
fp.write("        L2                        M.R.Dhage \n")
fp.write("                                     D.P.Salapurkar \n")
fp.write("\n\n")
fp.write("  7     Th6/E   Systems Programming & Operating          C.A.Laulkar       "+repr(DLpres)+"       "+repr(DLpass)+"      "+repr(DLpp)+"\n")
fp.write("        L2      System Lab           H.A.Bhute\n")
fp.write("                                     D.N.Patil\n")
fp.write("                                     G.G.Chiddarwar\n")
fp.write("                                     J.B.Kulkarni\n")
fp.write("\n\n")
fp.write("  8     Pr1     Computer Net         G.T. Chavan     "+repr(CLpres)+"       "+repr(CLpass)+"      "+repr(CLpp)+"\n")
fp.write("                   Lab               E. Jayanthi\n")
fp.write("                                     A.S. Kalaskar\n")



fp.write("\nStaff wise Result Analysis :\n\n")

fp.write(" Sr.no  Subject           %Pass  No.of     O   A+   A   B+   B   C    P   F \n")
fp.write("                                 students  \n")
fp.write("                                 appeared\n")
fp.write("\n\n")
fp.write("  1     Design & Analysis of Algorithms         "+repr(Tpp)+"   "+repr(Tpres)+"      "+repr(t['O'])+"   "+repr(t['A+'])+"   "+repr(t['A'])+"  "+repr(t['B+'])+"   "+repr(t['B'])+"  "+repr(t['C'])+"   "+repr(t['P'])+"  "+repr(t['F'])+"\n")
fp.write("\n\n")
fp.write("  2     Systems Programming & Operating System  "+repr(Dpp)+"   "+repr(Dpres)+"      "+repr(d['O'])+"   "+repr(d['A+'])+"   "+repr(d['A'])+"  "+repr(d['B+'])+"   "+repr(d['B'])+"  "+repr(d['C'])+"   "+repr(d['P'])+"  "+repr(d['F'])+"\n")
fp.write("\n\n")
fp.write("  3     Embedded Systems & Internet of Things     "+repr(Spp)+"   "+repr(Spres)+"      "+repr(s['O'])+"   "+repr(s['A+'])+"   "+repr(s['A'])+"  "+repr(s['B+'])+"   "+repr(s['B'])+"  "+repr(s['C'])+"   "+repr(s['P'])+"  "+repr(s['F'])+"\n")
fp.write("\n\n")
fp.write("  4     Software Modeling and Design  "+repr(Ipp)+"   "+repr(Ipres)+"      "+repr(i['O'])+"   "+repr(i['A+'])+"   "+repr(i['A'])+"  "+repr(i['B+'])+"   "+repr(i['B'])+"  "+repr(i['C'])+"   "+repr(i['P'])+"  "+repr(i['F'])+"\n")
fp.write("\n\n")
fp.write("  5     Web Technology          "+repr(Cpp)+"   "+repr(Cpres)+"      "+repr(c['O'])+"   "+repr(c['A+'])+"   "+repr(c['A'])+"  "+repr(c['B+'])+"   "+repr(c['B'])+"  "+repr(c['C'])+"   "+repr(c['P'])+"  "+repr(c['F'])+"\n")  
fp.write("\n\n")
fp.write("  6     Web Technology Lab"+repr(Lpp)+"   "+repr(Lpres)+"      "+repr(l['O'])+"   "+repr(l['A+'])+"   "+repr(l['A'])+"  "+repr(l['B+'])+"   "+repr(l['B'])+"  "+repr(l['C'])+"   "+repr(l['P'])+"  "+repr(l['F'])+"\n")
fp.write("        Lab     \n")
fp.write("\n\n")
fp.write("  7     Systems Programming & Operating      "+repr(DLpp)+"  "+repr(DLpres)+"      "+repr(dl['O'])+"   "+repr(dl['A+'])+"   "+repr(dl['A'])+"  "+repr(dl['B+'])+"   "+repr(dl['B'])+"  "+repr(dl['C'])+"   "+repr(dl['P'])+"  "+repr(dl['F'])+"\n")
fp.write("        System Lab     \n")
fp.write("\n\n")
fp.write("  8     Computer Network  "+repr(CLpp)+"  "+repr(CLpres)+"      "+repr(cl['O'])+"   "+repr(cl['A+'])+"   "+repr(cl['A'])+"  "+repr(cl['B+'])+"   "+repr(cl['B'])+"  "+repr(cl['C'])+"  "+repr(cl['P'])+"  "+repr(cl['F'])+"\n")
fp.write("        Lab    \n")
 
"""
