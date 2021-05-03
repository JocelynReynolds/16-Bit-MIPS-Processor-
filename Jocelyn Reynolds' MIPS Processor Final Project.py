#Jocelyn Reynolds
#Computer Organization
#Professor Sonya Dennis
#Final Project
#April 25, 2021

import sys
import random


def registers_and_memory(registers, memory): #makes a function called registers_and_memory which is also a global variable that can be acessed at any time 
    print("\n") #prints a new line
    print("REGISTERS") #prints the word REGISTERS as is 
    print("----------------") #prints a line
    print("\n") #prints a new line 
    for i in range(0, len(registers)): #for loop with a range as long as the length of the array registers 
        print("Register $%i: %i" % (i, registers[i])) #Formats how registers will be displayed on the screen
        print("\n") #prints a new line
    
    print("MEMORY") #prints MEMORY as is 
    print("----------------") #prints a line
    print("\n") #prints a new line
    for i in range(0, len(memory)): #for loop to create an array of memory with a range as long as the length of th memory array 
        print("Memory [%i]: %i" % (i, memory[i])) #formats how Memory will be displayed on the screen to the user
        print("\n") #prints a new line

running = True #assigns the variable running to True
    
while running:  #while loop to keep the program going while the variable running is true
    print("\n")
    print("Welcome to Jocelyn's MIPS Processor! Come join the fun!", "\U0001F600") #displays what is in quotes
    print("\n") #prints a new line
    hex_var = input("Please enter a hexadecimal number: ") #asks user to enter a hexadecimal number 
    print("\n") #prints a new line
    
    try: #tests code line below
        dec_conversion = int(hex_var, 16)#variable asssigned to integer type variable hex_var and it includes the base for a hexadecimal
        conversion = bin(dec_conversion) #assigns conversion variable to convert a decimal input to a binary input
        
    except ValueError:                    #Doesn't print the computer error message 
        print("This is not a hex number") #print statement 
        sys.exit(1) #stops program after the print statement

    #Initializing the registers and memory
    registers = [] #Empty array for registers
    memory = [] #empty aray for memory
    for i in range(0, 16): #for loop with the range from 0 to 16 which is actually 17
        x = random.randint(1,10) #will output random numbers 
        registers.append(x) #adds random integers to array registers as the program executes
        memory.append(x) #adds random integeres to array memory as the program executes
    registers_and_memory(registers, memory) #gives the registers abd nemory after the user enters a hexadecimal number


    #Assigns variables

    op_code = dec_conversion >> 26 #if variable instruction is equal to r, then the variable op_code shifts by 26

    if op_code == 0: #condition statement 
        rs = dec_conversion >> 21 #shifts rs by 21
        rs_mask = 0b00000011111 #rs mask gives the bits that represent rs solely 
        rs_func = rs & rs_mask #rs_func gives the decimal value of rs
        rt = dec_conversion >> 16 #shifts rt by 16
        rt_mask = 0b0000000000011111 #rt_mask gives the bits that represnt rt solely 
        rt_func = rt & rt_mask #rt_func gives the decimal value of rt 
        rd = dec_conversion >> 11 #shifts rd by 11
        rd_mask = 0b000000000000000011111 #rd_mask gives the bits that represent rd solely
        rd_func = rd & rd_mask  #rd_func gives the value of rd
        shamt = dec_conversion >> 6 #shifts shamt by 6
        shamt_mask = 0b00000000000000000000011111 #represents shamt bits solely
        shamt_func = shamt & shamt_mask #gives the decimal value of shamt
        funct = dec_conversion #funct doesn't get shifted by anything 
        funct_mask = 0b00000000000000000000000000111111 #represents the bits of func which are the last six bits
        funct2 = funct & funct_mask #gives decimal value of funct 2

        if rs_func < 0 or rs_func > 15 or rd_func < 0 or rd_func > 15 or rt_func < 0 or rt_func > 15: #condition to check if the registers will have the right amount which is 16
            print("Invalid register locations") #what is in quotes will appear on the screen to the user 
            sys.exit(1) #exits the program if condition is true
        print("R - Format") #what is in quotes will appear on the screen to the user 
        print("Op_code: ", op_code, "\n", "Rs: ", rs_func, "\n", "Rt: ", rt_func, "\n", "Rd: ", rd_func,"\n", "Shamt: ", shamt_func, "\n", "Funct: ", funct2)#prints contents
        #what is in quotes will appear on the screen to the user 
       
        #Instruction calculations for R-format
        if funct2 == 32: #condition statement 
            print("This is the add instruction of the R-format") #what is in quotes will appear on the screen to the user 
            print("Add: ", "$", rd_func, "=","$",  rs_func, "+", "$", rt_func) #displays the intruction
            print("\n") #prints a new line
            
            registers[rd_func] = registers[rs_func] + registers[rt_func] #displays the register and memory for the instruction
            
        elif funct2 == 34: #condition statement
            print("This is the sub instruction of the R-format") #what is in quotes will appear on the screen to the user 
            print("Sub: ", "$", rd_func, "=","$",  rs_func, "-", "$", rt_func) #displays the instruction
            print("\n") #prints a new line 
            
            registers[rd_func] = registers[rs_func] - registers[rt_func] #displays the registers and memory for the instruction

        elif funct2 == 36: #condition statement 
            print("This is the and instruction of the R-format") #what is in quotes will appear on the screen to the user 
            print("And: ", "$", rd_func, "=","$",  rs_func, "&", "$", rt_func) #displays the instruction
            print("\n") #prints a new line
            
            registers[rd_func] = registers[rs_func] & registers[rt_func] #displays the registers and memory for the instruction

        elif funct2 == 37: #condition statement 
            print("This is the or instruction of the R-format") #what is in quotes will appear on the screen to the user 
            print("Or: ", "$", rd_func, "=","$",  rs_func, "|", "$", rt_func) #displays the instruction
            print("\n") #prints a new line 
            
            registers[rd_func] = registers[rs_func] | registers[rt_func] #displays the registers and memory for the instruction

        else: #executes when the condition is false
            print("Invalid Instruction for R-Format :(") #what is in quotes will appear on the screen to the user 
            sys.exit(1)#exits program if the codition is false 
            
        registers_and_memory(registers, memory) #displays the registers and memory 

        


    elif op_code == 4 or op_code == 8 or op_code == 5 or op_code == 35 or op_code == 43: #conidtion statement to check which instruction to operate 
        rs = dec_conversion >> 21      #shifts rs by 21
        rs_mask = 0b00000011111        #rs mask gives the bits that represent rs solely
        rs_func = rs & rs_mask         #rs_func gives the decimal value of rs
        rt = dec_conversion >> 16      #shifts rt by 16
        rt_mask = 0b0000000000011111   #rt_mask gives the bits that represnt rt solely
        rt_func = rt & rt_mask         #rt_func gives the decimal value of rt
        immediate = dec_conversion      
        immediate_mask = 0b00000000000000001111111111111111 #immediate_mask gives the bits that represent immediate solely
        immediate_func = immediate & immediate_mask #immediate_func gives the decimal value of immediate

        if rs_func < 0 or rs_func > 15 or rt_func < 0 or rt_func > 15: #condition that it is the correct format
            print("Invalid register locations")#what is in quotes will appear on the screen to the user
            sys.exit(1) #exits the program if condition is false 
            
        print("I-Format") #what is in quotes will appear on the screen to the user
        print("Op-Code: ", op_code, "\n", "Rs: ", rs_func, "\n", "Rt: ", rt_func, "\n", "Immediate: ", immediate_func)#prints statements and content

        if op_code == 8: #executes what is below if condition is true 
            print("This is the addi instruction of the I-format") #what is in quotes will appear on the screen to the user
            print("Addi: ", "$", rt_func, "=","$",  rs_func, "+", immediate_func) #prints the instruction
            print("\n") #prints a new line 
            registers[rt_func] = registers[rs_func] + immediate_func #displays the registers and memory
            
        if op_code == 4: #executes what is below if condition is true
            print("This is the beq instruction of the I-format") #what is in quotes will appear on the screen to the user
            print("Beq: ", "if($", rs_func, "==","$",  rt_func, ") goto PC + 1 + ", immediate_func) #displays the instruction 
            print("\n") #prints a new line 
            
            if registers[rs_func] == registers[rt_func]: #condition  statement 
                print("True") #if condition statement above is true, this line will print what is in quotes
            else: #executes what is below if condition is false 
                print("False") #what is in quotes will appear on the screen to the user
            
        if op_code == 5: #conidition statement
            print("This is the bne instruction of the I-format") #what is in quotes will appear on the screen to the user
            print("Bne: ", "if($", rs_func, "!==","$",  rt_func, ") goto PC + 1 + ", immediate_func) #displays instruction
            print("\n") #prints a new line 
            
            if registers[rs_func] != registers[rt_func]: #conidtion statement 
                print("True") #what is in quotes will appear on the screen to the user
                print("\n") #prints a new line 
                
            else: #executes what is below if condition is false
                print("False") #what is in quotes will appear on the screen to the user
                print("\n") #prints a new line

        if op_code == 35: #condition statement 

            if (registers[rs_func] + immediate_func) < 0 or (registers[rs_func] + immediate_func) > 15: #ensures the correct amount of memory locations 
                print("Invalid memory location") #what is in quotes will appear on the screen to the user
                sys.exit(1) #exits program
                
            print("This is the lw instruction of the I-format") #what is in quotes will appear on the screen to the user
            print("Lw: ", "$", rt_func, "= Memory","($", rs_func, "+", immediate_func, ")") #displays instruction
            print("\n") #prints a new line 
            print(registers[rs_func]) #prints rs 
            print(immediate_func)     #prints immediate
            print(registers[rt_func]) #prints rt
            
            registers[rt_func] = memory[registers[rs_func] + immediate_func] #calculates what goes in the register for this specific instruction 
            print(registers[rt_func]) #displays the register afte the calculation of the instruction 

        
        if op_code == 43: #condition statement 

            if (registers[rs_func] + immediate_func) < 0 or (registers[rs_func] + immediate_func) > 15: #checks number of memory locations
                print("Invalid memory location") #what is in quotes will appear on the screen to the user
                sys.exit(1) #exits program
                
            print("This is the sw instruction of the I-format") #what is in quotes will appear on the screen to the user
            print("Sw: ", " Memory","($", rs_func, "+", immediate_func, ") = $", rt_func, "\n") #displays the instruction 
            print("\n") #prints a new line 
            
            memory[registers[rs_func] + immediate_func] = registers[rt_func] #calculates the instruction and puts it into memory 
            
        registers_and_memory(registers, memory) #displays what is in the memory location after the calculation 

      

    #error checking
    else:
        print("Invalid format :( ") #what is in quotes will appear on the screen to the user
        sys.exit(1) #extis program 

    resume = input("Would you like to continue (Y/N): ") #user input
    resume = resume.upper() #allows uppercase input
    
    if resume == "Y": #condition statement 
        running = True # assigns the running variable to True
        
        
    if resume == "N": #condidition statement 
        running == False #if running is false
        print("\n") #prints a new line 
        print("Awww, so sad to see you go. See you next time! ", "\U0001F600") #prints if running is false 
        sys.exit(1) #exits the program 


#Test user input values:

#206400AF - addi instruction

#20A20056 - addi instruction

#00823820 - add instruction 

#00822822 - sub instruction

#00823024 - and instruction

#00821825 - or instruction

#AD070005 - sw instruction

#8D0C0005 - lw instruction

#1126000D - beq instruction

#14A60007 - bne instruction


#R-format
#add - decimal - 32, binary - 100000
#sub - decimal - 34, binary - 100010
#and - decimal - 36, binary - 100100
#or - decimal - 37. binary - 100101
    

#I-format
#addi - decimal - 8, binary- 001000
#beq - decimal - 4, binary - 000100
#bne - decimal - 5, binary - 000101
#lw - deciaml - 35, binary - 100011
#sw - decimal - 43, binary - 101011
