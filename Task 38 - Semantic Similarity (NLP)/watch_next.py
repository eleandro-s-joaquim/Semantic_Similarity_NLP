'''
Compulsory Task 2
    Let us build a system that will tell you what to watch next based on the word
    vector similarity of the description of movies.
        ● Create a file called watch_next.py
        ● Read in the movies.txt file. Each separate line is a description of a different
        movie.
        ● Your task is to create a function to return which movies a user would watch
        next if they have watched Planet Hulk with the description “Will he save
        their world or destroy it? When the Hulk becomes too dangerous for the
        Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
        planet where the Hulk can live in peace. Unfortunately, Hulk land on the
        planet Sakaar where he is sold into slavery and trained as a gladiator.”
        ● The function should take in the description as a parameter and return the
        title of the most similar movie.
        ● Host your solution on a Git host such as GitLab or GitHub.
            ○ Remember to exclude any venv or virtualenv files from your repo.
        ● Add the link for your remote Git repo to your semantic_similarity.txt file.

    https://github.com/meljarad/HyperionDevSEBootcamp/tree/main/T38
'''

import spacy
from tabulate import tabulate


# This function returns a list of movies and their descriptions by reading them in from the text file 'movies.txt'.
def import_movies_list():
    with open('movies.txt', 'r') as file:
        # Uses list comprehension to remove the line breaks from each line
        movies_as_list = [line.strip() for line in file]

    # Converts the list of movies to a list of dicts with the movie name and description stores as values
    movies_as_dicts = []
    for movie in movies_as_list:
        movies_as_dicts.append({'Name': movie.split(":")[0], 'Description': movie.split(":")[1]})

    return movies_as_list, movies_as_dicts

# This function returns recommendation scores for a list of movies based on the
# description of the last watched movie.
def recommend_movie(last_watched_movie_description, movies_as_dicts):

    # Reads in the description of Planet Hulk and finds the similarity scores with the other movies.
    headers = ["Movie:", "Similarity:"]
    similarity_data = []
    similarity_dict_list = []
    watched_movie_desc_token = nlp(last_watched_movie_description)
    movie_descriptions_list = [list(movie_dict.values())[0] for movie_dict in movies_as_dicts]

    # Loops through the list of movies and calculates their similarity score based on the description
    for movie in movies_as_dicts:
        movie_similarity_score = round(nlp(movie['Description']).similarity(watched_movie_desc_token)*100,0)
        similarity_data.append([movie['Name'], str(movie_similarity_score) + '%'])
        similarity_dict_list.append({'Name': movie['Name'], 'Similarity': movie_similarity_score})

    print(tabulate(similarity_data, headers=headers, tablefmt="simple_outline"))

    # Extracts movie which is most similar based on description
    max_similarity_score = 0
    recommended_movie_name = ""
    for movie in similarity_dict_list:
        if movie['Similarity'] > max_similarity_score:
            max_similarity_score = movie['Similarity']
            recommended_movie_name = movie['Name']
    return recommended_movie_name, max_similarity_score

# Loads the medium-sized English language model used for NLP capabilities
nlp = spacy.load('en_core_web_md')

watched_movie = {'Name': 'Planet Hulk',
                 'Description': 'Will he save their world or destroy it? '
                                'When the Hulk becomes too dangerous for the Earth, '
                                'the Illuminati trick Hulk into a shuttle and launch him'
                                ' into space to a planet where the Hulk can live in peace. '
                                'Unfortunately, Hulk land on the planet Sakaar where he is '
                                'sold into slavery and trained as a gladiator.'
                 }

# Import the list of movies
movies_as_list = import_movies_list()[0]
movies_as_dicts = import_movies_list()[1]

recommendation_stats = recommend_movie(watched_movie['Description'], movies_as_dicts)
recommended_movie_name = recommendation_stats[0]
max_similarity_score = recommendation_stats[1]

# Print recommendation to the user
print(f"Based on your last watched movie {watched_movie['Name']}:\nOur algorithm recommends you watch\n"
      f"{recommended_movie_name}next, with a recommendation score of {max_similarity_score:.0f}%!")

"""
References Used:

Most code was obtained help in some conversations and doubts via APP DISCORD
from the HyperionDev Software Engineering student group.
#---------------------------------------------------------------------------------#
SE T38 - Semantic Similarity (NLP).pdf
SE T38 - Semantic Similarity (NLP) video
https://youtu.be/IB9m-2x88TI
Author : HyperionDev 2023.
#---------------------------------------------------------------------------------#
Reference: Site W3 Schools Python/
https://www.geeksforgeeks.org/
#---------------------------------------------------------------------------------#
Reference: Real Python
https://realpython.com/natural-language-processing-spacy-python/
#---------------------------------------------------------------------------------#
"""