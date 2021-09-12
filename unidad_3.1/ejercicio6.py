"""
Estos son los depoortes de un polideportivo. ¿Pueden ir tres amigos si a uno le gusta el futbol, otro le gusta el basket o el voley, pero el ultimo odia el voley?

Futbol siosi
basket o el voley
no el voley
"""
futbol=True
basquet=False
voley=False
condicion_amigo_1=futbol
condicion_amigo_2=basquet or voley
condicion_amigo_3=not voley
van_los_amigos=(condicion_amigo_1) and (condicion_amigo_2) and (condicion_amigo_3)
print(f"van los amigos ?!{van_los_amigos}")