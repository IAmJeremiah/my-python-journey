import os
# Get the folder where THIS script lives
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build a full path to system.log in the same folder
log_path = os.path.join(base_dir, "system.log")
print("Log file path:", log_path)


def count_entries(log_file):
    error_count = 0
    warning_count = 0

    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    return error_count, warning_count


def print_report(error_count, warning_count):
    print("\n=== Log Scan Report ===")
    print("Total ERRORS:", error_count)
    print("Total WARNINGS:", warning_count)

    if error_count > 0:
        print("\n⚠️ Action needed: Errors detected in the system log.")
    else:
        print("\n✔️ System healthy. No errors detected.")


# MAIN PROGRAM
log_path = r"C:\Users\Jeremiah\MyJourney\Fundamentals\system.log"   # you can change this anytime
errors, warnings = count_entries(log_path)
print_report(errors, warnings)
