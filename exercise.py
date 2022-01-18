import numpy as np

def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL analysis")
        print("9 - Quit")
        choice = input("Enter your choice:")
        if choice=='9':
            keep_running = False
        elif choice=='1':
            driver_hdl()

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

def output(answer):
    print(answer)
    
        
        

interface()
