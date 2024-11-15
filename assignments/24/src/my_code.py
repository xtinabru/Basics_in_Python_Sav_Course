"""
24

1) Create class SMSMessage. The class contains following properties:
- sender                - Phone number
- receiver              - Phone number
- send_time             - Sending date and time
- message               - Message text

2) Create class SMSUtils, which contains two class (static) methods:
- find_messages_dt(messages, dt) - messages contains list containing SMSMessage objects. The function returns list of messages sent at date dt.
- find_messages_sender(messages, sender) - messages contains list containing SMSMessage objects. The function prints list of messages sent from sender phone number.

There is a test software below, don't modify it. Output of the test program shall be following:
ll messages:
+35844123123 +35840632123 02.11.2021 Kotiin ja heti
+35844126783 +358406334523 12.01.2021 Osta makkaraa
+35845678533 +3584007243 12.01.2021 I Love You!!
+35844126783 +358406334523 13.01.2021 Muistitko makkaran?!?!

12.01.2021 messages:
+35844126783 +358406334523 12.01.2021 Osta makkaraa
+35845678533 +3584007243 12.01.2021 I Love You!!

Sender +35844126783 messages:
+35844126783 +358406334523 12.01.2021 Osta makkaraa
+35844126783 +358406334523 13.01.2021 Muistitko makkaran?!?!

"""
from datetime import datetime
#Write class and imports here!




if __name__ == "__main__":
    #Don't modify the main program!
    messages=[]
    dateFormat='%d.%m.%Y'
    timeFormat='%d.%m.%Y %H:%M:%S'
    messages.append(SMSMessage('+35844123123', '+35840632123', datetime.strptime('02.11.2021 11:38:15', timeFormat), 'Kotiin ja heti'))
    messages.append(SMSMessage('+35844126783', '+358406334523', datetime.strptime('12.01.2021 23:45:34', timeFormat), 'Osta makkaraa'))
    messages.append(SMSMessage('+35845678533', '+3584007243', datetime.strptime('12.01.2021 22:33:44', timeFormat), 'I Love You!!'))
    messages.append(SMSMessage('+35844126783', '+358406334523', datetime.strptime('13.01.2021 00:55:01', timeFormat), 'Muistitko makkaran?!?!'))

    print('All messages:')
    for v in messages:
        print(v)

    print()
    dt=datetime.strptime('12.01.2021', dateFormat)
    todays_messages=SMSUtils.find_messages_dt(messages, dt)
    print(datetime.strftime(dt, '%d.%m.%Y'),'messages:')
    for v in todays_messages:
        print(v)
    
    print()
    sender='+35844126783'
    print('Sender', sender, 'messages:')
    SMSUtils.find_messages_sender(messages, sender)

