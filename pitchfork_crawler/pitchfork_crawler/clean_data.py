import pandas as pd


# reading data from csv 
df = pd.read_csv('data.csv')

typos = [['Abby Garnett', 'Abigail Garnett'],
['Alex Lindhart', 'Alex Linhardt', 'Alexander Lloyd Linhardt'],
['Andy O\'Connor', 'Andy O\' Connor'],
['Andy Beta', 'Dr. Andy Beta'],
['Chris Weber', 'Christopher Weber'],
['Cory Byrom', 'Cory D. Byrom'],
['Edwin "STATS" Houghton', 'Edwin “STATS” Houghton', 'Edwn "STATS" Houghton'],
['Jeremy Larson', 'Jeremy D. Larson'],
['Katherine St Asaph', 'Katherine St. Asaph'],
['Kim Shannon', 'Kim Fing Shannon'],
['Mark Richardson', 'Mark Richard-San'],
['Matthew Wellins', 'Matt Wellins'],
['Mia Clarke', 'Mia Lily Clarke'],
['Paul Thompson', 'Paul A. Thompson'],
['P.J. Gallagher', 'PJ Gallagher'],
['Sean Fennessey', 'Sean Fennessy'],
['Seth Colter Walls', 'Seth Colter-Walls'],
['Stephen M. Deusner', 'Stephen M. Duesner', 'Stephen Deusner'],
['Stephen Trouss', 'Stephen Troussé']]

for typo in typos:
    for i in range(1, len(typo)):
        df.review_author = df.review_author.replace(typo[i], typo[0])

df.to_csv('cleaned_data.csv', index = False)