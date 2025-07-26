# process_file.py
import time

start = time.time()

with open("data.csv", "r") as file:
    lines = file.readlines()

# Filtrim i të dhënave me një kusht të thjeshtë
filtered = [line for line in lines if "ERROR" in line]

with open("output.csv", "w") as file:
    file.writelines(filtered)

end = time.time()
print(f"Execution Time: {end - start} seconds")
