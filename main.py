import cash_on_hand,overheads,profit_loss
from pathlib import Path
import csv

def main():
   
    output_file_path = Path.cwd() /"summary_report.txt"
    with output_file_path.open(mode="w", encoding="UTF-8", newline="") as output_file:
       
        output_file.write(overheads.overheads())
        output_file.write(cash_on_hand.coh())
        output_file.write(profit_loss.pl())
  
main()

