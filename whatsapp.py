import pywhatkit as p

numbers=["+917xxxxxxxxxxxxx","+916xxxxxxxxxxx28","+9199xxxxxxxxxxxx"]

for contact in numbers:
    p.sendwhatmsg_instantly(contact,"hello ",tab_close=True)

