# Ants
It's a tower-defend game.

## Element

**food**: to deploy the ant troops.

**place**: 
- there can be **one ant** or **many bees** in each **place**.
- all places make up a tunnel.

**ant**: 
- HavestwrAnt, add **one food** in each turn.
- ThrowerAnt, throw **a leaf** in each turn.

**win**: 
- The entire bee fleet has been vanquished (you win).
- A bee reaches the end of a tunnel (you lose).

## Map

(exit)# # # # # # # # # #(entrance)
**Bees** travel through the tunnel from **entrance** to **exit**.


## Test

python ants_text.py
python ants_gui.py

> `python ants_text.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]`
> 
> optional arguments:
>   -h, --help     show this help message and exit
>   -d DIFFICULTY  sets difficulty of game (test/easy/medium/hard/extra-hard)
>   -w, --water    loads a full layout with water
>   --food FOOD    number of food to start with when testing





