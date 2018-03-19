from information_extraction import answer_question, process_data_from_input_file

def question_answers(question):
    print '================================='
    print 'Question:  ' + question
    try:
        answer_question(question)
    except Exception as e:
        print 'Failed to answer this question.'
    print '\n'

process_data_from_input_file('assignment_01_grader.data')


question_answers('Who has a dog?') # Bob, Mary, Zach
question_answers('Who is traveling to Japan?') # Sally
question_answers('Who is going to France?') # Bob and Mary
question_answers('Does Bob like Mary?') # Yes
question_answers('When is Sally flying to Mexico?') # In 2020
question_answers('When is Chris traveling to Peru?') # on April 20th
question_answers('Who likes Mary?') # Joe, Bob, Sally, [Chris], Zach
question_answers('Who likes Sally?') # Mary, [Carl]
question_answers('Who likes Michael?') # I don't know.
question_answers('Who does Chris like?') # [Bob, Joe, Mary]
question_answers('Who does Bob like?') # Mary, [Chris]
question_answers("What's the name of Mary's dog?") # Rover

question_answers("Who does Carl like?") # Zach, Mike, Joe, Sally
question_answers("Who likes Zach?") # Carl
question_answers("When is Carl going to Africa?") # In the spring of next year
question_answers("What's the name of Zach's dog?") # Buttercup