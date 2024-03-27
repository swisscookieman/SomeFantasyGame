# SomeFantasyGame

Description goes here.

## To Do

- [x] Redo save_handler.py - *done*
- [ ] Level system with graduing exp requirements
- [ ] Redo qte and puzzle **correctly**
- [ ] Rewrite Level class
- [ ] Make a function for choices
- [ ] Define default inventory

## Goal / help / roadmap / whatever

Player:

Stats:
Max health (base 100 max 1000)  
Strenght (base 100 max 1000) increases physical damage  
Magic knowledge (base 100 max 1000) increases magic damage  
Archery (base 100 max 1000) increases ranged dmg  
Stealth (base 0 max 100) chance for enemy attack to miss  
Accuracy (base 75 max 200) chance for attack to hit  
speed (base 100 max 1000) increases hits per sec  
Physical resistance (base 0 max 100) phy damage reduction %  
Magic resistance (base 0 max 100) mag dmg reduction %  
Ranged resistance (base 0 max 100) mag dmg reduction %  
crit chance (base 10 max 100) chance to x2 dmg

tout increase dune manière ou d'une autre avec le lvl, mais plus ou moins selon la classe
possibilité de choisir ou mettre ses points ?
les equipments sont ce qui increase a fond

l'idée serait que tu peux pas max tt en meme temps, i.e. si tu fais un build full stealth alors tu te fais quasi jamais hit mais tu fais base dmg, voire moins  
tu ferais un build monster-specific pour le farm efficaement

Monstres:

2 types:

- monstres de base, farmable en boucle pour du loot rare
- boss, demade des actions text based (e.g. un puzzle, choisir une target, jsp) donc fights plus long mais much better chance pour loot

Chaque monstre a ses spécifités, comme faire du gros magic dmg ou etre resistant physical.

Damage:  
Soit physical, soit magic, soit ranged

Classes:  
Mercenary: bcp de health (tank), attack physique  
Warrior: strenght surtout, est accurate  
Archer: archery bcp, high accuracy, low health  
Mage: magic knowledge, bcp de ranged resistance ??  
Assasin: bcp de stealth, dmg physique pas mal  
+++

Rarities:

⬜️ Common - Quasiment tout, matériaux, truc que tu vend tt de suite, etc  
🟦 Rare - Drops usable, que tu vas utiliser early game sans probleme et qui peuvent se craft en mieux. Doit ETRE RARE, soit <3% minimum  
🟪 Fabled - Des items dont on parle dans les fables. Doit avoir des capacités spéciales e.g. lifeleach? Vrmt rare, minimum 30 min de farm sur un mob  
🟨 Relic - Des items dont on parle dans les légendes depuis des siècles. Capacités puissantes, le genre de drop dur a farm et plutot random  
🟥 Celestial - L'item ultime. Si droppé early game par chance, te donne un méga boost de progression. le genre d'item que t'as 1-2 fois dans ton invertaire, pas 50

Autre: 🟩 Sovereign Material - uniquement pour des matériaux rares, type la plume de phoenix bien rare qui crafte le meilleur staff du jeu.

## Future plans

## Contributions and issues

## Idk we need to make this better

https://alwore.itch.io/wizard-icon-set ta tjrs besoin de ca ? Si non delete pls

truc pour que leo oublie pas: compte le nbr de monstres, a la fin du farm ca run la loot tables x fois et donne le loot
