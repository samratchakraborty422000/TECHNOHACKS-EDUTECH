# function to convert from celsius to fahrenheit
def To_fahrenheit():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius )+ " degree Celsius is equal to  " + str(fahrenheit )+" degree Fahrenheit.")
    
# function to convert from fahrenheit to celsius  
def To_celsius():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32)/1.8
    print(str(fahrenheit )+ " degree Fahrenheit is equal to " + str(celsius ) + " degree Celsius." )

#main code   
print("TEMPARATURE COVERTER---CREATED BY SAMRAT CAHKRABORTY \n")
print("convert to 1.celcius \n \
          2.fahrenheit \n")
          
select=int(input("select input: "))



while select not in [1,2] :
    print("INVALID INPUT PLEASE TRY AGAIN")
    print("convert to 1.celcius \n \
          2.fahrenheit \n")
    select=int(input("select input: "))
    
    
    
if select==1:
    To_celsius()
if select==2:
    To_fahrenheit()

