# CSC226 Final Project

## Instructions

**Author(s)**: A M Fahad, Boone Riley

**Google Doc Link**: https://docs.google.com/document/d/1N20xMdcSbjpd84dWcVu8vcQWkl0jQD0CLZO8tORZdHM/edit?usp=sharing

---

## Milestone 1: Setup, Planning, Design

**Title**: Berea Quad Store Product Inventory 

**Purpose**: What if we had a Walmart-like store in the middle of the Quad? What if the store told the students
to build them a somewhat functional backend software that is able to keep track of their inventory.

**Source Assignment(s)**: UPC Barcode assignment 

️**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:

    
**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: fahada1
    Branch 2 starting name: rileyk
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

Stack overflow to dig into difference between instances and objects, Stack overflow to dig into connecting
SQL with python

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    Right now I don't feel the best because me and my partner haven't had much time to
    work due to scheduling conflicts but I am confident that we will get it done on time.
    We have been working mostly in long sessions at night in order to make up for it which
    is working but can be tiresome working so late. I think we are doing good, and communication
    will probably be the most important thing for us to get everything done on time.
    
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `50%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    I think our GUI should work. The thing we are struggling with the most is the database and connecting the database
    to the UPC code. We will most likely finish the project. We're going to focus on the database now and
    implementing the UPC. 
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

    1. Run the main.py in PyCharm to open the Berea Quad Walmart! 
    2. Since you've hit run, we're assuming you're a store employee in the Berea Quad Walmart.
    3. Write down any valid UPC and the name of the product, as well as quantity and add product to add it in the system.
    4. If you want to stock in a product that already exists, choose stock in.
    5. To search a product, enter UPC code and click Search Product to find out details about the product.
### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

    1. We wanted to do a scrollbar that can scroll through the products but we didn't have
    the time to implement it.
    2. Ideally, you would want to search with the name of the product. But we found it easier
    to implement a search that uses the UPC to search. That can be a future addition.
    3. It's a small program so it doesn't have any crazy bugs anymore.

### ❗Reflection

❗Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Boone: We selected the project that we did because we thought it would be interesting and
    maybe not so difficult to create a virtual 'Walmart' using the UPC system from a previous
    homework assignment. We also thought the idea of there being a huge walmart in the middle of 
    the quad on campus would be really funny.

    Our final product does not match out inital design exactly but I would say it is about 70%
    of what the intial design was and we ended up having to add and do some things we did not expect.

    I learned a lot from this process with it being the first time I have ever worked on a serious
    coding project. I think the biggest thing I learned not only from this project but the class
    overall is how to effecctively work with other people on assignments and tasks.

    I beleive that having to figure out how to use SQL was the hardest part. We decdied we wanted
    to use an SQL database in our intial design but didn't realize it would be as big of a task. We
    still do not fully understand it but just enough to make it work for this project and connect
    it to our inventory sysytem.

    If we had to do it differently this time the first thing I would do is try to be moree available
    and meet with my partner more often. We haven't ahd the most time to work due to our schedules
    and me heading home most weekends.

    Me and my partner worked well, buit as mentioned above our schedules made it difficult to find
    time to work together. But when we were able to work together we were able to get a lot of work
    done. I enjoyed working with Fahad and I think he was my best partner choice in our class. We
    were both able to work and get along well and I would happily work with him again.
```

```
    Fahad: We selected the project because we wanted to work with the UPC barcodes homework because
    that homework project was really interesting. We thought it would be fun to play around
    with the barcodes and create a system that manages inventory using the barcodes. As we found the
    modulo function that checks the validity of barcodes very interesting and wanted to
    use that. 
    
    The final project is a reflection of about 60-70% of the initial design. It's still not
    complete and it doesn't do many things we wish it could do. For example, being able
    to scan an actual barcode instead of typing out the input would have been really cool. 
    Learning SQL on the go was probably the hardest part of the final project, as none of us
    are still really good at it. Connecting the inventory system to the program was hard. If 
    there's one thing we would do differently next time, that would be spend a lot more time on
    design. The test suite is also not complete yet, and we found it tedious to write tests 
    for the whole thing in such a short amount of time so we were testing functions manually
    on our laptops before committing them. 
    
    I think it was fine working with my partner. We got along well. The only issue was we both
    commit a bunch of code together instead of working in chunks, as we relied on sitting 
    down together and testing things on the laptop to see if they work and then committing piles 
    of code. Maybe that's something we can do differently next time, as Berea schedule made it 
    difficult to find the time to work. But at the end of the day, it turned out okay.  
```

---