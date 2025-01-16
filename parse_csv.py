import json
import csv

# Load JSON data from file
input_file = "C:\\Users\\Savage\\Downloads\\velociraptor-master\\velociraptor-master\\vql\\hunting-sideload\\result_dataToAnalyzePath_1735745065160644000.json"
with open(input_file, "r", encoding="utf-8") as f:
    json_data = json.load(f)

# Specify CSV output file
output_file = "output.csv"

# Flatten JSON and write to CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)

    # Write the header
    header = [
        "id", "process_path", "parent_path", "dll_path", "size", "verified", 
         "md5", "sha1", 
        "final_result", "point"
    ]
    csv_writer.writerow(header)

    # Write the data rows
    for entry in json_data:
        row = [
            entry["id"],
            entry["process_info"].get("process_path"),
            entry["process_info"].get("parent_path"),
            entry["process_info"].get("dll_path"),
            entry["process_info"].get("size"),
            entry["signature_info"].get("verified"),
            entry["signature_info"].get("md5"),
            entry["signature_info"].get("sha1"),
            entry.get("final_result"),
            entry.get("point")
        ]
        csv_writer.writerow(row)

print(f"Data has been written to {output_file} successfully.")
