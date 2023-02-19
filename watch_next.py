
import spacy

nlp = spacy.load('en_core_web_md')


# function to find the most similar movie to the already watched movie
def watch_next(description):

    movies = open('movies.txt', 'r')
    movie_list = []

    # split movies into title and description and store in list
    for i in movies:
        movie_list.append(i.split(':'))

    # count number of movies in file
    count = len(movie_list)

    # create list for similarity
    similarity_list = []

    model_sentence = nlp(description)

    for i in range(0, count):
        similarity_list.append(nlp(movie_list[i][1]).similarity(model_sentence))

    max_sim = max(similarity_list)
    max_sim_index = similarity_list.index(max_sim)

    # return the most similar movie
    return movie_list[max_sim_index][0]


# description of Planet Hulk
planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar, where he is sold into slavery and trained as a gladiator."""

print(f"The movie to watch next should be: {watch_next(planet_hulk)}")
