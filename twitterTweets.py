""" Imagine there is a file full of Twitter tweets by various users and you are provided
a set of words that indicates racial slurs. 
Write a program that can indicate the degree of profanity for each sentence in the file. 
Write in any programming language (preferably in Python) - make any assumptions, 
but remember to state them. """

import re

def score(tweets, racial_slurs):
    # Count he number of racial slur in the tweets
    count  = 0
    for slur in racial_slurs:
        count += len(re.findall(r"\b" + slur + r"\b" + tweets, re.IGNORECASE))

    # Calculate the profanity score as a percentage of total words
    words =  tweets.split()
    total_words = len(words)
    if total_words == 0:
        return 0
    else:
        return 100*count/total_words


def main():
    # load the racial slur
    with open("racial_slur.txt", "r") as f:
        racial_slur = [line.strip() for line in f]
    
    # load the tweets
    with open("tweets.txt","r") as f:
        tweets = [line.strip() for line in f]

    # calculate the prfanity score for each tweets and print it out
    for tweet in tweets:
        total_score = score(tweets, racial_slurs)
        print(f"{tweet}\nProfanity Score : {total_score:.2f}%\n")


if __name__ == "__main__":
    main()