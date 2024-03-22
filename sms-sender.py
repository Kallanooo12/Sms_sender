import requests
import random
#-----------𝗳𝗼𝗿𝗺𝗮𝘁  𝗰𝗼𝗹𝗼𝘂𝗿 𝗰𝗼𝗱𝗲------------#
b="\033[1;34m"#----------𝗯𝗹𝘂𝗲
bl="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄
w="\033[1;37m"#----------𝘄𝗵𝗶𝘁𝗲 {𝗲𝗻𝗱}
random_colour = [
b,c,g]
ran = random.choice(random_colour)
#------------logo ------------#

logo = (f"""
{ran}-----------------------------------------------{w}
██╗  ██╗ █████╗ ██╗  ██╗   ██╗ █████╗ ███╗   ██╗    
██║ ██╔╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗████╗  ██║    
█████╔╝ ███████║██║   ╚████╔╝ ███████║██╔██╗ ██║    
██╔═██╗ ██╔══██║██║    ╚██╔╝  ██╔══██║██║╚██╗██║    
██║  ██╗██║  ██║███████╗██║   ██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝    
{ran}-----------------------------------------------{w}

{c}Owner  : {ran}S-K Kalyan vai 🥰🥰
{c}Chanel : {ran}Tarmux comand gurop 
{c}Type  : {ran}CUSTOM SMS                                       
""")

print(logo)
# API endpoint
api_url = "https://csfcustomsms.000webhostapp.com/sms.php"

# Phone number to send the SMS to
phone_number = input("ENTER TARGET NUMBER : ")  # Update with the desired phone number

# Custom SMS message to send
sms_message = input("ENTER YOUT MESSAGE : ") # Update with the desired message

# Construct the full API URL with parameters
full_api_url = f"{api_url}?number={phone_number}&sms={sms_message}"

# Send the request to the API
response = requests.get(full_api_url)

# Check if the request was successful
if response.status_code == 200:
    print("SMS sent successfully! OF KALYAN 🥰🥰😁")
else:
    print("Failed to send SMS. Please check the API or try again. name KALyAn my 😁😁")