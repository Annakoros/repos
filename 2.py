sec = int(input('Введите время в секундах: '))
minutes = 0
hours = 0
if sec >= 60:
    minutes = sec // 60
    sec = sec % 60
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
if sec < 10:
    strsec = '0' + str(sec)
else:
    strsec = sec
if minutes < 10:
    strminutes = '0' + str(minutes)
else:
    strminutes = minutes
if hours < 10:
    strhours = '0' + str(hours)
else:
    strhours = hours
print(f'{strhours}:{strminutes}:{strsec}')