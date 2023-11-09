import xml.etree.ElementTree as ET
import math
import os

# Load the .xes file
tree = ET.parse('/.../event_logs/BPI_Challenge_2017.xes')
root = tree.getroot()

# Define the number of parts you want to split the file into
num_parts = 12

# Calculate the number of traces in each part
num_traces = len(root.findall('.//trace'))
traces_per_part = math.ceil(num_traces / num_parts)

# Specify the folder where you want to save the split files
output_folder = '/.../event_logs'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Split the file into parts
for part_num in range(num_parts):
    # Create a new .xes file for each part
    part_tree = ET.ElementTree(ET.Element("log"))
    part_root = part_tree.getroot()

    # Copy the attributes from the original .xes file
    for key, value in root.attrib.items():
        part_root.set(key, value)

    # Copy a portion of traces to the current part
    traces_in_part = root.findall('.//trace')[part_num * traces_per_part:(part_num + 1) * traces_per_part]
    for trace in traces_in_part:
        part_root.append(trace)

    # Save the part as a separate .xes file in the output folder
    output_file_path = os.path.join(output_folder, f'part_{part_num + 1}.xes')
    part_tree.write(output_file_path)

print("Splitting complete.")
