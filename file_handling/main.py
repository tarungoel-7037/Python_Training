import re

log_pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[([^\]]+)\] ".*?" (\d{3}) \d+'

with open("file_handling/sample_log.log") as f,open("file_handling/output.csv","w") as o:
    o.write("IP Address, Date/Time, Status Code\n")
    
    for line in f:
        match = re.search(log_pattern,line)
        if(match):
            ip = match.group(1)
            datetime_str = match.group(2)
            status = match.group(3)
            o.write(f"{ip}, {datetime_str}, {status}\n")   
    
print(f"Copied to output.csv")
