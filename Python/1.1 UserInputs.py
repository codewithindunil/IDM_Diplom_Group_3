print('-------WELCOME-------')
name=input('Enter Your Name : ')
subOne=eval(input('Enter Your Sub One Marks : '))
subTwo=eval(input('Enter Your Sub Two Marks : '))
subThree=eval(input('Enter Your Sub Three Marks : '))
subFour=eval(input('Enter Your Sub Four Marks : '))
subFive=eval(input('Enter Your Sub Five Marks : '))

#GETTING TOTAL OF MARKS
total=subOne+subTwo+subThree+subFour+subFive
print('Hello ,',name,' Your Total Is : ',total)

#GETTING AVERAGE
average=total/5
print('Your Average Is : ',average)



if average>75:
    print('You Have A Pass')
elif average>65:
    print('You Have B Pass')
elif average>55:
    print('You Have C Pass')
else:
    print('You Are Fail')
