import imaplib
import email
import datetime
import configparser
from datetime import date





config = configparser.ConfigParser()
config.read("happy.config")
email_user=config.get("emailCreds", "email_user")
email_pass=config.get("emailCreds", "email_pass")
previousDay=date.today() - datetime.timedelta(days=1)
previousDay=previousDay.strftime('%d-%b-%Y')

initial=date.today() - datetime.timedelta(days=5)
final=date.today() - datetime.timedelta(days=3)

# initial=initial.strftime('%d-%b-%Y')
# final=final.strftime('%d-%b-%Y')
# print(date.today().strftime('%d-%b-%Y'))
# print(previousDay.strftime('%d-%b-%Y'))

#searchQuery='(since "%s" before "%s")'  % (initial, final)
searchQuery='(since "%s")'  % previousDay

print(searchQuery)
mail = imaplib.IMAP4_SSL("<serverName>")
mail.login(email_user, email_pass)


def getMAil():
    mailfolderName='inbox'
    mail.select(mailfolderName)

    result, data = mail.uid('search', None, searchQuery) 

    ids = data[0]

    # list of uids
    id_list = ids.split()

    i = len(id_list)
    # for x in range(i):
    #     latest_email_uid = id_list[x]
    #     print(x)

    #     # fetch the email body (RFC822) for the given ID
    #     result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    #     # I think I am fetching a bit too much here...

    #     raw_email = email_data[0][1]

    #     # converts byte literal to string removing b''
    #     #raw_email_string = raw_email.decode('utf-8')
    #     email_message = email.message_from_bytes(raw_email)
    #     #keyValue=email_message
    #     print(email_message)
    #     print("____________________________________")




    latest_email_uid = id_list[0]
    print(0)

        # fetch the email body (RFC822) for the given ID
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # I think I am fetching a bit too much here...

    raw_email = email_data[0][1]

        # converts byte literal to string removing b''
        #raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_bytes(raw_email)
        #keyValue=email_message
    
    print(email_message['subject'])
    print(email_message['date'])
    print(email_message['from'])
    print("____________________________________")
  

       




    mail.close()

    mail.logout()


getMAil()
