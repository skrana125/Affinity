!. for file twitterTweets.py
    Assumptions:
        The tweets file is a text file with one tweet per line.
        The racial slurs file is a text file with one slur per line.
        The racial slurs are provided in lowercase and the tweets are normalized to lowercase before checking for matches.
        A racial slur is counted only if it appears as a whole word and not as part of another word (e.g., "butt" is not counted as a slur if "butter" is mentioned in the tweet).
        The profanity score is calculated as the percentage of words in the tweet that are racial slurs.

    example input be like
        tweets.txt:
            I love my job and my coworkers. #happylife
            I can't believe that guy cut me off in traffic. #roadrage
            Just saw the best movie ever! #entertainment
            I hate it when people cut in line. #annoyed
            racial_slurs.txt:
            black
            white
    example out be like
        I love my job and my coworkers. #happylife
        Profanity score: 0.00%

        I can't believe that guy cut me off in traffic. #roadrage
        Profanity score: 0.00%

        Just saw the best movie ever! #entertainment
        Profanity score: 0.00%

        I hate it when people cut in line. #annoyed
        Profanity score: 0.00%


2. for unixsellscript to conver text file into csv file
    #!/bin/bash

# Download the NAVAll.txt file and extract the Scheme Name and Asset Value fields
curl -s "http://amfiindia.com/spages/NAVAll.txt" | sed '1d' | awk -F ';' '{print $4 "," $5}' > output.csv

        Explanation:

        The curl command downloads the contents of the URL.
        The sed command removes the first line of the file, which contains a header row.
        The awk command uses ; as the field separator (-F ';') and prints the 4th and 5th fields (Scheme Name and Asset Value) separated by a comma (',').
        The output is redirected to a file named output.csv.

  Once you save the above script in a file, say extract.sh, you need to make it executable by running the command chmod +x extract.sh. Then you can run it by simply typing ./extract.sh on the command line in the directory where the script file is saved. After the script runs successfully, you should see a new file named output.csv in the same directory with the extracted data in CSV format.
