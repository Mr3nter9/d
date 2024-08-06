from flatlib.datetime import Datetime
from flatlib.chart import Chart
from flatlib import const

# إعداد البيانات
birth_date = Datetime('1990/07/05', '12:30', '+00:00')
latitude, longitude = 51.5, -0.12

# إنشاء خريطة فلكية
chart = Chart(birth_date, (latitude, longitude))

# عرض الكواكب ومواضعها
for name in const.LIST_OBJECTS:
    obj = chart.get(name)
    print(f"{name}: {obj.lon:.2f} degrees")
