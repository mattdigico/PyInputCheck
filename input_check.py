#Input Validation & Check Functions
#Matt Davison
#04/09/2019



#--------------------------------
#----Integer-Input-Validation----
#--------------------------------
"""Returns integer value once user has entered a valid integer"""
def int_input(ask_string,error_string): #Checks if the input is an integer
  valid=False
  while not valid: #Loops until a valid integer is inputted
    try:
      int_input = int(input(ask_string)) #Tries to convert to int
      valid=True
    except:
      print(error_string)
      valid=False #Continues in loop if false
  return int_input


#------------------------------
#---Yes/No-Input-Validation----
#------------------------------
"""Returns True (input of yes/y) or False (input of no/n) once user has entered valid input"""
def yes_no_input(ask_string,error_string): #Checks string input and returns bool
  valid=False
  while not valid: #Iterates until valid input
    yn_input = input(ask_string)
    yn_lower = yn_input.lower()
    if yn_lower == 'y' or yn_lower == 'yes': #Check for y
      valid = True #Changes to exit loop
      return True
    elif yn_lower == 'n' or yn_lower == 'no': #Check for n
      valid = True #Changes to exit loop
      return False
    else: #Stays in loop, prints error message
      print(error_string)



#-----------------------------------
#----IP-Address-Input-Validation----
#-----------------------------------
"""Returns IP address as string once the user has provided a valid input"""
#General Function
def ip_input(ask_string,error_string,ip_version=4):
  valid_ip = False
  while not valid_ip: #Iterates until valid input
    check = True
    user_ip = input(ask_string)
    ip_nums = user_ip.split('.') #Splits into separate numbers
    for i in ip_nums:
      try: #Checks if value is less than a byte
        if int(i)<0 or int(i)>255:
          check = False #Changes to false if limits exceeded
      except: #Changes to false if it isn't an int value
        check = False
    if len(ip_nums) != ip_version:
      check = False #Changes to false if IP is too longer for version
    if not check: #If check is false, error message printed
      print(error_string)
    valid_ip = check #Stays in loop if false
  return user_ip

#IPv4 Input
def ipv4_input(ask_string,error_string):
  return ip_input(ask_string,error_string,4)

#IPv6 Input
def ipv6_input(ask_string,error_string):
  return ip_input(ask_string,error_string,6)


#---------------------------
#----IP-Address-Checking----
#---------------------------
"""Returns True or False depending on whether the IP address string is valid or not"""
#General Function
def ip_check(ip,ip_version=4):
  check = True
  ip_nums = ip.split('.') #Splits into separate numbers
  for i in ip_nums:
    try:
      if int(i)<0 or int(i)>255:
        check = False #False if they are out of range
    except:
      check = False #False if not integers
  if len(ip_nums) != ip_version:
    check = False #False if incorrect number of values
  return check

#IPv4 Check
def ipv4_check(ip):
  return ip_check(ip,4)

#IPv6 Check
def ipv6_check(ip):
  return ip_check(ip,6)
