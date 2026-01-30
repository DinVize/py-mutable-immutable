lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

# --- Блок изменений ---
lucky_number += 1
pi = 3.14159
one_is_a_prime_number = True
name = "Richard Jones"
my_favourite_films.append("Hunert")
profile_info = ("michel", "michel@gmail.com", "12345678", "Ukraine")
marks["Ryan"] = 2
collection_of_coins.add(14)
sorted_variables = {
    "mutable": [
        my_favourite_films,
        marks,
        collection_of_coins,
    ],
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        profile_info,
    ],
}
