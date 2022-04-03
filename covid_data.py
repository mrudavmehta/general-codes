import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#welcome page

    
print("""
                                            =================================================================================
             
                                                                             IP PROJECT 2020-21 

                                            =================================================================================
    """)




print("""
                                   ======================================================================================================
             
                                                                      ANALYSIS OF COVID-19 IN INDIA
                                    (please note all figures are provided by official sources and are 100% accurate as of 26th Feb 2021)

                                   ======================================================================================================
    """)

#program menu

def Func():
    print("""                          \n\n\n                                            =================================================================================
             
                                                                                PROGRAM MENU 

                                            =================================================================================
                                            =================================================================================
             
                                                                      1. Data in Tabular Form
                                                                      
                                                                      2. Data in Line charts
                                                                      
                                                                      3. Data in Bar graphs
                                                                      
                                                                      4. Data in Pie charts
                                                                      
                                                                      5. Exit

                                            ================================================================================= """)
    
    

#input




    
while True:
    Func()
    YC = int(input("Enter your choice (1-5): "))

    if YC == 1:   #tabular form
        print("")
        print("Data of Covid-19 Cases in a Tabular form: ")
        print("")
        df=pd.read_csv('covid_data.csv')
        print(df.to_string(index=False),'\n\n')
        
        df['State'] = ['MH','KL','KA','AP','TN','DL','UP','WB','OD','RJ']    #reading from csv file and declaring dataframe columns as variables
        State=df['State']
        Cases=df['Cases']
        Recovered=df["Recovered"]
        Active_Cases=df["Active_Cases"]
        Deaths=df["Deaths"]
        
        print("     1 - Sort by least confirmed cases.")    #tabular form sub-menu
        print("     2 - Sort by most recoveries cases per state.")
        print("     3 - Sort by most deaths per state.")
        print("     4 - Sort by most active cases per state.")
        print("     5 - Sort in alphabetical order of State. ")
        print("     6 - Return to main menu. \n\n\n")
        
        YC=int(input("Enter the number representing your preferred query: "))
        
        if YC == 1:
            print("Least cases: ")
            print('\n\n',df.sort_values('Cases',ascending=True))
            
        elif YC == 2:
            print('Most recoveries: ')
            print(df.sort_values('Recovered',ascending=False))
            
        elif YC == 3:
            print('Most deaths: ')
            print(df.sort_values('Deaths',ascending=False))
            
        elif YC == 4:
            print('Most active cases: ')
            print(df.sort_values('Active_Cases',ascending=False))
            
        elif YC == 5:
            print('Alphabetical Order: ')
            print(df.sort_values('State',ascending=True))
            
        elif YC == 6:
            continue
            
        else:
            print("Please enter a valid input: ")
        
    
    elif YC == 2:     #line chart
        
        df=pd.read_csv('covid_data.csv')     #reading from csv file and declaring dataframe columns as variables 
        df['State'] = ['MH','KL','KA','AP','TN','DL','UP','WB','OD','RJ']
        State=df['State']
        Cases=df['Cases']
        Recovered=df["Recovered"]
        Active_Cases=df["Active_Cases"]
        Deaths=df["Deaths"]
        plt.xlabel("States")
        
        print("     1 - Line chart for Confirmed cases per state.")    #line chart sub-menu
        print("     2 - Line chart for Recovered cases per state.")
        print("     3 - Line chart for Deaths per state.")
        print("     4 - Line chart for Active cases per state.")
        print("     5 - Summary")
        print("     6 - Return to main menu. \n\n\n")
        
        YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
        
        if YC == 1:
            plt.ylabel("Cases")
            plt.title("State Wise Cases")
            plt.plot(State, Cases, color='k',marker='o',linewidth=5)
            plt.grid(True)
            plt.show()
            
        elif YC == 2:
            plt.ylabel("Recovered Cases")
            plt.title("State Wise Recovered Cases")
            plt.plot(State, Recovered, color='gold',marker='8',linewidth=2.5)
            plt.grid(True)
            plt.show()
            
        elif YC == 3:
            plt.ylabel("Death Cases")
            plt.title("state wise Death Cases")
            plt.plot(State, Deaths, color='r',marker='*',linewidth=2.5)
            plt.grid(True)
            plt.show()
            
        elif YC == 4:
            plt.ylabel("Active_Cases")
            plt.title("state wise Active_Cases ")
            plt.plot(State, Active_Cases, color='green',marker='d',linewidth=2.5)
            plt.grid(True)
            plt.show()
            
        elif YC == 5:
            plt.ylabel("Number of cases")
            plt.plot(State, Cases, color='b', label = "state wise Cases Cases",marker='o',linewidth=2.5)
            plt.plot(State, Recovered, color='g', label = "state wise Recovered Cases",marker='8',linewidth=2.5)
            plt.plot(State, Deaths, color='r', label = "state wise Death Cases",marker='*',linewidth=2.5)
            plt.plot(State, Active_Cases, color='c', label = "state wise Active_Cases",marker='d',linewidth=2.5)
            plt.title('Line Chart Summary')
            plt.legend()
            plt.grid(True)
            plt.show()
        
        elif YC == 6:
            continue
            
            
        else:
            print("Please enter valid input")
 
    
    elif YC == 3:   #bar graph
        
        print("     1 - Bar graph for Confirmed cases per state.")     #bar graph sub-menu
        print("     2 - Bar graph for Recovered cases per state.")
        print("     3 - Bar graph for Deaths per state.")
        print("     4 - Bar graph for Active cases per state.")
        print("     5 - Bar graph for stack bar chart")
        print("     6 - Bar graph for multi bar chart")
        print("     7 - Return to main menu. \n\n\n")
        
        YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
        
        df = pd.read_csv('covid_data.csv')            #reading from csv file and declaring dataframe columns as variables
        df['State'] = ['MH','KL','KA','AP','TN','DL','UP','WB','OD','RJ']
        State = df["State"]
        Cases = df["Cases"]
        Recovered = df["Recovered"]
        Deaths = df["Deaths"]
        Active_Cases = df["Active_Cases"]
        plt.xlabel("States")
        
        if YC == 1:
            plt.ylabel("Cases")
            plt.title("state wise Cases ")
            plt.bar(State, Cases, color='k', width = 0.5)
            plt.show()
            
        elif YC == 2:
            plt.ylabel("Recovered Cases")
            plt.title("state wise Recoveries")
            plt.bar(State, Recovered, color='gold', width = 0.5)
            plt.show()
            
        elif YC == 3:
            plt.ylabel("Deaths")
            plt.title("state wise Deaths")
            plt.bar(State, Deaths, color='red', width = 0.5)
            plt.show()
            
        elif YC == 4:
            plt.ylabel("Active Cases")
            plt.title("state wise Active Cases")
            plt.bar(State, Active_Cases, color='green', width = 0.5)
            plt.show()
            
        elif YC == 5:
            plt.bar(State, Cases, color='k', width = 0.5, label = "state wise Cases ")
            plt.bar(State, Recovered, color='gold', width = 0.5, label = "state wise Recoveries")
            plt.bar(State, Deaths, color='r', width = 0.5, label = "state wise Deaths")
            plt.bar(State, Active_Cases, color='green',width = 0.5, label = "state wise Active Cases")
            plt.legend()
            plt.show()
            
        elif YC == 6:
            D=np.arange(len(State))
            width=0.25
            plt.bar(D,Cases, width, color='k', label = "state wise Cases")
            plt.bar(D+0.25, Recovered, width, color='gold', label = "state wise Recoveries")
            plt.bar(D+0.50, Deaths, width, color='r', label = "state wise Deaths")
            plt.bar(D+0.75, Active_Cases ,width, color='green', label = "state wise Active Cases")
            plt.xlabel('State Rankings')
            plt.xticks([1,2,3,4,5,6,7,8,9,10])
            plt.legend()
            plt.show()
            
        elif YC == 7:
            continue
            
        else:
            print("Please enter valid input")
            

    
    elif YC == 4:     #pie chart
        
        print("     1 - Pie chart for Confirmed cases per state.")      #pie chart sub menu
        print("     2 - Pie chart for Recoveries per state.")
        print("     3 - Pie chart for Deaths per state.")
        print("     4 - Pie chart for Active cases per state.")
        print("     5 - Return to main menu. \n\n\n")
        
        YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
        
        df = pd.read_csv('covid_data.csv')         #reading from csv file and declaring dataframe columns as variables
        df['State'] = ['MH','KL','KA','AP','TN','DL','UP','WB','OD','RJ']
        State = df["State"]
        Cases = df["Cases"]
        Recovered = df["Recovered"]
        Deaths = df["Deaths"]
        Active_Cases = df["Active_Cases"]
        
        if YC == 1:
            plt.pie(Cases,labels=State,autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Total Cases')
            plt.show()
            
        elif YC == 2:
            plt.pie(Recovered,labels=State,autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Recoveries')
            plt.show()
            
        elif YC == 3:
            plt.pie(Deaths,labels=State,autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Deaths')
            plt.show()
            
        elif YC == 4:
            plt.pie(Active_Cases,labels=State,autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Active Cases')
            plt.show()
            
        elif YC == 5:
            continue
        
        else:
            print("Please enter a valid input")
    
    elif YC == 5:
        break

    
   
    
    else:
        print("Please enter a valid input")
        continue
    

