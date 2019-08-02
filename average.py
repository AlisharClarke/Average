# 1. Establish list of ages.
# 2. Add all of the ages together.
# 3. Divide total by length of list
# 4. Show value.
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
TotalAge = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] +ages[7] + ages[8]
Average = TotalAge/9
print (Average)

sum = sum(ages)
age_ind = len(ages)
result = sum / age_ind
print (result)
