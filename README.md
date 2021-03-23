# LT2222 V21 Assignment 2

Assignment 2 from the course LT2222 in the University of Gothenburg's winter 2021 semester.

Your name: KAMANEH 

Part 1 - preprocessing:

To preprocess the text I separated each line and filtered column two, to remove all the none alphabetic, and then stemming and Lemmatizing and make them lowercase.
Then I tried to remove the punctuation with re library. After all filtering, I saw there are some empty spaces, so I tried to filter those lines and add the other lines to the cliean_row list.
Then I created a list that was mentioned in the assignment as my column-names.
Then I return the data as a matrix which I created by using the pandas library.


Part 2 - Creating instances:

For doing this part I decided to keep the entities as a feature.
For creating a collection of Instance objects I did these steps:
-First I put each column (sentence number, word, type) in the specific list. Then I made a list of triple tuples.
-Then I tried to find which entity is beginning with B then replace the B- with empty space.
-For finding the 5 features before and after the word with a NE, I tried to check them in range the one to six:
then I checked them for the positive indexes If they were in the same sentence, add them to the list of features,
else, put the start tag " which I choose as <s>" and for the end tags "<e>".Here I don't use the end tags and start tags with different numbers.

And at the end, we put all features with the classes in the instances list.


Part 3 - Creating the table and splitting:

In this part, I tried to create a reduced matrix from the instances. A matrix that takes the name of its columns from the features.
For preparing the data,I just count the unique words in the features and neclasses in instances.
 
Then I used to reduce the matrix to reduced it, Then I split the matrix into training and testing sets and train and random with an 80% fraction.

Part 5 - Evaluation:

Then I used a confusion matrix for evaluating the machine. But I didn't get a very good result so I repeated the code to get the better result, which I think is because they were(my data) not classified as they should. 
