import random
Elements = ("Vent","Feu","Eau") #Vous Pouvez En Rajouté Ou Supprimer 
running = True #Il Sert a Faire Tourner Le Jeu
Points = 0 #Vous Pouvez Tricher Si sa vous fait plsaisir :)
Streaks = 0 #Vous Pouvez Tricher Si sa vous fait plasiri :)

#Description: 
#Ceci Est Un Mini Projet Que J'ai Fais Moi Même Pour M'Amuser ,Ceci Est Un Simple Jeu de Type Pierre Feuille Ciseaux en Python Il ya quelque Easter Eggs Dans Les Messages De Victoire Defaite et Egalité... A toi les Trouvé
#Ah Oui N'hesite Pas A Voir Mes Autres Projets Sur Github et Cie. 
#Sa Suffit Les Blabla Amusez Vous Bien 


# Messages d'égalité
messages_egalite = [
    "⚔ Les forces s'équilibrent... Impossible de départager cette manche !",
    "🌍 Égalité parfaite ! La nature elle-même hésite !",
    "🤝 Un duel sans vainqueur ! Qui prendra l'avantage au prochain tour ?",
    "🐲Les forces s’équilibrent… Rejouez pour trancher le destin !🐲",
    "⚖️ Aucune victoire, aucune défaite... Le destin semble indécis !⚖️ ",
    "🌀Une égalité pure et parfaite. Tout peut encore arriver !",
    "🙈🙉🙊Sussy Baka🙈🙉🙊",
    "Aucun vainqueur aujourd’hui… mais qui sait ce que le futur réserve ?",
    "🌞La nature de la bataille refuse de choisir… L’égalité prévaut.🌞"
]
# Messages De Défaite
message_defaite = ["💠 La victoire t'a échappé… Cette fois, la chance n'était pas de ton côté.💠",
" 🔰Ton adversaire a été plus rapide, plus malin. Tu t’inclines cette fois !🔰",
"⚜️ Un échec cruel… La prochaine fois, ce sera différent.",
"⚠️⚠️ La partie s’est retournée contre toi. Reprends-toi, ce n’est pas fini !",
"Tu t'es fait surprendre ! Mais il reste une chance de te rattraper.❗",
"La victoire a glissé entre tes doigts, mais la prochaine manche est à toi !",
"Un pas de trop… Tu trébuches juste avant la ligne d’arrivée.",
"❗Tu as été pris de vitesse, mais tu peux encore revenir dans le jeu !",
"❎C’est une défaite temporaire, tu reviendras plus fort la prochaine fois.❎",
"Cette manche t’échappe, mais ce n'est qu'un petit contretemps dans la bataille !","Le destin n’était pas de ton côté… Reprends-toi et tente à nouveau ta chance !","♥️ Stay Determined ♥️"]
#Message Victoire Feu sur Vent 
message_victoire1 = ["Un souffle ne suffit pas contre un brasier enragé🔥 ! Victoire totale !",
"Le vent a attisé tes flammes🔥 au lieu de les éteindre… Tu as gagné !",
"Une simple bourrasque ne peut rivaliser avec un incendie déchaîné !",
"Le feu danse et dévore tout sur son passage, réduisant le vent à néant !",
"La tempête s’essouffle… et le feu triomphe🏆🏆 dans une explosion de puissance !",
"Le brasier consume la brise, réduisant le vent en cendres ! Vous Avez Gagné ✨✨!","Hot Comme Toi 🫦"]
#Message Victoire Vent Sur Eau
message_victoire2 = ["🌪️🌪️ Une bourrasque puissante disperse les vagues, emportant l’eau au loin ! Vous Avez Gagné!🌪️🌪️","🌫️ Une rafale violente disperse les vagues… La tempête l’emporte !🌫️",
"Les gouttes sont emportées dans un ouragan furieux ! Victoire écrasante !",
"Le vent balaie tout sur son passage, laissant l’eau impuissante !💨",
"🌬️ Les vagues se brisent sous la puissance du souffle du vent !",
"Une bourrasque imprévisible a renversé l’océan lui-même ! Impressionnant !👀","Un Futon Trés Puissant ! "]
#Message Victoire Eau Sur Feu
message_victoire3 = ["Une vague déferlante éteint les flammes en un instant ! Vous Avez Gagné!🏄‍♂️🏄‍♂️","Les flammes sifflent une dernière fois avant de s’éteindre… Victoire de l’eau !",
"Un torrent impitoyable noie le brasier sans laisser de trace !",
"L’eau s’abat en cascade et engloutit le feu sans effort !🌊🌊",
"Une simple goutte 💧 peut éteindre une mer de flammes… Aujourd’hui, tu l’as prouvé !",
"Le feu se dissout dans une marée inarrêtable. L’eau triomphe !","🗣️ Attend C'est Comme Sa Que Sa Se Forme Un Bloc D'Obsidian ?? ⛏️"]
while running:

    Vous = None 
    IA = random.choice(Elements) #Tu Sais Deja Pourquoi j'ai mis random.choice(Elements) que au IA :/

    while Vous not in Elements:
        Vous = input("Choissisez Votre Elements Pensez à L'ecrire bien en Majuscule la premiere lettre ! (Vent , Feu , Eau): ")

    print(f"Vous: {Vous}")
    print(f"L'intelligence Artificielle(IA): Je Joue {IA} ! ")

    if Vous == IA:
        print(random.choice(messages_egalite))
    elif Vous == "Feu" and IA == "Vent":
        print(random.choice(message_victoire1))
        Points += 1
        Streaks += 1 
    elif Vous == "Vent" and IA == "Eau":
        print(random.choice(message_victoire2))
        Points += 1
        Streaks += 1 
    elif Vous == "Eau" and IA == "Feu":
        print(random.choice(message_victoire3))
        Points += 1
        Streaks += 1 
    else:
        print(random.choice(message_defaite))
        Streaks *= 0
    
    if Streaks >= 3 : #Configurable
        print(f"⭐Mais Vous etes le/la boss des bosses o: avec vos {Streaks} de Streaks⭐ Mais Je Parie Que Tu N'arriveras Pas a 10 De Streaks ")
    if Streaks >= 10: #Configurable
        print(f"🏆🏆 IMPOSSIBLE COMMENT {Streaks}?!!! A Ce Stade La  Vous êtes deja un champion Mondiale 🏆🏆")
    if Points >= 20 : #Configurable
        print(f"Wow {Points}pt/s Ce N'est Pas Normal Pour Un Mortelle🗿")
    if Points >= 100 : #Configurable
        print(f"🏅Mais Vous Aimez Bien vous donnez de defis {Points}pts Bravo 🏅🗿🗿Vous Etes Un Giga Chad 🗿🗿")    
    
    print(f"---------------Vous Avez Actuellement : {Points}pt/s, Et Un Streaks De {Streaks} N'abandonnez Pas !--------------- ")
    Rejouez = input("Voulez Vous Continuez à jouez ? (y/n): ").lower()
    if not Rejouez == 'y':
        Points *= 0
        Streaks *= 0
        running = False #Mettre En Off Le Jeu 
print("Merci d'avoir Jouer  A Bientôt ! Credits: B.David , Discord:Buinggamer ")        