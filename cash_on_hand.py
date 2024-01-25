from pathlib import Path
import csv


fp = Path.cwd()/"csv_reports"/"cash-on-hand-sgd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    coh_data = list(reader)
    


deficit_record = []
increment_record = []
max_increment_day = {"day": None, "amount": 0}
max_deficient = {"day": None, "amount": 0}
current_coh = 0
deficit_amount = 0
deficit_day = None


for i in range (1,len(coh_data)):
    day, coh = int(coh_data[i][0]), int(coh_data[i][1])
    prev_coh = int(coh_data[i - 1][1])#if calculation wrong try again with + not -
    cash_difference = coh-prev_coh


    if cash_difference > 0:
        increment_record.append({"day": day, "amount": cash_difference})
        if cash_difference > max_increment_day['amount']:
            max_increment_day = {'day': day, 'amount': cash_difference}
    elif cash_difference < 0:
        deficit_record.append({"day": day, "amount": cash_difference})
        if cash_difference < max_deficient["amount"]:
            max_deficient = {'day': day, 'amount': cash_difference}
print("Increment Record:", increment_record)
print("Max Increment Day:", max_increment_day)
print("Top Deficit Record:", deficit_record)
print("Max Deficit Day:", sorted(max_deficient)[0:3])



