from models.sneaker import Sneaker
from models.order import Order

sneaker1 = Sneaker("Yeezy Boost 700", "Adidas",
["Faded Azure", "Bright Blue", "Kyanite", "Cream", "Utility Black"], 
{"Faded Azure": [11, 11.5, 12, 12.5, 13], "Bright Blue": [8, 8.5, 10, 11.5, 12, 113],
"Kyanite": [9.5, 10.5, 11, 11.5, 13], "Cream": [9.5, 12.5],
"Utility Black": [8.5, 9, 12.5, 13]
})

sneaker2 = Sneaker("Originals Womens Falcon", "Adidas", 
["Crystal White", "Ice Mint", "Black"],
{"Crystal White": [4, 5, 6], 
"Ice Mint": [4, 8], 
"Black": {3, 4, 5, 6, 7}
})

sneaker3 = Sneaker("Air Jordan 1 Retro High OG", "Nike", 
["University Blue", "White/Natural Grey", "White/Blue", "Black/Red"],
{"University Blue": [8, 9, 10, 11, 12, 13],
"White/Natural Grey": [8, 9, 10, 11, 12, 13],
"White/Blue": [9, 10, 11.5, 12, 12.5],
"Black/Red": [8.5, 9, 9.5, 10, 10.5, 11, 11.5, 13]
})



sneaker4 = Sneaker("Sk8-Hi - Led Zeppelin", "Vans", 
["Black/Red", "Black/White"],
{"Black/Red": [6, 6.5, 7, 8, 8.5, 9.5, 10, 11.5],
"Black/White": [5.5, 6.5, 7, 7.5, 8, 9, 10]
})

order1 = Order("Michael Jordan", "23/07/1990", sneaker3, "University Blue", 13, 2)
order2 = Order("Kanye West", "02/02/2017", sneaker1, "Bright Blue", 12, 1)
order3 = Order("Jimmy Page", "01/10/1980", sneaker4, "Black/Red", 11, 2)
order4 = Order("Kylie Jenner", "24/12/2022", sneaker2, "Ice Mint", 8, 1)

orders = [order1, order2, order3, order4]