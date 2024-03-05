from datetime import time 

open_close_hour=[(time(h,m).strftime('%I:%M:%p'),time(h,m).strftime('%I:%M:%p')) for h in range(0,24)for m in (0,30)]

print(open_close_hour)
# print(data)
# for h in range(0,24):
#     for m in(0,30):
#         print(time(h,m).strftime('%I:%M:%p'))