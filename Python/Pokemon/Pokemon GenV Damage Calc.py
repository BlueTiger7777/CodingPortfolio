import random
import math

Level=int(input("Level of user: "))
A=int(input("Attack or Special Attack stat of attacker depending on move: "))
D=int(input("Defence or Special Defence stat of deffender depending on move: "))
Power=int(input("Power of move: "))
Targets=1
PB=1
Weather=1
Critical=2
Random=1 #math.floor(random.randint(85, 100)/100)
STAB=1.5
Type=2
Burn=1
Other=1
ZMove=1
TeraSheild=1
Damage=((2*Level/5+2)*Power*A/D/50+2)*Targets*PB*Weather*Critical*Random*STAB*Type*Burn*Other*ZMove*TeraSheild
print(f'{Damage} asuming that there is 1 target, no Parental Bond, no weather, not a crit, STAB is 1.5, super effectiveness totaling to 2 times, no burn, no zmove, no tera sheild')

      
