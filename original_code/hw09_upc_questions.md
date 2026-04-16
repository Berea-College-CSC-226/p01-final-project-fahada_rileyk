# UPC Barcodes

## Instructions

**Replace each `**Replace This With Your Answer**` with your answer**

---

## SECTION 1

1.a. Based on the four steps, which sounds like the hardest to for any computing problem, 
     such as the DNA assignment from last homework?

```
     developing a working algorithm and translating it into code is my hardest challenge
     right now. the DNA assignment already had a strong skeleton structure ready so it wasn't
     very challenging.
```
   
1.b. When the end of CSC 226 comes, what is your next step to becoming a better computer scientist? 
     Or, if computer science isn’t your career aspiration, tell us what is, and what you’ll be doing starting 
     at the end of the semester to achieve that goal.

```
     code a lot on my own. I want to write projects and programs, bad programs. and then make
     them better and find ways to optimize my code more and more.
```

_Return to the Google doc to continue the assignment._

---

## SECTION 2

Use the section below to list out the steps of your code, one step per row. Indicate the expected inputs and desired 
outputs of each step. Again, you are NOT writing code; these should be high order tasks written in plain English 
as shown in the example. Also, don’t forget the test suite you will use to test each task, considering both expected 
and unexpected cases, and the main function. Think fruitful functions!

Add more rows as needed to solve the problem. Sometimes you'll realize a step can be broken down further; 
number them with subnumbers, as shown below (try to avoid going more than 2 deep though!)

2.a. For each section, give a logical function name, and a description of what the function is doing in plain English.

```
        ________________________________________________________________
        Step 1:         Correct input validation
        Function name:  createlist
        Description:    A function that will take input and create a list of numbers that
        I can work with. It needs proper input validation so that it loops the user
        until they give it a 12 digit code with numbers from 0-9

        ________________________________________________________________
        Step 2:         Modulo check character
        Function name:  check_character
        Description:    This function will iterate through the odd positions and 
        add them. and then multiply the result by 3. 
        ________________________________________________________________
            Step 2.a:       
            Function name: check_character
            Description: Next, iterate through the even number positions and add them.
        ________________________________________________________________
            Step 1.b:  
            Function name: check_character
            Description: Add the results and check remainder by 10. 
            If the remainder is 0, that's the check result. if it's
            not 0, then subtract it from 10
        ________________________________________________________________
        Step 3: Converting the input to binary
        Function name:  binary_convert
        Description:    This function will convert the decimal valid input to binary.
        ________________________________________________________________
        Step 4: Invert the code for the right side
        Function name: flip_left
        Description: this function will flip the binary number and invert the 0s to 1s and
        the 1s to 0s. 
        ________________________________________________________________
        Step 5: Joining the code
        Function name:  final_code
        Description:    This function will contain the start code, the left code, the middle code,
        and the inverted right code
        
```

_Return to the Google doc to continue the assignment._

---

## SECTION 3

3.a. Were you able to completely convert the UPC code to using classes? If not, where did you get stuck? 
     If so, what was the most challenging part of the conversion?

```
     Understanding where the self goes was the most challenging part. I still get 
     confused on how to use the self parameter sometimes. 
```

3.b. How did our use of turtles, in particular the Screen class, change with the introduction of classes?

```
   I'm confused as to what this question is asking. As I didn't work with a Screen class
   for my code, as I just used the default turtle screen you get from creating a turtle
   object. However, I did set specific bar height and width so that the barcode 
   was not super thin and was actually scanable. 
```

3.c. (Required only for those who worked with a partner) How well did you and your partner collaborate? Did you leverage
     git to ensure you could both work on the assignment when you were not meeting together? Did you both contribute 
     equally to the assignment? 

```
     **Replace This With Your Answer**
```


3.d. Finally, head to our [Slack channel](https://bereacs.slack.com/archives/C3QACGH8R) and ask a question related to classes and objects. Right click your 
     comment and paste the link to it here.
![Example of how to copy the link from Slack](slack_copy_link.png)

```
     Hi, in my UPC class, the width of the bar and height of the bar never change. I'm using instance variables on self for the bar height and bar width. In this case, would class variables be more useful? What are the implications of using either for something like bar_height and width for my UPC barcode
```
---