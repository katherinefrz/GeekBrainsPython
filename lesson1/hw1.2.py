time_in_sec = int(input("Enter your local time in sec: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Now is {hours}:{minutes}:{sec} ")