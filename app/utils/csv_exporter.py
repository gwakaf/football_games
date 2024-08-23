import csv, json
import os

def export_summary(json_folder_path, output_csv_file_path):
    output_summary = []

    for file_name in os.listdir(json_folder_path):
        if file_name.startswith("teams_in_competition"):
            file_path = os.path.join(json_folder_path, file_name)
            with open(file_path, 'r') as file:
                content = json.load(file)
                output_summary.append((content["competition"]["name"], content["count"]))
                

    with open(output_csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Competition', 'Number of Teams'])
        writer.writerows(output_summary)