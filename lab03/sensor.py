threshold = float(input())
total_records = int(input())

error_count = 0
exceed_count = 0
valid_count = 0
sum_temperatures = 0.0

max_temperature = None

for _ in range(total_records):
    entry = input().strip()
    
    if entry == "error":
        error_count += 1
    else:
        temp = float(entry)
        valid_count += 1
        sum_temperatures += temp
        
        if temp > threshold:
            exceed_count += 1
            
        if max_temperature is None or temp > max_temperature:
            max_temperature = temp

print(total_records)
print(error_count)
print(exceed_count)

print(f"{max_temperature:.1f}")

average_temperature = sum_temperatures / valid_count
print(f"{average_temperature:.1f}")