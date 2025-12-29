import random, math

planet_ao = float(input("Дістанція планети: "))
planet_atmo_albedo = float(input("Альбедо планети: "))
planet_atmo_greenhouse = float(input("Парниковий ефект: "))
solar_luminos = float(input("Світність зірки: "))

#planet_distance = random.uniform(9.5e+10*planet_number, 1.5e+11*planet_number) * planet_number
#planet_ao = planet_distance / (1.496e+11)
planet_effective_temp = ((solar_luminos * 1e+4)/ (16 * math.pi * 5.67e-8 * (planet_ao**2))) ** (1/4)
planet_kelvin_temp = planet_effective_temp * ((1 + (planet_atmo_greenhouse + planet_atmo_albedo)) ** (1/4))
planet_temp = planet_kelvin_temp - 273.15

print(
   "Дано\n"
   f"Дістанція до зірки: {planet_ao:,} а. о\n"
   f"Альбедо: {planet_atmo_albedo}\n"
   f"Парниковий ефект: {planet_atmo_greenhouse}\n"
   f"Світність зірки: {solar_luminos:,} L☉\n"
   "\n"
   "Результати\n"
   f"Ефективна температура: {planet_effective_temp:,.2f} K\n"
   f"Сер. температура: {planet_kelvin_temp:,.2f} K\n"
   f"Температура в Цельсіях: {planet_temp:,.2f} °C\n"
)