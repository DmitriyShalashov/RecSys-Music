from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
def top_k():
    history = [
        [0.58, 0.26, 1., 0.99, 0.99, 0.55, 0.14, 1., 1., 1., 0.29,
                1., 0.95, 1., 1., 0.2, 0.99, 0.07, 1., 0.99, 0.09, 0.86,
                0.95, 0.99, 0.91, 0.92, 1., 0.98, 0.96, 0.22, 0.79, 0.96, 0.91,
                0.31, 0.2, 0.98, 0.22, 1., 0.97, 0.69, 0.06, 1., 0.44, 0.98],
               [0.01, 0.14, 0.35, 0.09, 0.93, 0.07, 0.55, 0.51, 0.47, 0.85, 0.09,
                0.27, 0.34, 0.78, 0.33, 0.11, 0.24, 0.01, 0.56, 0.69, 0.03, 0.02,
                0.07, 0.08, 0.48, 0.03, 0.74, 0.42, 0.18, 0.38, 0.35, 0.23, 0.04,
                0.19, 0.36, 0.12, 0.61, 0.99, 0.18, 0.42, 0.04, 0.08, 0.1, 0.53],
               [0.01, 0.09, 0.03, 0.53, 0.15, 0., 0.22, 0.82, 0.3, 0.22, 0.02,
                0.14, 0.04, 0.56, 0.16, 0.27, 0.13, 0., 0.56, 0.15, 0.05, 0.12,
                0.05, 0.05, 0.2, 0.06, 0.41, 0.04, 0.05, 0.03, 0.28, 0.03, 0.35,
                0.13, 0.17, 0.01, 0.56, 0.76, 0.09, 0.07, 0.06, 0.08, 0.14, 0.08],
               [0.22, 0.03, 0.16, 0.15, 0.65, 0.03, 0.04, 0.95, 0.26, 0.17, 0.06,
                0.19, 0.24, 0.3, 0.89, 0.25, 0.06, 0.04, 0.4, 0.34, 0.17, 0.17,
                0.11, 0.05, 0.29, 0.16, 0.4, 0.12, 0.1, 0.26, 0.04, 0.21, 0.01,
                0.28, 0.04, 0.04, 0.15, 0.98, 0.36, 0.12, 0.05, 0.82, 0.05, 0.25],
               [0.02, 0.27, 0.34, 0.37, 0.99, 0.51, 0.95, 0.99, 0.51, 1., 0.18,
                0.44, 0.91, 0.97, 0.96, 0.37, 0.1, 0.15, 0.85, 0.86, 0.46, 0.06,
                0.34, 0.09, 0.91, 0.21, 0.95, 0.64, 0.46, 0.6, 0.92, 0.85, 0.41,
                0.45, 0.4, 0.57, 0.94, 1., 0.2, 0.87, 0.05, 0.92, 0.73, 0.4],
               [0.01, 0.02, 0.1, 0.67, 0.99, 0.08, 0.53, 0.98, 0.98, 0.71, 0.01,
                0.23, 0.53, 0.99, 1., 0.9, 0.23, 0., 0.63, 0.31, 0.08, 0.49,
                0.02, 0.03, 0.16, 0.04, 0.54, 0.16, 0.03, 0.45, 0.88, 0.01, 0.19,
                0.12, 0.02, 0.06, 0.16, 0.99, 0.13, 0.06, 0.04, 0.78, 0.11, 0.02],
               [0.01, 0.14, 0.08, 0.25, 0.96, 0.17, 0.75, 1., 0.16, 0.99, 0.09,
                0.06, 0.96, 0.98, 0.67, 0.49, 0.23, 0.11, 0.2, 0.33, 0.36, 0.04,
                0.35, 0.22, 0.62, 0.01, 0.93, 0.12, 0.43, 0.79, 0.76, 0.52, 0.08,
                0.29, 0.41, 0.5, 0.89, 1., 0.06, 0.05, 0.01, 0.55, 0.04, 0.03],
               [0.38, 0.06, 0.46, 0.92, 1., 0.2, 0.11, 0.99, 1., 0.98, 0.4,
                0.59, 0.29, 0.99, 1., 0.9, 0.57, 0.06, 1., 0.26, 0.51, 0.57,
                0.92, 0.42, 0.14, 0.76, 0.69, 0.76, 0.46, 0.7, 0.87, 0.92, 0.15,
                0.57, 0.1, 0.75, 0.32, 1., 0.61, 0.65, 0.18, 0.89, 0.8, 0.64],
               [0.03, 0.1, 0.02, 0.45, 0.02, 0.03, 0.25, 0.88, 0.52, 0.38, 0.02,
                0.13, 0.7, 0.91, 0.55, 0.86, 0.13, 0.02, 0.64, 0.02, 0.12, 0.22,
                0.01, 0.19, 0.53, 0.1, 0.78, 0.12, 0.26, 0.04, 0.26, 0.12, 0.05,
                0.68, 0.35, 0.06, 0.45, 0.88, 0.22, 0.22, 0.03, 0.62, 0.65, 0.07],
               [0.04, 0.1, 0.88, 0.26, 1., 0.58, 0.97, 0.99, 1., 1., 0.16,
                0.69, 0.99, 1., 1., 0.95, 0.95, 0.11, 0.99, 0.85, 0.85, 0.35,
                0.48, 0.75, 0.98, 0.45, 0.77, 0.9, 0.94, 0.96, 0.99, 0.71, 0.07,
                0.14, 0.14, 0.89, 0.75, 1., 0.27, 0.96, 0.16, 0.85, 0.97, 0.31],
               [0.03, 0.04, 0.27, 0.13, 0.18, 0.01, 0.4, 0.72, 0.78, 0.59, 0.04,
                0.44, 0.15, 0.88, 0.6, 0.66, 0.71, 0., 0.65, 0.01, 0.19, 0.14,
                0.02, 0.09, 0.14, 0.08, 0.68, 0.07, 0.54, 0.01, 0.07, 0.16, 0.08,
                0.09, 0.01, 0.15, 0.41, 0.3, 0.03, 0.07, 0.08, 0.59, 0.11, 0.16]]
    tracks_filtered=[2, 3, 9, 11, 13, 14, 15, 17, 18, 19, 22, 24, 27,
        30, 33, 35, 36, 38, 39, 42, 43, 48, 49, 51, 52, 54, 55, 57, 59, 60, 62, 63,
        65, 66, 67, 68, 72, 73, 87, 90, 91, 92, 98, 99]
    user_rec =[x for x in zip(history[0],tracks_filtered)]
    user_rec.sort(key=lambda x:x[0],reverse=True)
    print(user_rec)
    top_10=user_rec[:10]
    top_20=user_rec[:20]

    return {
        "top_10":top_10,
        "top20":top_20
    }


def tracks_process(tracks_ids):
    res=[]
    for id in tracks_ids:
        res.append({"name":tracks[id[1]]})

    return res


class RecommendationApi(APIView):
    def get(self, request, **kwargs):
        userName = kwargs["name"]

        if userName == "Alex":
            return Response(data={
                "tracks": tracks_process(top_k()["top_10"])
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "tracks": tracks_process(top_k()["top_10"]),
                "users": users
            }, status=status.HTTP_200_OK)








tracks=['The Weeknd – "Blinding Lights"' ,
'Dua Lipa – "Levitating"' ,
'Olivia Rodrigo – "drivers license"' ,
'BTS – "Dynamite"' ,
'Justin Bieber – "Peaches" (ft. Daniel Caesar, Giveon)' ,
'Billie Eilish – "Bad Guy"' ,
'Lil Nas X – "MONTERO (Call Me By Your Name)"' ,
'Doja Cat – "Say So"' ,
'Harry Styles – "Watermelon Sugar"' ,
'Drake – "God’s Plan"' ,
'Ed Sheeran – "Shape of You"' ,
'Cardi B – "WAP" (ft. Megan Thee Stallion)' ,
'Ariana Grande – "Positions"' ,
'Post Malone – "Circles"' ,
'Travis Scott – "SICKO MODE"' ,
'Maroon 5 – "Memories"' ,
'Lizzo – "Truth Hurts"' ,
'Taylor Swift – "Cardigan"' ,
'Shawn Mendes – "Señorita" (ft. Camila Cabello) ' ,
'SZA – "Good Days"' ,
'Silk Sonic – "Leave The Door Open"' ,
'Kanye West – "Stronger"' ,
'Rihanna – "Umbrella" (ft. JAY-Z)' ,
'Bruno Mars – "24K Magic"' ,
'Tones And I – "Dance Monkey"' ,
'Katy Perry – "Roar"' ,
'Imagine Dragons – "Believer"' ,
'Khalid – "Talk"' ,
'Camila Cabello – "Havana" (ft. Young Thug)' ,
'Lil Nas X – "Old Town Road" (ft. Billy Ray Cyrus)' ,
'Lady Gaga – "Shallow" (with Bradley Cooper)' ,
'Beyoncé – "Single Ladies (Put a Ring on It)"' ,
'Shakira – "Hips Don’t Lie" (ft. Wyclef Jean)' ,
'Eminem – "Lose Yourself"' ,
'Justin Timberlake – "Can’t Stop The Feeling!"' ,
'Macklemore & Ryan Lewis – "Thrift Shop" (ft. Wanz)' ,
'Avicii – "Wake Me Up"' ,
'Pharrell Williams – "Happy"' ,
'Luis Fonsi – "Despacito" (ft. Daddy Yankee)' ,
'Black Eyed Peas – "I Gotta Feeling"' ,
'DJ Snake, Lil Jon – "Turn Down For What"' ,
'Ellie Goulding – "Love Me Like You Do"' ,
'Major Lazer – "Lean On" (ft. MØ & DJ Snake)' ,
'Calvin Harris – "This Is What You Came For" (ft. Rihanna) ' ,
'David Guetta – "Titanium" (ft. Sia)' ,
'The Chainsmokers – "Closer" (ft. Halsey)' ,
'Flo Rida – "Good Feeling"' ,
'Wiz Khalifa – "See You Again" (ft. Charlie Puth)' ,
'Adele – "Rolling in the Deep"' ,
'Sam Smith – "Stay With Me"' ,
'John Legend – "All of Me"' ,
'Coldplay – "Viva La Vida"' ,
'Maroon 5 – "Sugar"' ,
'Ed Sheeran – "Perfect"' ,
'Shawn Mendes – "In My Blood"' ,
'Justin Bieber – "Sorry"' ,
'Ariana Grande – "7 Rings"' ,
'Selena Gomez – "Lose You to Love Me"' ,
'Drake – "In My Feelings"' ,
'Halsey – "Without Me"' ,
'Lorde – "Royals"' ,
'Zedd – "The Middle" (ft. Maren Morris, Grey)' ,
'Kygo & Whitney Houston – "Higher Love"' ,
'Marshmello – "Happier" (ft. Bastille)' ,
'DJ Khaled – "Im The One" (ft. Justin Bieber, Quavo, Chance the Rapper, Lil Wayne)' ,
'J Balvin, Willy William – "Mi Gente"' ,
'Bad Bunny – "DÁKITI" (ft. Jhay Cortez)' ,
'Rosalía – "Con Altura" (ft. J Balvin)' ,
'Ozuna – "Baila Baila Baila"' ,
'Cardi B – "I Like It" (ft. Bad Bunny & J Balvin)' ,
'Lil Uzi Vert – "XO TOUR Llif3"' ,
'Juice WRLD – "Lucid Dreams"' ,
'Future – "Mask Off"' ,
'Migos – "Bad and Boujee" (ft. Lil Uzi Vert)' ,
'Pop Smoke – "Dior"' ,
'Roddy Ricch – "The Box"' ,
'Megan Thee Stallion – "Savage Remix" (ft. Beyoncé)' ,
'Playboi Carti – "Magnolia"' ,
'21 Savage – "Bank Account"' ,
'A$AP Rocky – "Praise the Lord (Da Shine)" (ft. Skepta)' ,
'Kendrick Lamar – "HUMBLE."' ,
'Childish Gambino – "This Is America"' ,
'Frank Ocean – "Thinkin Bout You"' ,
'Anderson .Paak – "Come Down"' ,
'Bryson Tiller – "Exchange"' ,
'Travis Scott – "Goosebumps" (ft. Kendrick Lamar)' ,
'Rae Sremmurd – "Black Beatles" (ft. Gucci Mane)' ,
'Fetty Wap – "Trap Queen"' ,
'Young Thug – "The London" (ft. J. Cole & Travis Scott)' ,
'Lil Baby – "Drip Too Hard" (ft. Gunna)' ,
'DaBaby – "Rockstar" (ft. Roddy Ricch)' ,
'Gunna – "Top Off"' ,
'Summer Walker – "Girls Need Love" (with Drake)' ,
'Sia – "Chandelier"' ,
'Ellie Goulding – "Burn"' ,
'The Weeknd – "Starboy" (ft. Daft Punk)' ,
'Khalid – "Location"' ,
'J. Cole – "Middle Child"' ,
'The Kid LAROI & Justin Bieber – "Stay"' ,
'Clean Bandit – "Rather Be" (ft. Jess Glynne)' ,
]
users=[("Maria", 0.64), ("Michael", 0.61),
       ("John", 0.68)]