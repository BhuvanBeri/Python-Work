#Nesting a list in dictionary in dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"]},
    "India": {"cities_visited": ["Ferozepur", "Faridkot", "Ludhiana"]}
}

#Nesting Dictionary in a list  

travel_log = [
    {"country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {"country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg"]
    },
    {"country": "India", 
    "cities_visited": ["Ferozepur", "Faridkot", "Ludhiana"]
    }
]