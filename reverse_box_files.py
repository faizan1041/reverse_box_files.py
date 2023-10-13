import os

# Define the directory path
dir_path = 'data/arabic-dataset/'

# Iterate over all files in the directory
for filename in os.listdir(dir_path):
    # Only process .box files
    if filename.endswith('.box'):
        filepath = os.path.join(dir_path, filename)
        
        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        # If there's at least one line
        if lines:
            # Get the last line
            last_line = lines[-1]
            
            # Reverse the order of lines excluding the last line
            reversed_lines = lines[:-1][::-1]
            
            # Append the last line back
            reversed_lines.append(last_line)
        
        # Write the reversed content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(reversed_lines)
