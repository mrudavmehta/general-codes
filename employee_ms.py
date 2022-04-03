print('')
print("                                                 INFORMATICS PRACTICES PROJECT")
print("-"*120)
print("                                                      Prepared by Mrudav")
print('-'*120)
print("                                           Employee Payroll Management System")
print('-'*120)
print ('-'*120)
print('')
D={}
n=int(input("   Enter the number of employees: "))
for i in range(n):
    d={}
    k=input("         Enter the employee's ID: ")
    v=input("       Enter the employee's name: ")
    d["Employee Name"]=v
    v=input("Enter the employee's designation: ")
    d["Designation"]=v
    v=int(input("        Enter the employee's age: "))
    d["Age"]=v
    v=int(input("             Enter the basic pay: "))
    d["Basic Pay"]=v
    D[k]=d
    print()
    
D2={}
for i in D:
    n=D[i]["Basic Pay"]
    HRA=n*0.2
    DA=(n+HRA)*0.1
    gross=n+HRA+DA
    PF=0.1225*n
    TAX=0.25*n
    deductions=PF+TAX
    net=gross-deductions
    D2[i]={"HRA":HRA,"DA":DA,"Gross pay":gross,"PF":PF,"Tax":TAX,"Deductions":deductions,"Net Pay":net}

ans='YES' or ans=='yes'
while ans=='YES' or ans=='yes':
    print("What would you like to see ?")
    print("1) All records in ascending order of Basic Pay")
    print("2) Records of employees between the ages of 50 and 60")
    print("3) Records of employees earning above minimum salary")
    print("4) Employee details")
    print("5) Salary Slip")
    print('')
    ch=int(input("Enter your choice:(1-5) "))
    print('\n\n')

    if ch==1:
        l=[]
        for i in D.values():
            l.append(i["Basic Pay"])
        l=sorted(l)
        for i in l:
            for j in D:
                if D[j]['Basic Pay']==i:
                    print("  Employee ID: ",j)
                    print("Employee Name: ",D[j]["Employee Name"])
                    print("  Designation: ",D[j]["Designation"])
                    print("          Age: ",D[j]["Age"])
                    print("    Basic Pay: ",D[j]["Basic Pay"])
                    
    elif ch==2:
        for i in D:
            if D[i]["Age"]<=60 and D[i]["Age"]>=50:
                print("      Employee ID: ",i)
                print("    Employee Name: ",D[i]["Employee Name"])
                print("      Designation: ",D[i]["Designation"])
                print("              Age: ",D[i]["Age"])
                print("        Basic Pay: ",D[i]["Basic Pay"])

    elif ch==3:
        x=int(input("Enter minimum salary: "))
        for i in D:
            if D2[i]["Net Pay"]>=x:
                print("      Employee ID: ",i)
                print("    Employee Name: ",D[i]["Employee Name"])
                print("      Designation: ",D[i]["Designation"])
                print("              Age: ",D[i]["Age"])
                print("        Basic Pay: ",D[i]["Basic Pay"])

    elif ch==4:
        x=input("Enter Employee ID: ")
        if x in D:
            print("          Employee ID: ",x)
            print("        Employee Name: ",D[x]["Employee Name"])
            print("          Designation: ",D[x]["Designation"])
            print("                  Age: ",D[x]["Age"])
            print("            Basic Pay: ",D[x]["Basic Pay"])
        else:
            print("Invalid Employee ID")

    elif ch==5:
        x=input("Enter Employee ID: ")
        month=input("      Enter month: ")
        year=input("       Enter year: ")
        print("\n\n                            SALARY SLIP FOR THE EMPLOYEE FOR THE MONTH OF",month,"YEAR",year,'\n')
        print("          Employee ID  :",x)
        print("          Employee Name:",D[x]["Employee Name"])
        print("          Designation  :",D[x]["Designation"])
        print()
        print("                            Earning                                  ", "        Deductions")
        print("                        Basic Pay:",D[x]["Basic Pay"], "                          PF(12.25% of Basic Pay):",D2[x]["DA"])
        print("            HRA(20% of Basic Pay):",D2[x]["HRA"],      "                          Tax(25% of Basic Pay):",D2[x]["Tax"])
        print("     DA(10% of Basic Pay and HRA):",D2[x]["DA"])
        print("      Gross Pay(Basic Pay+HRA+DA):",D2[x]["Gross pay"],"         Net Deduction(PF+Taxes):",D2[x]["Deductions"])
        print('')
        print('\n'"NET PAY (Gross Pay - Deductions):",D2[x]["Net Pay"])

    else:
        print("Invalid Choice")
    print('\n')
    ans=input("Return to Menu?(YES or NO ?) ")
    print('\n')
