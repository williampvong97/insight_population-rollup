import numpy as np
import os
from config_insight_draft import filename_input,filename_output
import csv


# File paths
dir_root=os.getcwd()[:-4]
dir_input=dir_root+"\input"
dir_test=dir_root+"\insight_testsuite\\tests\\your-own-test_1\\input"
dir_output=dir_root+"\output"



# Read input file
lst_cbsa09=[]
lst_cbsa_t=[]
lst_pop00=[]
lst_pop10=[]
lst_ppchg=[]


#dir_input=dir_test
file_input=os.path.join(dir_input,filename_input)
with open(file_input,newline='') as file_input:
    _=csv.reader(file_input,delimiter=",")
    for row in _:
        lst_cbsa09.append(row[7])
        lst_cbsa_t.append(row[8])
        lst_pop00.append(row[12])
        lst_pop10.append(row[14])
        lst_ppchg.append(row[17])

    lst_cbsa09.pop(0)
    lst_cbsa_t.pop(0)
    lst_pop00.pop(0)
    lst_pop10.pop(0)
    lst_ppchg.pop(0)



# Processing data #############################################################

placeholder=-1
arr_report_cbsa09=np.array([placeholder])
lst_report_cbsa_t=[[placeholder]]
lst_report_pop00=[[placeholder]]
lst_report_pop10=[[placeholder]]
lst_report_ppchg=[[placeholder]]


n=np.size(lst_cbsa09)
n=66
for row in range(n):
    
    try:
        _cbsa09=int(lst_cbsa09.pop(0))
    except:
        _cbsa09=str(lst_cbsa09.pop(0))
        
    _cbsa_t=lst_cbsa_t.pop(0)
    _pop00=lst_pop00.pop(0)
    _pop10=lst_pop10.pop(0)
    _ppchg=lst_ppchg.pop(0)
    
    
    # Consider commas
    if type(_pop00)==str:
        _pop00=float(_pop00.replace(",",""))
    else:
        _pop00=float(_pop00)
    if type(_pop10)==str:
        _pop10=float(_pop10.replace(",",""))
    else:
        _pop10=float(_pop10)
    if type(_ppchg)==str:
        try:
            _ppchg=float(_ppchg.replace(",",""))
        except:
            _ppchg=0
    else:
        _ppchg=float(_ppchg)




    if type(_cbsa09)!=str:
        try:
            loc=np.where(arr_report_cbsa09==_cbsa09)[0][0]
        except:
            loc=False
        
        
        if loc!=False:
            lst_report_pop00[loc].append(_pop00)
            lst_report_pop10[loc].append(_pop10)
            lst_report_ppchg[loc].append(_ppchg)
        
        else:
            arr_report_cbsa09=np.append(arr_report_cbsa09,_cbsa09)
            lst_report_cbsa_t.append([_cbsa_t])
            lst_report_pop00.append([_pop00])
            lst_report_pop10.append([_pop10])
            lst_report_ppchg.append([_ppchg])

    else:
        pass







# Write output file

file_output=os.path.join(dir_output,filename_output)
with open(file_output,'w+',newline='') as f:
    writer=csv.writer(f,delimiter=",")
    
    for rows in range (1,len(lst_report_cbsa_t)):
        var1=str(arr_report_cbsa09[rows])
        var2=lst_report_cbsa_t[rows][0]
        var3=str(len(lst_report_pop00[rows]))
        var4=str(int(sum(lst_report_pop00[rows])))
        var5=str(int(sum(lst_report_pop10[rows])))
        var6=str(np.round(np.mean(lst_report_ppchg[rows]),2))
        
        writer.writerows([[var1,var2,var3,var4,var5,var6]])












































