def makeEmailmsg(name):
    return "Hello " + name + '\n' + 'Thank you for attending my dinner'+'\nYours Faithfully,\n'+ 'Haimie'

emailBody=makeEmailmsg('My love')

print(emailBody)