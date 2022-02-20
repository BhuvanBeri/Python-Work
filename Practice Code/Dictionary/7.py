travel_log = [
    {"country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {"country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg"],
    "total_visits": 1
    },
    {"country": "India", 
    "cities_visited": ["Ferozepur", "Faridkot", "Ludhiana"],
    "total_visits": 15
    },
]

def add_new_country(country_visited, cities_visited, total_visits):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["visits"] = total_visits
    travel_log.append(new_country)

add_new_country = ("Russia", ["Moscow"], 2)

print(travel_log)