import csv
from pathlib import Path
##JAVIER
filepath = Path.cwd()/"csv_reports"/"Overheads.csv"
with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    overheads_data = list(reader)




def overheads():
    each_category = {}
    total_amount = 0

    for x in overheads_data:
        Items, Amount = x
        Amount = float(Amount)  # Convert Amount to a numeric type
           
    
        if Items not in each_category:
            each_category[Items] = {"Amount": Amount}
            total_amount += Amount    

        else:
            each_category[Items]["Amount"] += Amount
            total_amount += Amount    

    



  
   
#     highest_overhead_category = max(each_category)

#     highest_category_percentage= (each_category[highest_overhead_category]["Amount"])/ (total_amount) * 100
    

#     overheads_output = (f"[HIGHEST OVERHEAD] {highest_overhead_category}:{round(highest_category_percentage,2)}%\n")
#     return overheads_output
            


