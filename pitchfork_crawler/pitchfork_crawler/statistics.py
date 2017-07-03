import pandas as pd
import matplotlib.pyplot as plt


# general sats
def calculate_general_statistics(data): 
    number_of_artist = len(data.artist.unique())
    number_of_reviews = len(data)
    print('--- GENERAL STATISTICS ---')
    print(' Number of reviews: {}\n Unique artists: {}'.format(number_of_reviews, number_of_artist))

    
# overall score statistics    
def calculate_score_statistics(data):
    q1 = data.score.quantile(0.25)
    q2 = data.score.quantile(0.5)
    q3 = data.score.quantile(0.75)
    mean = data.score.mean()
    maximum = data.score.max()
    minimum = data.score.min()
    top_scores = data.score.value_counts()
    print('--- SCORE STATISTICS ---')
    print(' Quartile 1: {}\n Quartile 2 (median): {}\n Quartile 3: {}\n Mean: {}\n Min: {}\n Max: {}'.format(q1, q2, q3, mean.round(2), minimum, maximum))
    print('\nTop scores:\n{}'.format(top_scores))

    
# score histogram
def plot_score_histogram(data):
    plt.figure()
    plt.hist(data.score, bins = 50)
    plt.title('Score histogram')
    plt.xlabel('Score')
    plt.ylabel('Number of albums')
    plt.savefig('charts/score_histogram.png')
    print('\n Score histogram saved!\n')
      
      
# reviews/year plot
def plot_num_reviews(data):
    plt.figure()
    data.review_date_year.value_counts(ascending = True).plot(kind='bar')
    plt.title('Number of albums reviewed each year')
    plt.xlabel('Year')
    plt.ylabel('Number of albums')
    plt.savefig('charts/albums_year_plot.png')
    print('\nreviews/year chart saved!\n')
    
    
# statistics regarding reviews' authors
def calculate_authors_statistics(data):
    number_of_authors = len(data.review_author.unique())
    top_authors_names = data.review_author.value_counts()[:10].keys()
    top_authors_numbers = data.review_author.value_counts()[:10]
    print('--- AUTHORS\' STATISTICS ---')
    print('Number of authors: {}\nTop authors:\n{}\n'.format(number_of_authors, top_authors_numbers))
    for author in top_authors_names:
        plt.figure()
        d = data[data.review_author == author]
        plt.hist(d.score, bins = 50)
        plt.title('Score histogram - {}'.format(author))
        plt.xlabel('Score')
        plt.ylabel('Number of albums')
        plt.savefig('charts/score_histogram_{}.png'.format(author))
    print('\nAuthors\' histograms saved!\n')
    
    
# statistics regarding artists
def calculate_artist_statistics(data):
    number_of_artists = len(data.artist.unique())
    top_artists_names = data.artist.value_counts()[:10].keys() 
    top_artists_numbers = data.artist.value_counts()[1:11] # excluding 'various artists' from the list
    print('--- ARTISTS\' STATISTICS ---')
    print('Number of artists: {}\ntop artists:\n{}\n'.format(number_of_artists, top_artists_numbers))
    
    
def main(): 
    df = pd.read_csv('cleaned_data.csv', encoding = "ISO-8859-1")
    calculate_general_statistics(df)
    calculate_score_statistics(df)
    plot_score_histogram(df)
    calculate_authors_statistics(df)
    plot_num_reviews(df)
    calculate_artist_statistics(df)
    
if __name__ == '__main__':
    main()
    