import random

omriID = 302571773
lidorId = 205622814
nivID = 207992975
eliID = 208676742
ruslanID = 321906497


print('Using Omri ID as seed:')
random.seed(omriID)
questionNumber = random.randint(1,9)
print('First question from questions 1-9:', questionNumber,'\n')

print('Using Lidor ID as seed:')
random.seed(lidorId)
questionNumber = random.randint(10,17)
print('Second question from questions 10-17:', questionNumber,'\n')

print('Using Eli ID as seed:')
random.seed(eliID)
questionNumber = random.randint(18,29)
print('Third question from questions 18-29:', questionNumber,'\n')

print('Using Niv ID as seed:')
random.seed(nivID)
questionNumber = random.randint(18,29)
print('Fourth question from questions 18-29:', questionNumber,'\n')

print('Using Ruslan ID as seed:')
random.seed(ruslanID)
questionNumber = random.randint(30,35)
print('Fifth question from questions 30-35:', questionNumber,'\n')

print('Using Omri ID as seed:')
random.seed(omriID)
questionNumber = random.randint(36,41)
print('Sixth question from questions 36-41:', questionNumber,'\n')