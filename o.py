import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import get_body_barycentric, solar_system_ephemeris
from astropy.time import Time

# إعداد بيانات الميلاد (التاريخ، الوقت، والمكان)
year, month, day = 1980, 1, 1
hour, minute = 12, 0
latitude, longitude = 37.7749, -122.4194  # موقع سان فرانسيسكو

# إعداد الوقت
birth_time = Time(f'{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:00')

# حساب مواقع الكواكب
bodies = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
positions = {}

with solar_system_ephemeris.set('builtin'):
    for body in bodies:
        pos = get_body_barycentric(body, birth_time)
        positions[body] = np.degrees(np.arctan2(pos.y, pos.x))

# رسم الخريطة
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('E')
ax.set_theta_direction(-1)
ax.set_yticklabels([])

for body, angle in positions.items():
    ax.text(np.radians(angle), 1, body.capitalize(), fontsize=12, ha='center', va='center')

# إعداد علامات الأبراج
zodiac = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]
angles = np.linspace(0, 2 * np.pi, 13)
for i, (angle, sign) in enumerate(zip(angles, zodiac)):
    ax.text(angle, 1.1, sign, fontsize=10, ha='center', va='center')

plt.title('Birth Chart')
plt.show()
