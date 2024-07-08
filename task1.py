from pathlib import Path

# calculate total salary from file with users salary 
def total_salary(path: Path) -> tuple:
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as fh:
            try:
                for line in fh:
                    name, salary = line.strip().split(",")
                    total += int(salary)
                    count += 1
            except ValueError:
                print(f"Incorect salary value {salary}, must be integer")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    average = total // count if count > 0 else 0
    return total, average

# create a file with users salary
with open("salary.txt", "w") as fh:
    fh.write("Alex Korp,3000\n")
    fh.write("Nikita Borisenko,2000\n")
    fh.write("Sitarama Raju,1000")

file_with_salary = Path("salary.txt")

# calculate the total and average salary
total, average = total_salary(file_with_salary)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
