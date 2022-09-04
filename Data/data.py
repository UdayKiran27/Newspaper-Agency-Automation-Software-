import json
import datetime
Mjson = { 'Manager' : {'Username':'Manager', 'UserID':'123456', 'Password':'Manager@NAAS', 'date':str(datetime.date(2002, 12, 2))} }
with open("random.json", "w") as write_file:
    json.dump(Mjson, write_file)