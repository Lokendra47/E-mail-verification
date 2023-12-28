OTP Generation:

generateOTP: Creates a 4-digit OTP randomly from "0123456789".
SMTP Email Sending:

Connects securely to Gmail SMTP, logging in with the account ("Senders_email") using an authentication password ("Password"). Replace with a valid Gmail or App Password.
Email Composition and Sending:

Sends an email from "Senders_email" to "Recievers_email" with the OTP in the body ("OTP: " + y).
User Input for OTP Verification:

User inputs the received OTP with input("Enter your OTP >>: ").
Compares entered OTP (a) with generated OTP (y). Prints "Verified" if matched, otherwise, "Please Check your OTP again."
Google App Password and SMTP:

App Passwords: For secure Google service access with two-step verification.
Use generated App Passwords in Google Account settings.
Replace script's password ("Password") with a valid App Password.
