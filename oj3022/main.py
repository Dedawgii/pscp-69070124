"""[LEARNING LOGS] Temperature"""

Temp = float(input())
Unit_from = input().upper()
Unit_to = input().upper()

offsets = {'C':0, 'F':32, 'K':273.15, 'R':491.67}
scales = {'C':5, 'F':9, 'K':5, 'R':9}
result = (((Temp - offsets[Unit_from])/scales[Unit_from])*scales[Unit_to])+offsets[Unit_to]

print(f"{result:.2f}")
