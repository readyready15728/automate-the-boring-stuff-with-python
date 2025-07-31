print("Enter TB or GB for the advertised unit:")
unit = input(">")

# Calculate the amount that the advertised capacity lies:
if unit == "TB" or unit == "tb":
    discrepancy = 1e12 / 1_099_511_627_776
elif unit == "GB" or unit == "gb":
    discrepancy = 1e9 / 1_073_741_824

print("Enter the advertised capacity:")
advertised_capacity = input(">")
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths, and convert
# it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print("The actual capacity is " + real_capacity + " " + unit)
