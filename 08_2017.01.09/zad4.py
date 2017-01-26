#! /usr/bin/python3
# algorytmy, ktore sprawdza, czy podane dane sa dopuszczalne,

def validate_email(email):
    if '@' in email and email.count('@') == 1:
        splitEmail = email.split('@')
        beforeAt = splitEmail[0]
        afterAt = splitEmail[1]
        if len(beforeAt) >= 1 and len(afterAt) >= 5:
            if '.' in afterAt and afterAt.count('.') <= 2:
                #beforeDot = afterAt.split('.')[0]
                afterDot = afterAt.split('.')[-1]
                if len(afterDot) == 2:
                    print(True)
                else:
                    print(False) 
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)
        
def validate_zip(zipCode):
    zipCode = zipCode.lstrip().rstrip()
    if '-' in zipCode and zipCode.count('-') == 1:
        beforeHyphen = zipCode.split('-')[0].rstrip()
        afterHyphen = zipCode.split('-')[1].lstrip()
        if beforeHyphen.isalnum() and afterHyphen.isalnum() and len(beforeHyphen) == 2 and len(afterHyphen) == 3:
            print(True)
        else:
            print(False)
    else:
        print(False)

running = True
while running:
    print('\nValidator:')
    menu = {1: '- Adresu email.', 2: '- Kodu pocztowego.'}
    for k,v in menu.items():
        print(k, v)
    choice = ''
    while choice not in ['1', '2']:
        choice = input('Wybierz opcje: ')
    if choice == '1':
        mail = input('\nPodaj adres email: ')
        validate_email(mail)
    else:
        zipC = input('\nPodaj kod pocztowy: ')
        validate_zip(zipC)
    dalej = input('Kontynuowac? (t/n): ')
    if dalej == 'n':
        running = False
