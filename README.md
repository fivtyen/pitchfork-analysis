#Pitchfork reviews analysis.

Pitchfork is one of the largest and most popular music websites. It is not only a good source of knowledge for music consumers but it’s also believed to have great influence on the music market, especially indie music (so called ‘Pitchfork Effect’).  Large base of reviews is also a great source of data to analyse -  I decided to collect this data and conduct a simple statistical analysis. 

**Collecting the data.** 

An easy way to gather the data from a website is a web crawler. Because reviews’ section of pitchfork.com has a very clear structure (and so do the reviews themselves) writing a crawler is a simple task. I decided to go with Python and Scrapy. 

Data regarding 18 959 reviews was collected with the crawler. Every reviews was described by:

-	artist (author of the album reviewed)
-	album name
-	genre
-	score
-	merit (‘Best new music’ or ‘Best new reissue’)
-	release year
-	label
-	album cover image URL (I decided to include it despite the fact that I didn’t use it this time)
-	review author 
-	date of the review (split to day, month, year)
-	review URL (again, I didn’t use it really this time but I decided to collect it – maybe for some further use)

**Cleaning the data.**

Gathered data required some work before conducting an analysis – the review’s author name was sometimes misspelled or a different form of a name was used in different reviews i.e.: 

> Edwin "STATS" Houghton', 'Edwin “STATS” Houghton', 'Edwn "STATS" Houghton'

As I had no other idea I decided to manually go through the list of names and create a dictionary that will be then used to make corrections. I’ve found 19 authors which names sometimes required a correction – for each of those authors I chose one of the forms his/her name happened to be written and replaced all other forms with this one. 

clean_data.py is the script used to perform cleaning

**Analysis.** 

For the purpose of analysis I decided to stick to Python – pandas and matplotlib are very handy libraries for dealing with such tasks.  

Results of a very basic statistical analysis can be found in the jupyter notebook.
