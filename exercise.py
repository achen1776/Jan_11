import numpy as np

def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL analysis")
        print("2 - LDL analysis")
        print("3 - Total Cholesterol Analysis")
        print("9 - Quit")
        choice = input("Enter your choice:")
        if choice=='9':
            keep_running = False
        elif choice=='1':
            driver_hdl()
        elif choice=='2':
            driver_ldl()
        elif choice=='3':
            driver_total()

def accept_inputs(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)

def check_hdl(entry):
    if entry >= 60:
        answer="Normal"
    elif 60 > entry >= 40:
        answer="Borderline Low"
    else:
        answer="Low"
    return answer

def driver_hdl():
    entry = accept_inputs("HDL")
    answer = check_hdl(entry)
    output(answer)

def check_ldl(entry):
    if entry < 130:
        answer="Normal"
    elif 159 >= entry >= 130:
        answer="Borderline High"
    elif 189 >= entry >= 160:
        answer="High"
    else:
        answer="Very High"
    return answer

def driver_total():
    entry = accept_inputs("Total Cholesterol")
    answer = check_total(entry)
    output(answer)

def check_total(entry):
    if entry < 200:
        answer="Normal"
    elif 239 >= entry >= 200:
        answer="Borderline High"
    else:
        answer="High"
    return answer

def driver_ldl():
    entry = accept_inputs("LDL")
    answer = check_ldl(entry)
    output(answer)

def output(answer):
    print(answer)
    
        
        

interface()
