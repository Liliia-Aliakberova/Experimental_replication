import os
import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer
from split import num_parts

# Define the folder where your .xes files are located
folder_path = '/.../hl_log'
# Create an empty list to store event data
event_data = []
# Loop through the range of parts
for number in range(1, num_parts + 1):
    xes_file = os.path.join(folder_path, f"high-level-log_{number}.xes")

    if os.path.exists(xes_file):
        event_log = xes_importer.apply(xes_file)

        # Extract the number from the loop
        file_number = number

        # Append the events from each log to the event_data list
        for trace in event_log:
            for event in trace:
                event_data.append(event)

                # Modify the "case" column to include the number from the loop
                event_data[-1]['case'] = str(event['case']) + "_" + str(number)

# Create a DataFrame from the event data
event_df = pd.DataFrame(event_data)

# Define the path for the output CSV file
output_csv_path = '/.../hl_log/output.csv'

# Save the merged data to a CSV file
event_df.to_csv(output_csv_path, index=False)