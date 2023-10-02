import math
import time

def progress_bar(progress, total, size = 100, fill_sign = '■', empty_sign = '='):
    percent = size * (progress / float(total))
    percent2 = 100 * (progress / float(total))
    bar = fill_sign * int(percent) + empty_sign * (size - int(percent))
    print(f"\r|{bar}| {percent2:.0f}%", end="\r")