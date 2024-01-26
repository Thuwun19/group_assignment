import csv
from pathlib import Path

filepath = Path.cwd()/"csv_reports"/"profit-and-loss.csv"

with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    pl_data = list(reader)
    
def pl():
    deficit_record = []
    increment_record = []
    max_increment_day = {"day": None, "amount": 0}
    deficit_amount = 0
    deficit_day = None

    for i in range (1,len(pl_data)):
        day, netprofit = int(pl_data[i][0]), int(pl_data[i][4])
        prev_netprofit = int(pl_data[i - 1][4])#if calculation wrong try again with + not -
        cash_difference = netprofit-prev_netprofit

        
        if cash_difference > 0:
            increment_record.append({"day": day, "amount": cash_difference})
            if cash_difference > max_increment_day['amount']:
                max_increment_day = {'day': day, 'amount': cash_difference}
        elif cash_difference < 0:
            deficit_record.append({"day": day, "amount": cash_difference})
            max_deficit_day = sorted(deficit_record, key=lambda x: x["amount"], reverse=False)[0:3]

            
            
    if increment_record and deficit_record:
        
        for deficit in deficit_record:
            print(f"[NET PROFIT DEFICIT] DAY:{deficit['day']} AMOUNT:{deficit['amount']}")
        print(f"[HIGHEST NET PROFIT DEFICIT] DAY:{max_deficit_day[0]['day']} AMOUNT:{max_deficit_day[0]['amount']}")
        print(f"[2nd HIGHEST NET PROFIT DEFICIT] DAY:{max_deficit_day[1]['day']} AMOUNT:{max_deficit_day[1]['amount']}")
        print(f"[3rd HIGHEST NET PROFIT DEFICIT] DAY:{max_deficit_day[2]['day']} AMOUNT:{max_deficit_day[2]['amount']}")
        
    elif increment_record:
        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")     
        print(f"[HIGHEST NET PROFIT SURPLUS] DAY:{max_increment_day['day']} AMOUNT:{max_increment_day['amount']}")
    elif deficit_record:
        print("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")     
        print(f"[HIGHEST CASH DEFICIT] DAY:{max_deficit_day[0]['day']} AMOUNT:{max_deficit_day[0]['amount']}")
            

pl()