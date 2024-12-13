import json
import pandas as pd

# Load JSON file
input_file = "input_file.json"  # Replace with your JSON file path
output_file = "output_file.xlsx"  # Output Excel file path

# Load JSON data
with open(input_file, "r") as file:
    data = json.load(file)

# Extract information
rows = []
for endpoint, methods in data["paths"].items():
    for method, details in methods.items():
        param_names = [param["name"] for param in details.get("parameters", [])]
        rows.append({
            "Description": details.get("description", ""),
            "Method": method.upper(),
            "Endpoint": endpoint,
            "Params": "\n".join(param_names) if param_names else ""  # Empty if no parameters
        })

# Convert to DataFrame
df = pd.DataFrame(rows)

# Reorder columns as requested
df = df[["Description", "Method", "Endpoint", "Params"]]

# Save to Excel
df.to_excel(output_file, index=False)

print(f"Data exported to {output_file}")
