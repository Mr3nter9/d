import matplotlib.pyplot as plt
from astroquery.jplhorizons import Horizons

# إعداد بيانات الميلاد (التاريخ، الوقت، والمكان)
year, month, day = 1980, 1, 1
hour, minute = 12, 0
latitude, longitude = 37.7749, -122.4194  # موقع سان فرانسيسكو

# حساب مواقع الكواكب
obj_ids = {
    'Sun': '10',
    'Moon': '301',
    'Mercury': '199',
    'Venus': '299',
    'Mars': '499',
    'Jupiter': '599',
    'Saturn': '699',
    'Uranus': '799',
    'Neptune': '899',
    'Pluto': '999',
}

positions = {}

for name, obj_id in obj_ids.items():
    obj = Horizons(id=obj_id, location=f'geo={longitude},{latitude}', epochs={'start': f'{year}-{month}-{day}T{hour}:{minute}:00', 'stop': f'{year}-{month}-{day}T{hour}:{minute}:01', 'step': '1m'})
    eph = obj.ephemerides()
    positions[name] = float(eph['RA'][0])

# رسم الخريطة
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 360)
ax.set_ylim(-1, 1)

# وضع علامات الكواكب على الدائرة
for name, position in positions.items():
    ax.text(position, 0, name, fontsize=12, ha='center', va='center')

ax.set_yticks([])
ax.set_xticks(range(0, 360, 30))
ax.set_xticklabels(['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'])

plt.grid(True)
plt.title('Birth Chart')
plt.show()
