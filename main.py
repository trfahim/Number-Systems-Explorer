import os

def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def back_home():
    back_home = input("\n[0] HOME [00] EXIT >> ")
    if back_home == "0":
        main()
    else:
        print("\nPROGRAM EXIT SUCESSFULL")
        os._exit(0)

def banner():
    print("\n******************************************")
    print("    Number Systems Explorer -- TRFAHIM")
    print("******************************************\n") 

def ban_1():
    print("\n-----------------------------")
def ban_2():
    print("-----------------------------\n")    
    
def home_menu():
    banner()
    print("[1] Decimal Convert")
    print("[2] Binary Convert")
    print("[3] Octal Convert")
    print("[4] Hexadecimal Convert")
    print("[00] Exit")
    
def deci_menu():
    cl()
    banner()
    print("[1] Decimal to Binary")
    print("[2] Decimal to Octal")
    print("[3] Decimal to Hexadecimal")
    print("[0] Home")

def bin_menu():
    cl()
    banner()
    print("[1] Binary to Decimal")
    print("[2] Binary to Octal")
    print("[3] Binary to Hexadecimal")
    print("[0] Home")

def octa_menu():
    cl()
    banner()
    print("[1] Octal to Decimal")
    print("[2] Octal to Binary")
    print("[3] Octal to Hexadecimal")
    print("[0] Home")

def hex_menu():
    cl()
    banner()
    print("[1] Hexadecimal to Decimal")
    print("[2] Hexadecimal to Octal")
    print("[3] Hexadecimal to Binary")
    print("[0] Home")
         
def decimal_to_binary(deci_to_bin):
    try:
        decimal_value = bin(deci_to_bin) [2:]
        print(f"\nDecimal ({deci_to_bin}) >> Binary ({decimal_value})")
    except ValueError:
        print("\nInvalid Decimal Number !!")

def decimal_to_octal(deci_to_oct):
    try:
        decimal_num = oct(deci_to_oct) [2:]
        print(f"\nDecimal ({deci_to_oct}) >> Octal ({decimal_num})")
    except ValueError:
        print("\nInvalid Decimal Number !")

def decimal_to_hexa(deci_to_hex):
    try:
        decimal_num = hex(deci_to_hex) [2:]
        print(f"\nDecimal ({deci_to_hex}) >> Hexadecimal ({decimal_num.upper()})")
    except ValueError:
        print("\nInvalid Decimal Number !")

def binary_to_decimal(bin_to_deci):
    try:
        bin_num = int(bin_to_deci, 2) # Convert binary (string) to decimal using int() with base 2
        print(f"\nBinary ({bin_to_deci}) >> Decimal ({bin_num})")
    except ValueError:
        print("\nInvalid Binary Number !")
        
def binary_to_octal(bin_to_oct):
    try:
        decimal = int(bin_to_oct, 2)
        bin_num = oct(decimal) [2:]     
        print(f"\nBinary ({bin_to_oct}) >> Octal ({bin_num})")
    except ValueError:
        print("\nInvalid Binary Number !")

def binary_to_hexa(bin_to_hex):
    try:
        decimal = int(bin_to_hex) 
        bin_num = hex(decimal) [2:]
        print(f"\nBinary ({bin_to_hex}) >> Hexadecimal({bin_num.upper()})")        
    except ValueError:
        print("\nInvalid Binary Number !")

def octal_to_decimal(oct_to_deci):
    try:
        oct_num = int(oct_to_deci, 8)  
        print(f"\nOctal ({oct_to_deci}) >> Decimal({oct_num})")    
    except ValueError:
        print("\nInvalid Octal Number !")
    
def octal_to_binary(oct_to_bin):
    try:
        decimal = int(oct_to_bin, 8) 
        oct_num = bin(decimal) [2:]
        print(f"\nOctal ({oct_to_bin}) >> Binary({oct_num})")    
    except ValueError:
        print("\nInvalid Octal Number !")
 
def octal_to_hexa(oct_to_hex):
    try:
        decimal = int(oct_to_hex, 8) 
        oct_num = hex(decimal) [2:]
        print(f"\nOctal ({oct_to_hex}) >> Hexadecimal ({oct_num.upper()})")    
    except ValueError:
        print("\nInvalid Octal Number !")
    
def hex_to_decimal(hex_to_dec):
    try:
        hex_num = int(hex_to_dec, 16)
        print(f"\nHexadecimal ({hex_to_dec.upper()}) >> Decimal ({hex_num})")    
    except ValueError:
        print("\nInvalid Hexadecimal Number !")
        
def hex_to_octal(hex_to_oct):
    try:
        decimal = int(hex_to_oct, 16)        
        hex_num = oct(decimal) [2:]
        print(f"\nHexadecimal ({hex_to_oct.upper()}) >> Octal ({hex_num})")
    except ValueError:
        print("\nInvalid Hexadecimal Number !")

def hex_to_binary(hex_to_bin):
    try:
        decimal = int(hex_to_bin, 16)        
        hex_num = bin(decimal) [2:]
        print(f"\nHexadecimal ({hex_to_bin.upper()}) >> Binary ({hex_num})")
    except ValueError:
        print("\nInvalid Hexadecimal Number !")
               
def main():
    cl()
    home_menu()
    home_menu_choose = input("\n>>> ")
    
    if home_menu_choose == "1":
        deci_menu()
        deci_menu_choose = input("\n>>> ")
        if deci_menu_choose == "1":
            cl()
            ban_1()
            print("     DECIMAL TO BINARY")
            ban_2()
            deci_to_bin = int(input("\nEnter Decimal Number >> "))
            cl()
            decimal_to_binary(deci_to_bin) 
            back_home()  
        elif deci_menu_choose == "2":
            cl()
            ban_1()
            print("     DECIMAL TO OCTAL")
            ban_2()
            deci_to_oct = int(input("\nEnter Decimal Number >> "))
            cl()
            decimal_to_octal(deci_to_oct)
            back_home()
        elif deci_menu_choose == "3":
            cl()
            ban_1()
            print("   DECIMAL TO HEXAADECIMAL") 
            ban_2()
            deci_to_hexa = int(input("\nEnter Decimal Number >> "))
            cl()
            decimal_to_hexa(deci_to_hexa)
            back_home()
        elif deci_menu_choose == "0":
            main()
        else:
            cl()
            print("\nWrong Input !!")
            back_home()
    
    elif home_menu_choose == "2":
           bin_menu()
           bin_menu_choose = input("\n>>> ")    
           if bin_menu_choose == "1":
               cl()
               ban_1()
               print("     BINARY TO DECIMAL")
               ban_2()
               bin_to_deci = (input("\nEnter Binary Number >> "))
               cl()
               binary_to_decimal(bin_to_deci)
               back_home()
           elif bin_menu_choose == "2":
               cl()
               ban_1()
               print("     BINARY TO OCTAL") 
               ban_2()
               bin_to_oct = input("\nEnter Binary Number >> ")
               cl()
               binary_to_octal(bin_to_oct)
               back_home()
           elif bin_menu_choose == "3":
               cl()
               ban_1()
               print("    BINARY TO HEXADECIMAL")
               ban_2()
               bin_to_hex = input("\nEnter Binary Number >> ")
               cl()
               binary_to_hexa(bin_to_hex)
               back_home()
           elif bin_menu_choose == "0":
                main()
           else:
               cl()
               print("\nWrong Input !!")
               back_home()
                
    elif home_menu_choose == "3":
        octa_menu()
        octa_menu_choose = input("\n>>> ")
        if octa_menu_choose == "1":
            cl()
            ban_1()
            print("    OCTAL TO DECIMAL")
            ban_2()
            oct_to_deci = input("\nEnter Octal Number >> ")
            cl()        
            octal_to_decimal(oct_to_deci)
            back_home()
        elif octa_menu_choose == "2":
            cl()
            ban_1()
            print("    OCTAL TO BINARY")
            ban_2()
            oct_to_bin = input("\nEnter Octal Number >> ")
            cl()        
            octal_to_binary(oct_to_bin)
            back_home()    
        elif octa_menu_choose == "3":
            cl()
            ban_1()
            print("   OCTAL TO HEXADECIMAL")
            ban_2()
            oct_to_hex = input("\nEnter Octal Number >> ")
            cl()        
            octal_to_hexa(oct_to_hex)
            back_home()    
        elif octa_menu_choose == "0":
            main()
        else:
            cl()
            print("\nWrong Input !!")
            back_home()    

    elif home_menu_choose == "4":
        hex_menu()
        hex_menu_choose = input("\n>>> ")
        if hex_menu_choose == "1":
            cl()
            ban_1()
            print("   HEXADECIMAL TO DECIMAL")
            ban_2()
            hex_to_dec = input("\nEnter Hexadecimal Number >> ")
            cl()
            hex_to_decimal(hex_to_dec)
            back_home()
        elif hex_menu_choose == "2":
            cl()
            ban_1()
            print("   HEXADECIMAL TO OCTAL")
            ban_2()
            hex_to_oct = input("\nEnter Hexadecimal Number >> ")
            cl()
            hex_to_octal(hex_to_oct)
            back_home()
        elif hex_menu_choose == "3":
            cl()
            ban_1()
            print("   HEXADECIMAL TO BINARY")
            ban_2()
            hex_to_bin = input("\nEnter Hexadecimal Number >> ")
            cl()
            hex_to_binary(hex_to_bin)
            back_home()    
        elif hex_menu_choose == "0":
            main()
        else:
            cl()
            print("\nWrong Input !!")
            back_home()    
    
    elif home_menu_choose == "00":
        cl()
        print("\nEXIT SUCESSFUL\n")
        os._exit(0)
    else:
        cl()
        print("\nWrong Input !!")
        back_home()  



if __name__ == "__main__":
    main()
