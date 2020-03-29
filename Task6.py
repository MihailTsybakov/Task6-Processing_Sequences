Answer = 0

name_of_file = 'C:\\Users\\mihai\\Desktop\\progy\\data.txt'

def Even_or_odd(name_of_file):
    file = open(name_of_file, 'r')
    len_of_file = 0
    string = file.read()
    for h in string:
        if (h != ''):
            len_of_file += 1
    file.seek(0)    
    temp_string = ''
    integer = ''
    index = 0
    Summ_of_even = 0
    Summ_of_odd = 0
    while (index < len_of_file):
        file.seek(index)
        temp_string = file.read(1)
        if ((temp_string != ' ') and (temp_string != '\n')):
            integer += temp_string
        if ((temp_string ==  ' ') or (temp_string == '\n') or (index == len_of_file - 1)):
            integer = int(integer)
            if ((integer % 2) == 0):
                Summ_of_even += integer
            else:
                Summ_of_odd += integer
            integer = ''
        index += 1
    if (Summ_of_even > Summ_of_odd):
        return 1
    if (Summ_of_even == Summ_of_odd):
        return 0
    if (Summ_of_even < Summ_of_odd):
        return -1
    return answer

def Autotest():
    Test_answer = 0
    test_name = 'C:\\Users\\mihai\\Desktop\\progy\\test.txt'
    Test_answer = Even_or_odd(test_name)
    if (Test_answer == 1):
        print("Autotest passed successfully")
    else:
        print("Autotest not passed")
    return 0

Autotest()

Answer = Even_or_odd(name_of_file)
if (Answer == 0):
    print("Amounts of even numbers and odd numbers are equal")
if (Answer == 1):
    print("Amount of even numbers is bigger than amount of odd numbers")
if (Answer == -1):
    print("Amount of odd numbers is bigger than amount of even numbers")
                
                
        
        
        
    
    
    
