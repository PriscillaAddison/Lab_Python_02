#6
primarySchoolAge = 4
legalVotingAge = 18
presidentialAge = 35
retirementAge = 60
personsAge = input(" Enter an age: ")

if personsAge<4:
    print 'Too young'
elif personsAge>=60:
    print 'Too old'
elif personsAge>=35:
    print 'Vote for me'
elif personsAge>=18:
    print 'Remember to vote'
else:
    print "Try again"

print '---'

#7
for i in range(40,-1,-1):
    if i%3==0:
        print i

print '---'

#8
for i in range(6,30,1):
    if i%2!=0:      #  Finding numbers between 6 and 30 that are not divisible by 2
        print i

print '---'

#9

