Please process the data from the **assignment_01.data** file. You can find it in the Assignment_01 folder in my class GitHub repo.

Use that data to make your bot able to answer the following questions:

1) Who has a \<pet_type>? (e.g. Who has a dog?)

2) Who is \[going to|flying to|traveling to] \<place>? (e.g. Who is flying to Japan?)

    (Your bot should be able to handle all of the verbs above for this question. Assume all people are traveling by plane.)

3) Does \<person> like \<person>? (e.g. Does Bob like Sally?)

4) When is \<person> \[going to|flying to|traveling to\] \<place>?

5) Who likes \<person>?

6) Who does \<person> like?

7) Bonus (5 pts): What's the name of <person>'s <pet_type>? (e.g. What's the name of Mike's dog?)

You code should have a function named answer_question that takes a single string as an argument and prints answers or 
"I don't know" to the screen.

Something similar to this:

```
def answer_question(question_string):
    # your code here
    for answer in answers:
        print answer
```

Your code should also have a function called process_data_from_input_file() that reads in the data from the correct 
input file and stores it for answering questions.

I will import those functions from your script and use them to grade your assignment. Make sure they work please.
 

DO NOT HARDCODE THE DATA. YOUR CODE SHOULD PROCESS THE FILE BY PARSING THE SENTENCES. YOU WILL NOT RECEIVE CREDIT FOR HARDCODED DATA. 
If a question has multiple answers, your bot should print all of them to the screen. 
If you don't have the data to answer a certain question, your bot should print "I don't know" to the screen.

To submit this assignment, please commit and push the code to your GitHub repo. The **answer_question** and 
**process_data_from_input_file** functions should be in a file name **information_extraction.py**. 
It should be in a folder named **Assignment_01** in the root directory.