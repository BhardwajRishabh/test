import pywhatkit
phoneno = input("Enter Receiver(recipient) Phone Number :")
message = input("Enter Message You want to send :")
print("Enter Schedule Time to send WhatsApp message to recipient :")
Time_hrs = int(input("- At What Hour :"))
Time_min = int(input("- At What Minutes :"))
pywhatkit.sendwhatmsg(phoneno, message, Time_hrs, Time_min)
pywhatkit.text_to_handwriting("Hello", "filename.png", (0, 0, 138))