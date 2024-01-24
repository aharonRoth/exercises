def The_punishment(First_punishment, Second_punishment, Third_punishment, The_slaves_answer,  counter):
    if The_slaves_answer == First_punishment:
        for i in range(100):
            print('Here is one of the lashes. ')
            The_slaves_answer = input('Are you ready to endure the continuation of the punishment? ')
            if The_slaves_answer == 'No':
                The_slaves_answer = input('If so, what punishment do you choose? ')
                counter += 1
                The_punishment(First_punishment, Second_punishment, Third_punishment, The_slaves_answer,  counter)
                return
        counter += 1
        if counter == 1:
            print('You only got one punishment.')
            return
        elif counter == 2:
            print('You only got tow punishments.')
            return
    elif The_slaves_answer == Second_punishment:
                    for i in range(10):
                        print('You ate a piece of the fish ')
                        The_slaves_answer = input('Are you ready to endure the continuation of the punishment? ')
                        if The_slaves_answer == 'No':
                            The_slaves_answer = input('If so, what punishment do you choose? ')
                            counter += 1
                            The_punishment(First_punishment, Second_punishment, Third_punishment, The_slaves_answer,  counter)
                            return
                    counter += 1
                    if counter == 1:
                        print('You only got one punishment.')
                        return
                    elif counter == 2:
                        print('You only got tow punishments.')
                        return
    elif The_slaves_answer == Third_punishment:
        counter += 1
        if counter == 1:
            print('You only got one punishment.')
            return
        elif counter == 2:
            print('You only got tow punishment.')
            return
        elif counter == 3:
            print('In the end you got all the punishments')
            return                

counter = 0
First_punishment = '1'
Second_punishment = '2'
Third_punishment = '3'
The_slaves_answer = input('What punishment do you choose? \n'
                          'click 1 to get a hundred lashes. \n'
                          'click 2 to eat the spoiled fish. \n'
                          'click 3 to pay a hundred coins: ')
The_punishment(First_punishment, Second_punishment, Third_punishment, The_slaves_answer,  counter)
