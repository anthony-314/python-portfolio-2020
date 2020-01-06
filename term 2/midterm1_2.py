
import sys


def open_file(file_name,mode):
    """Opens file in the given mode"""
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()




def next_line(the_file):
    """reads the next line in the file and formats it for our program"""
    
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line



def question_block(the_file):
    """ reade the question block from the file and returns
category, question, answers list, correct answer, and explanation"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category,question,answers,correct,explanation


def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to my python Trivia Challenge!\n")
    print("\t\t this test was created by", title, "\n")


def main():
    file_name = get_file_name()
    file = open_file(file_name,"r")
    title = next_line(file)
    name = input("Enter in your full name")
    questions = 0
    score = 0
    category,question,answers,correct,explanation = question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
        userAnswer = input("What's your answer?: ")
            
        if userAnswer == correct:
            score += 1
            questions += 1
            print("correct")
        else:
            questions += 1
            print("Wrong")
        print()
        print(explanation)
        category,question,answers,correct,explanation = question_block(file)
        
    file.close()
    


    print("That was the last question!")
    report_card(name,questions,score)


def get_file_name():
    while True:
        file = input("enter in the name of the test file")
        if ".txt" in file and " " not in file:
            return file
        else:
            print("not a good file name")
            






def report_card(name,questions,score):
    A = """
           #    
          # #   
         #   #  
        #     # 
        ####### 
        #     # 
        #     # """
    B = """
        ######  
        #     # 
        #     # 
        ######  
        #     # 
        #     # 
        ######  """
    C = """
         #####  
        #     # 
        #       
        #       
        #       
        #     # 
         #####  """
    D = """
        ######  
        #     # 
        #     # 
        #     # 
        #     # 
        #     # 
        ######  """
    F = """
        ####### 
        #       
        #       
        #####   
        #       
        #       
        #      """
    
    title = """
######                                        #####                       
#     # ###### #####   ####  #####  #####    #     #   ##   #####  #####  
#     # #      #    # #    # #    #   #      #        #  #  #    # #    # 
######  #####  #    # #    # #    #   #      #       #    # #    # #    # 
#   #   #      #####  #    # #####    #      #       ###### #####  #    # 
#    #  #      #      #    # #   #    #      #     # #    # #   #  #    # 
#     # ###### #       ####  #    #   #       #####  #    # #    # #####  """
    print("**************************************************************************")
    print(title)
    print("**************************************************************************")
    print()
    print()
    print("\tstudent: "+ name)
    print("\tyou answered "+str(score)+"/"+str(questions) +" Correct")
    percent = score / questions * 100
    percent_str = str(percent) + "%"
    point_per_question = (100/questions)
    totalpoints = point_per_question*questions
    totalscore = point_per_question*score
    print("\teach question was worth "+str(point_per_question)+ " points")
    print("\tyou received "+str(totalscore) +"/"+str(totalpoints) +" points")
    print("\tyou got a " + percent_str)
    if percent >= 90:
        print(A)
        print()
        print("\tGreat job")
    elif percent < 90 and percent >= 80:
        print(B)
        print()
        print("\tnot to bad")
    elif percent < 80 and percent >= 70:
        print(C)
        print()
        print("\tOK")
    elif percent < 70 and percent >= 60:
        print(D)
        print()
        print("\ttry harder")
    elif percent < 60:
        print(F)
        print()
        print("\tRealy try harder")
    print()
    print("**************************************************************************")
        
    
    

main()
    
     
    
    
    

    






















