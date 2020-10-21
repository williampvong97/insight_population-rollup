import os
import csv
from config_insight_pop_rollup import filename_input,filename_output


# File paths
dir_root=os.getcwd()
dir_input=dir_root+"/input"
dir_test=dir_root+"/insight_testsuite/tests/your-own-test_1/input"
dir_output=dir_root+"/output"



# Read input file and initialize ##############################################
lst_cbsa09=[]
lst_cbsa_t=[]
lst_pop00=[]
lst_pop10=[]
lst_ppchg=[]


file_input=os.path.join(dir_input,filename_input)
with open(file_input,newline='',encoding="ISO-8859-1") as file_input: # Encoding specified for case of entire .csv input
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
lst_report_cbsa09=[placeholder]
lst_report_cbsa_t=[[placeholder]]
lst_report_pop00=[[placeholder]]
lst_report_pop10=[[placeholder]]
lst_report_ppchg=[[placeholder]]


n=len(lst_cbsa09)
for row in range(n):
    
    # Check for empty space CBSA09
    try:
        _cbsa09=int(lst_cbsa09.pop(0))
    except:
        _cbsa09=False
        
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



    if _cbsa09!=False:
        try:
            loc=lst_report_cbsa09.index(_cbsa09)
        except:
            loc=False
        
        
        if loc!=False:
            lst_report_pop00[loc].append(_pop00)
            lst_report_pop10[loc].append(_pop10)
            lst_report_ppchg[loc].append(_ppchg)
        
        else:
            lst_report_cbsa09.append(_cbsa09)
            lst_report_cbsa_t.append([_cbsa_t])
            lst_report_pop00.append([_pop00])
            lst_report_pop10.append([_pop10])
            lst_report_ppchg.append([_ppchg])

    else:
        pass



# Write output file ###########################################################

file_output=os.path.join(dir_output,filename_output)
with open(file_output,'w+',newline='') as f:
    writer=csv.writer(f,delimiter=",")
    
    for rows in range(1,len(lst_report_cbsa_t)):
        _01=str(lst_report_cbsa09[rows])
        _02=lst_report_cbsa_t[rows][0]
        _03=str(len(lst_report_pop00[rows]))
        _04=str(int(sum(lst_report_pop00[rows])))
        _05=str(int(sum(lst_report_pop10[rows])))
        _06="{:.2f}".format(sum(lst_report_ppchg[rows])/len(lst_report_ppchg[rows]))
        
        writer.writerows([[_01,_02,_03,_04,_05,_06]])






















