# travel log

# # nesting a list in dictionary
# travel_log={
#     "France": ["Paris", "Lyon", "Marseille"],
#     "Germany": ["Berlin", "Munich", "Frankfurt"],
#     "Spain": ["Madrid", "Barcelona", "Valencia"],
# }

# # nesting a dictionary in a dictionary
# travel_log={
#     "France": {"Berlin":"2", "Paris":"1", "Lyon":"3"},
#     "Germany": {"Berlin":"1", "Munich":"2", "Frankfurt":"3"},
#     "Spain": {"Madrid":"1", "Barcelona":"2", "Valencia":"3"},
# }


# travel_log={
#     "France": {"cities_visited":["Paris","Lille","Dijon"]},
#     "Germany": {"cities_visited":["Berlin","Munich","Frankfurt"]},
#     "Spain": {"cities_visited":["Madrid","Barcelona","Valencia"]},
# }

# print(travel_log["France"]["cities_visited"])


travel_log = [
    {
        "country": "France",
        "times_visited": 2,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "times_visited": 3,
        "cities_visited": ["Berlin", "Munich", "Frankfurt"],

    },
    {
        "country": "Spain",
        "times_visited": 1,
        "cities_visited": ["Madrid", "Barcelona", "Valencia"],
    }]
# function to add new country and city


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["times_visited"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 3, ["Moscow", "Saint Petersburg", "Kazan"])
print(travel_log)
