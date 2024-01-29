from pathlib import Path
import csv


fp = Path.cwd()/"csv_reports"/"cash-on-hand-sgd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    coh_data = list(reader)
    
def coh():

    deficit_record = []
    increment_record = []
    max_increment_day = {"day": None, "amount": 0}
    # current_coh = 0
   
    


    for i in range (1,len(coh_data)):
        day, coh = int(coh_data[i][0]), int(coh_data[i][1])
        prev_coh = int(coh_data[i - 1][1])#if calculation wrong try again with + not -
        cash_difference = coh-prev_coh
        coh_output = ""


        if cash_difference > 0:
            increment_record.append({"day": day, "amount": cash_difference})
            if cash_difference > max_increment_day['amount']:
                max_increment_day = {'day': day, 'amount': cash_difference}
        elif cash_difference < 0:
            deficit_record.append({"day": day, "amount": cash_difference})
            max_deficit_day = sorted(deficit_record, key=lambda x: x["amount"], reverse=False)[0:3]
            # deficit_record.sort(key=lambda x: x["amount"], reverse=False)
            # max_deficit_day = sorted_deficit_record[0:3]

    if increment_record and deficit_record:
        
        for deficit in deficit_record:
            coh_output+=(f"[CASH DEFICIT] DAY:{deficit['day']} AMOUNT:USD{abs(deficit['amount'])}\n")
        coh_output+=(f"[HIGHEST CASH DEFICIT] DAY:{max_deficit_day[0]['day']} AMOUNT:USD{abs(max_deficit_day[0]['amount'])}\n")
        coh_output+=(f"[2nd HIGHEST CASH DEFICIT] DAY:{max_deficit_day[1]['day']} AMOUNT:USD{abs(max_deficit_day[1]['amount'])}\n")
        coh_output+=(f"[3rd HIGHEST CASH DEFICIT] DAY:{max_deficit_day[2]['day']} AMOUNT:USD{abs(max_deficit_day[2]['amount'])}\n")
        
    elif increment_record:
        coh_output+=("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")     
        coh_output+=(f"[HIGHEST CASH SURPLUS] DAY:{max_increment_day['day']} AMOUNT: USD{abs(max_increment_day['amount'])}\n")
    elif deficit_record:
        coh_output+=("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")     
        coh_output+=(f"[HIGHEST CASH DEFICIT] DAY:{max_deficit_day[0]['day']} AMOUNT:USD{abs(max_deficit_day[0]['amount'])}\n")
            
    return coh_output

