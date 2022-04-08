print('welcome to my quiz')

playing=input('Do you want to play ? ')

if playing.lower() != 'yes':
    quit()

print('Okay! lets play :)')
score=0

ans=input('What does CPU stand for ? ').lower()
if ans=='central processing unit':
    print('Correct!')
    score+=1
else :
    print('Incorrect!')

ans=input('What does GPU stand for ? ').lower()
if ans=='graphics processing unit':
    print('Correct!')
    score+=1
else :
    print('Incorrect!')

ans=input('What does RAM stand for ? ').lower()
if ans=='random access memory':
    print('Correct!')
    score+=1
else :
    print('Incorrect!')

ans=input('What does PSW stand for ? ').lower()
if ans=='power supply unit':
    print('Correct!')
    score+=1
else :
    print('Incorrect!')

print('you got '+str(score)+' questions correct!')
print('you got '+str((score/4)*100)+'%.')

