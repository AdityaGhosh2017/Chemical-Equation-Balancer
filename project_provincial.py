print("INSTRUCTIONS FOR FEEDING DATA INTO THE PROGRAM\n")
print("1. Enter the equation having the LHS & RHS seperated by '='.\n")
print("2. There shouldn't be any space within the limits of the equation to be entered.\n")
print("3. The equation should be entirely UNBLANCED, the program will throw error on the account when half-balanced equation had been entered.\n\n")

string_input=input("Enter Completely Unbalanced Chemical Equation :\n")

map=str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

print("\nEntered/Unbalanced Equation is :",string_input.translate(map))
print()
print("PROCESSING.....PLEASE WAIT FOR FEW SECONDS.\n")
complete_list_coe=[]
from sympy import *

import string
list_coefficient_symbol=[]
list_key=[]

rec_string=string_input.partition("=")
inp_reactant=len(rec_string[0].split("+")) 
temp_string=string_input.replace("=","+")
list1=temp_string.split("+")
for m,g in zip(range(len(list1)),string.ascii_lowercase):
  globals()[g]=symbols(g)
  list_coefficient_symbol.append(eval(g)) 
  n=str(m)
  exec("dict_chem_sub_"+n+"=dict()")
  dict_chem_sub=globals()["dict_chem_sub_"+n]
  final_str=list1[m]
  
  length=len(final_str)

  ele_brac_start=final_str.find("(")
  ele_brac_stop=final_str.find(")")
        
  if ele_brac_start!=-1 and ele_brac_stop!=-1:
    dict_chem_sub["ele_brac"]={}
    for a in range(ele_brac_start+1,ele_brac_stop):
      if final_str[a].isupper():
        if a+1<=length-1:
          if final_str[a+1].islower():
            if a+2<=length-1:
              if final_str[a+2].isnumeric():
                if a+3<=length-1:
                  if final_str[a+3].isnumeric():
                
                    dict_chem_sub["ele_brac"][(final_str[a]+final_str[a+1])]=int(final_str[a+2]+final_str[a+3]) 
                    list_key.append(final_str[a]+final_str[a+1])
                  else:
                    dict_chem_sub["ele_brac"][(final_str[a]+final_str[a+1])]=int(final_str[a+2])
                    list_key.append(final_str[a]+final_str[a+1])
                else:
             
                  dict_chem_sub["ele_brac"][(final_str[a]+final_str[a+1])]=int(final_str[a+2]) 
                  list_key.append(final_str[a]+final_str[a+1])
              
              else:
                dict_chem_sub["ele_brac"][(final_str[a]+final_str[a+1])]=1
                list_key.append(final_str[a]+final_str[a+1]) 
            else:  
              dict_chem_sub["ele_brac"][final_str[a]+final_str[a+1]]=1
              list_key.append(final_str[a]+final_str[a+1]) 
          elif final_str[a+1].isnumeric():
            dict_chem_sub["ele_brac"][final_str[a]]=int(final_str[a+1]) 
            list_key.append(final_str[a]) 
          else:
            dict_chem_sub["ele_brac"][final_str[a]]=1
            list_key.append(final_str[a]) 
        else:
          dict_chem_sub["ele_beac"][final_str[a]]=1
          list_key.append(dict_chem_sub["ele_beac"][final_str[a]])
  
    if ele_brac_stop+1<=length: 
      if final_str[ele_brac_stop+1].isnumeric():
        if ele_brac_stop+2<=length:
          if final_str[ele_brac_stop+2].isnumeric():
            temp_brac=int(final_str[ele_brac_stop+1]+final_str[ele_brac_stop+2]) 
          else:
            temp_brac=int(final_str[ele_brac_stop+1])
        else:
          temp_brac=int(final_str[ele_brac_stop+1])
      for x,y in dict_chem_sub["ele_brac"].items():
        dict_chem_sub["ele_brac"][x]=y*temp_brac
      
      
      
      
           
  for a in range(length):
    if a>=ele_brac_start and a<=ele_brac_stop:
      continue
    else:
        if final_str[a].isupper():
          if a+1<=length-1:
            if final_str[a+1].islower():
              if a+2<=length-1:
                if final_str[a+2].isnumeric():
                  if a+3<=length-1:
                    if final_str[a+3].isnumeric():
                
                      dict_chem_sub[(final_str[a]+final_str[a+1])]=int(final_str[a+2]+final_str[a+3]) 
                      list_key.append(final_str[a]+final_str[a+1]) 
                    else:
                      dict_chem_sub[(final_str[a]+final_str[a+1])]=int(final_str[a+2]) 
                      list_key.append(final_str[a]+final_str[a+1]) 
                  else:
             
                    dict_chem_sub[(final_str[a]+final_str[a+1])]=int(final_str[a+2]) 
                    list_key.append(final_str[a]+final_str[a+1]) 
              
                else:
                  dict_chem_sub[(final_str[a]+final_str[a+1])]=1
                  list_key.append(final_str[a]+final_str[a+1])
              else:  
                dict_chem_sub[final_str[a]+final_str[a+1]]=1
                list_key.append(final_str[a]+final_str[a+1]) 
            elif final_str[a+1].isnumeric():
              dict_chem_sub[final_str[a]]=int(final_str[a+1]) 
              list_key.append(final_str[a]) 
            else:
              dict_chem_sub[final_str[a]]=1          
              list_key.append(final_str[a])
       
          else:
            dict_chem_sub[final_str[a]]=1
            list_key.append(final_str[a])
  
list_temp=set(list_key) 
list_key_final=list(list_temp)

count=0
for key in list_key_final:
  globals()["list_coe_"+key]=[]
 
  var_list=eval("list_coe_"+key)
  count=count+1
  for m in range(len(list1)):
    
    var_dict=eval("dict_chem_sub_"+str(m))
    if key in var_dict.keys():
      if m<inp_reactant:
        var_list.append(var_dict[key])
      else:
        var_list.append(-var_dict[key])
    elif "ele_brac" in var_dict.keys():
      if key in var_dict["ele_brac"]:
        if m<inp_reactant:
          var_list.append(var_dict["ele_brac"][key])
        else:
          var_list.append(-var_dict["ele_brac"][key])
      else:
        var_list.append(0)
    else:
      var_list.append(0)
  var_list.append(0)
  complete_list_coe.append(eval("list_coe_"+key))

list_ini_eq=[1]
for x in range(1,len(list1)+1):
 
  if x==len(list1):
    list_ini_eq.append(1)
  else:
    list_ini_eq.append(0)


complete_list_coe.insert(0,list_ini_eq)


system=Matrix(complete_list_coe)

sol=solve_linear_system(system,*list_coefficient_symbol,sep=",")

list_dem_extract=[]
for x in sol.values():
  frac=fraction(x)
  list_dem_extract.append(frac[1])
  
lcm=lcm(list_dem_extract)

list_lcm=[]
for x in sol.values():
  list_lcm.append(x*lcm)

hcf=gcd(list_lcm)

for p,q,r in zip(sol.keys(),sol.values(),list_lcm):
  if hcf==1:
    sol[p]=q*lcm
  else:
    sol[p]=q/r
    



list_pre=[]
for p,q in zip(sol.values(),list1):
  
  z=q.translate(map)
  if p==1:
    list_pre.append(z)
  else:
    list_pre.append(str(p)+z)
  
for x in range(1,inp_reactant+len(list1)+1,2):
      if x<inp_reactant:
        list_pre.insert(x,"+")
      elif x==inp_reactant+1:
        list_pre.insert(x,"=")
      elif x>inp_reactant+1 and x<len(list1)+inp_reactant:
        list_pre.insert(x,"+")

s=""
final=s.join(list_pre)      
print("OUTPUT\nBalanced Equation is :",final)
  
  
  