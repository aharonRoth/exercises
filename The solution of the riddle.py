def The_calculations_options_of_the_riddle(dic):
    print("The first general option = three white \n"
        "The second general option = Two black and one white \n" 
        "The third general option = One black and two white" )
    numOption =  int(input("Choose an option from one to seven. (Note that you cannot repeat the same \n" 
                    "option twice in the same program): "))
    arr = []
    while len(arr) < 7:
        if numOption <= 7 and numOption > 0 and numOption not in arr:
            print(dic[numOption])
            arr.append(numOption)
            if numOption == 1:

                print("the second and third know")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("From the fact that the first one did not know, it is proven that the second general possibility is ruled out. The second who sees the third has black, it is proven that the first general possibility has been ruled out. And only the third general option remains. And the second knows that he has white. And the third also knows that he has black. ")

            elif numOption == 2:

                print("only the third knows")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("Since the first does not know, the second general possibility is ruled out. The second sees that the third has white. So the first general option also remains. But the third who sees black in the first realizes that the first general possibility is ruled out, and therefore he knows he has white. ")

            elif numOption == 3:

                print("only the third knows")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("The same idea of case two [only here the third sees the black in the second head and not in the first.] ")

            if numOption == 4:
                
                print("only the third knows")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("Same idea of cases two and three. Only that regarding to the third his knowledge comes from the fact that he sees two blacks. ")

            if numOption == 5:

                print("the second and third know")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("The second knows he has white because he sees two blacks. And the third one realizes that he has black. ")

            if numOption == 6:

                print("everyone knows")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("The first one knows he has white because he sees two blacks. And anyway the others also understand that each of them has a black. ")

            if numOption == 7:

                print("only the third knows")
                answere = input("do you want an explanation? ")
                if answere == "Yes":
                    print("From the fact that the first did not know, it is proved that the second general possibility is ruled out. The second one who saw white, did not know what he had since the other two general options remained. But the third understands that he has white, because if he had black then the second would know that he has white - which is actually the first case - and therefore it is proven that the third has white. ")

            if len(arr) == 7:
                return "you finished Hope you enjoyed."

            numOption =  int(input("Choose an option from one to seven. Note that you cannot repeat the same \n" 
                        "option twice in the same program: "))
                
        if numOption in arr:
            numOption = int(input("Sorry, but you have already selected this option. Choose another option:"))
        else:
            numOption = int(input("Sorry, but This is not a valid number, try again:"))


dic = {
       1 :"first and second white, third black",
       2: "first black, second and third white",
       3: "first white, second black, third white",
       4: "first and second black, third white",
       5: "first black, second white, third black",
       6: "first white, second and third black",
       7: "all white"
       }
The_calculations_options_of_the_riddle(dic)
