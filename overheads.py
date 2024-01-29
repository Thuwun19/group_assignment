import csv
from pathlib import Path

filepath = Path.cwd()/"csv_reports"/"overheads.csv"
with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    overheads_data = list(reader)




def overheads():
    each_category = {}
    total_amount = 0

    for x in overheads_data:
        Day, Items, Note, Amount = x
        Amount = float(Amount)  # Convert Amount to a numeric type
           
        # if overheads_data[Items] == 'Procurement Finished Goods' , 'Procurement Raw Material':
        #     del each_category[Items]

        if Items in ['Procurement Finished Goods', 'Procurement Raw Material', 'Overdraft Used']:
            continue

        if Items not in each_category:
            each_category[Items] = {"Amount": Amount}
            total_amount += Amount    

        else:
            each_category[Items]["Amount"] += Amount
            total_amount += Amount    

        # if each_category[Items]=='Procurement Finished Goods' or 'Procurement Raw Material' or 'Overdraft Used' :
        #     del each_category[Items]




  
    # highest_overhead_category= max(each_category[Items]["Amount"])
    highest_overhead_category = max(each_category, key=lambda k: each_category[k]["Amount"])

    highest_category_percentage= (each_category[highest_overhead_category]["Amount"])/ (total_amount) * 100
    # print(each_category)
    # print(each_category[highest_overhead_category]["Amount"])
    # print(total_amount)
    # print(highest_overhead_category)
    # print(highest_category_percentage)
  

    overheads_output = (f"[HIGHEST OVERHEAD] {highest_overhead_category}:{round(highest_category_percentage,2)}%\n")
    return overheads_output
            
# print(str(each_category))
    
    

    # # highest_overhead_category = max(overheads_data)
    # output = (f"[HIGHEST OVERHEAD] {highest_overhead_category[0]}:{highest_overhead_category[1]}%\n")
    # return output

print(overheads())
# print(type(overheads()))

# print(type(overheads()))