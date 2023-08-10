# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"105388.0","system":"med"},{"code":"19162.0","system":"med"},{"code":"28241.0","system":"med"},{"code":"31102.0","system":"med"},{"code":"35816.0","system":"med"},{"code":"35963.0","system":"med"},{"code":"36949.0","system":"med"},{"code":"38862.0","system":"med"},{"code":"41571.0","system":"med"},{"code":"42012.0","system":"med"},{"code":"42023.0","system":"med"},{"code":"44996.0","system":"med"},{"code":"47801.0","system":"med"},{"code":"779.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_bladder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_bladder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_bladder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_bladder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
