# An example of a quiz program that reads a quiz file and asks the user the questions
# The quiz file is a text file with the following format:
# question0;correctAnswer;answer01;answer02;answer03;answer04;...;answer0n
# question1;correctAnswer;answer11;answer12;answer13;answer14;...;answer1n
# question2;correctAnswer;answer21;answer22;answer23;answer24;...;answer2n
#
# questionm;correctAnswer;answerm1;answerm2;answerm3;answerm4;...;answermn
# m questions, n answers per question
def generateFile(m,n):
    f = open('quiz.txt','w')
    for i in range(m):
        f.write('question'+str(i)+';')
        f.write('correctAnswer'+str(i)+';')
        # write n answers for the question
        # exclude semicolon in the end of the line
        # write a new line
        for j in range(n):
            f.write('answer'+str(i)+str(j))
            if j < n-1:
                f.write(';')
        f.write('\n')
    f.close()



# define function that reads the file and returns
# a list of questions and
# a list of list of answers
def readQuizFile():
    f = open('quiz.txt','r')
    questions = []
    answers = []
    for line in f:
        # split the line into a list of strings
        lineList = line.split(';')
        # append the question to the list of questions
        questions.append(lineList[0])
        # append the list of answers to the list of answers
        answers.append(lineList[1:len(lineList)-1])
    f.close()
    return questions,answers

#def print the i'th question and the i'th list of answers in random order
#the first line is the question and the lines following are the answers in random order
def printQuestion(i,questions,answers):
    print(questions[i])
    # import the random module
    import random as random
    # shuffle the list of answers
    random.shuffle(answers[i])
    for j in range(len(answers[i])):
        print(str(j+1)+'. '+answers[i][j])


# define function that asks the user a question
# show the possible answers for that question in random order
# and returns true or false depending on the answer is correct or not
def askQuestion(question,answers):
    print(question)
    # import the random module
    import random as random
    # get the correct answer
    correctAnswer = answers[0]
    # shuffle the list of answers
    random.shuffle(answers)
    for i in range(len(answers)):
        print(str(i+1)+'. '+answers[i])
    # ask the user for the answer
    answer = input('Your answer (just write the number): ')
    # check if the answer is correct
    if answers[int(answer)-1] == correctAnswer:
        print('Correct answer!')
        return True
    else:
        print('Wrong answer!')
        return False
# define function that asks the user all the questions
# and returns the number of correct answers
def askAllQuestions(questions,answers):
    correctAnswers = 0
    for i in range(len(questions)):
        if askQuestion(questions[i],answers[i]):
            correctAnswers += 1
    return correctAnswers

# run the quiz in main
def main():
    # generate the quiz file with 10 questions and 5 answers per question
    generateFile(10,5)
    # read the quiz file
    questions,answers = readQuizFile()
    #printQuestion(1,questions,answers)    

    # ask all the questions 
    correctAnswers = askAllQuestions(questions,answers)
    # print the number of correct answers
    print('You have '+str(correctAnswers)+' correct answers!')
main()