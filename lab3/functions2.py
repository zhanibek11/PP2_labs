# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def check_movie(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False

def good_list(movies):
    res = []
    for m in movies:
        if m["imdb"] > 5.5:
            res.append(m)
    return res

def find_by_category(movies, cat):
    res = []
    for m in movies:
        if m["category"].lower() == cat.lower():
            res.append(m)
    return res

def avg_imdb(movies):
    if len(movies) == 0:
        return 0
    total = 0
    for m in movies:
        total += m["imdb"]
    return total / len(movies)

def avg_by_category(movies, cat):
    filt = find_by_category(movies, cat)
    return avg_imdb(filt)


print(check_movie(movies[8]))  
print(good_list(movies))  
print(find_by_category(movies, "Romance"))  
print(avg_imdb(movies))  
print(avg_by_category(movies, "Crime"))  