"""Restaurant rating lister."""

def read_ratings(filename = open("scores.txt")):

    for line in filename:
        new_line = line.rstrip().split(':')
        restaurant_name = new_line[0]
        restaurant_rating = new_line[1]
        ratings_dictionary[restaurant_name] = ratings_dictionary.get(
            restaurant_name, restaurant_rating)
    
    for restaurant_name, restaurant_rating in sorted(ratings_dictionary.items()):

        print "%s is rated at %s" % (restaurant_name, restaurant_rating)

ratings_dictionary = {}
restaurant_input = raw_input('What is a resturant that you like?')
rating_input = raw_input('What is the restaurant score?')
ratings_dictionary[restaurant_input] = rating_input  
read_ratings()
        



