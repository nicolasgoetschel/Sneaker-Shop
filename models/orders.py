from models.sneaker import Sneaker
from models.order import Order

sneaker1 = Sneaker("Yeezy Boost 700", "Adidas", "Faded Azure",)
sneaker2 = Sneaker("Originals Womens Falcon", "Adidas", "Crystal White")
sneaker3 = Sneaker("Air Jordan 1 Retro High OG", "Nike", "University Blue")
sneaker4 = Sneaker("Sk8-Hi - Led Zeppelin", "Vans", "Black/Red")

order1 = Order("Michael", "Jordan", "23/07/1990", "13", 4, sneaker3)
order2 = Order("Kanye", "West", "02/02/2017", "12", 1, sneaker1)
order3 = Order("Jimmy", "Page", "01/10/1980", "11", 2, sneaker4)
order4 = Order("Kylie", "Jenner", "24/12/2022", "8", 1, sneaker2)

orders = [order1, order2, order3, order4]