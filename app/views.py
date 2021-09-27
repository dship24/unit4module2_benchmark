from django.shortcuts import render
from dataclasses import dataclass
from typing import List

@dataclass
class Anime():
    name: str
    genre: str
    description: str
    characters: List[str]

def anime(request, anime):
    context = {
        "name": anime,
        "animes" : {
            "Jujutsu Kaisen": Anime("Jujutsu Kaisen", "Shonen/Action", "Yuji Itadori must rid the world of curses while also becoming one himself. He must learn the true powers that he has acquired to vanquish the evil that lies within his world.", ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugasaki", "Satoru Gojo", "Aoi Todo", "Sukuna", "Geto"]),
            "Naruto": Anime("Naruto", "Shonen", "Naruto Uzumaki is just a small boy with a big dream of becoming hokage of his village one day. He must test the limits of his power and battle many dangerous foes on his journey to the top.", ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Rock Lee", "Shikamaru Nara", "Orochimaru"]),
            "Hunter X Hunter" : Anime("Hunter X Hunter", "Adventure/Action", "Gon Freecss is a young boy on a quest to search for his father. He must explore the world of hunters and overcome the challenges and puzzles that await him.", ["Gon Freecss", "Killua Zoldyck", "Kurapika Kurta", "Leorio Paradinight", "Hisoka Morow", "Ging Freecss"]),
            "Rascal Does Not Dream of a Bunny Girl Senpai" : Anime("Rascal Does Not Dream of a Bunny Girl Senpai", "Romance", "Sakuta Azusagawa is just a teenage boy with a semi-normal life until he meets Mai Sakurajima. Now, he must uncover the mysteries of Adolescense Syndrome and help his closest friends.", ["Sakuta Azusagawa", "Mai Sakurajima", "Kaede Azusagawa", "Rio Futaba", "Shoko Makinohara", "Nodoka Toyohama"]),
            "No Game No Life" : Anime("No Game No Life", "Action", "Sora and Shiro are sent to a different world where everything is decided by games. They must save all of Imanity from extinction and defeat the god of the new world, Tet.", ["Sora", "Shiro", "Stephanie Dola", "Jibril", "Tet", "Chlammy Zell"]),
            "Your Lie in April" : Anime("Your Lie in April", "Romance/Slice of Life", "Kousei Arima is a young boy who is very gifted at piano however, in recent months, he has been unable to perform. He must regain the courage from the help of his friends to dazzle the world once again.", ["Kousei Arima", "Kaori Miyazono", "Tsubuka Sawabe", "Ryota Watari"])
        }
    }
    return render(request, "anime.html", context)

def root(request):
    context = {
        "animes" : {
            "Jujutsu Kaisen" : "jjk",
            "Naruto" : "naruto",
            "Hunter X Hunter" : "hxh",
            "Rascal Does Not Dream of a Bunny Girl Senpai" : "bgs",
            "No Game No Life" : "ngnl",
            "Your Lie in April" : "ylia"
        }
    }
    return render(request, "home.html", context)