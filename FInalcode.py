# import library
import math, random

# function to generate OTP
def generateOTP() :

	# Declare a digits variable
	# which stores all digits
	digits = "0123456789"
	OTP = ""

# length of password can be changed
# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	return OTP

# Driver code
if __name__ == "__main__" :
	
	x =" OTP of 4 digits is " ; y = str( generateOTP() )

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("Senders_email", "Password") #in case of gmail use google app Password
#Google App Passwords are generated passwords specifically designed for accessing Google services, including SMTP, from third-party applications.
#They are used when you have enabled two-step verification for your Google account. Instead of using your regular account password, 
#you generate an App Password for each application or device that requires access to your Google account.

# message to be sent

# sending the mail
s.sendmail("Senders_email", "recievers_email", str(x + y))

# terminating the session
s.quit()

a = input("Enter your OTP >>: ")
if a == y:
    print("Verified")
else:
    print("Please Check your OTP again")
