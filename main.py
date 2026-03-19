import datetime

log_file = "log.txt"
message = f"{datetime.datetime.now()} <- это время скрипта"
print(message)

with open(log_file, "a", encoding = "utf-8") as f:
    f.write(message)
