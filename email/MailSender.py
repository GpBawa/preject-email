import smtplib as s
smtpobj = s.SMTP("smtp.gmail.com", 587)
smtpobj.starttls()
smtpobj.login("gurjeetpalbawa1990@gmail.com", "password")

subject = "This is smtp mail transfer test "
body = "It should have worked successfully.."

message = "Mail:{}\n\n\n{}".format(subject, body)

smtpobj.sendmail("gurjeetpalbawa1990@gmail.com", "gurjeetpalbawa1990@gmail.com", message)

print("Mail sended successfully...")
smtpobj.close()

