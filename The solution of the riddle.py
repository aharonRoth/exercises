def The_calculations_options_of_the_riddle(First_option, Second_option, Third_option):
    The_first_answer = input("Do you know what color you have? ")
    The_second_answer= input("Do you know what color you have? ")
    The_third_answer = input("Do you know what color you have? ")
    if The_first_answer == "Yes":
        print (Second_option, "And that's when the first one sees two blacks in the heads of the others.") 
    elif  The_first_answer == "No" and The_second_answer == "Yes":
        print (Second_option, "And the second one is white, and he sees the others as black. And so he \n" 
               "knows that he has white.")
    elif The_first_answer and The_second_answer and The_third_answer == "No":
        print (First_option, "That's why no one knews, because everyone saw two whites.")
    elif The_first_answer and The_second_answer == 'No' and The_third_answer == "Yes":
        print (Third_option, "The first sees one black and one white. That's why he doesn't know, \n"
        "because he may also have a black hat. The second one doesn't know because he sees \n"
        "two whites, and if so it may be that he also has a white. But the third understands \n"
        "that since he sees one white and one black then the third option is ruled out. And \n"
        "since the first and second do not know, the second option is ruled out. If so, only the third \n"
        "option remains. And since the third one knows, he must have a white hat. \n"
        "can also be that", Second_option, "The first two saw one white and one black, and that \n"
        "each of them thought that the other didn't know Because the first possibility. But the third sees \n"
        "two blacks. and knows he is white .So that according to these two options. The first knows he is white.")
First_option = "Three white hats were given."
Second_option = "Two black and one white hats were given."
Third_option = "Two white and one black hats were given." 
The_calculations_options_of_the_riddle(First_option, Second_option, Third_option)
