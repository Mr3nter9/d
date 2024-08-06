import swisseph as swe

# إعداد البيانات
year, month, day, hour = 1990, 7, 5, 12.5
latitude, longitude = 51.5, -0.12

# حساب المواضع
jd = swe.julday(year, month, day, hour)
planets = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS, swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO]
positions = {swe.get_planet_name(p): swe.calc_ut(jd, p)[0] for p in planets}

# عرض النتائج
for planet, position in positions.items():
    print(f"{planet}: {position:.2f} degrees")

# حساب الصعود والتوسط
asc = swe.houses(jd, latitude, longitude)[0][0]
mc = swe.houses(jd, latitude, longitude)[0][9]

print(f"Ascendant: {asc:.2f} degrees")
print(f"Midheaven: {mc:.2f} degrees")
