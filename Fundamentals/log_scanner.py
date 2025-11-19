error_count = 0
warning_count = 0

# Open the log file
with open("system.log", "r") as file:
    for line in file:
        line = line.strip()

        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

# Print the report
print("\n=== Log Scan Report ===")
print("Total ERRORS:", error_count)
print("Total WARNINGS:", warning_count)

if error_count > 0:
    print("\n⚠️ Action needed: Errors detected in the system log.")
else:
    print("\n✔️ System healthy. No errors detected.")
