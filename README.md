# Swagger Export to XLSX

## Description

This script extracts API details from a Swagger JSON file and exports them to an Excel file (.xlsx). It processes the Swagger file to retrieve the following information for each endpoint and HTTP method:

- **Description**: A brief explanation of the endpoint.
- **Method**: HTTP method (e.g., GET, POST, DELETE).
- **Endpoint**: The URL of the API endpoint.
- **Params**: A list of parameter names used by the endpoint, separated by newlines (left blank if no parameters are provided).

The generated Excel file organizes this information into four columns:

| Description               | Method | Endpoint             | Params                            |
| ------------------------- | ------ | -------------------- | --------------------------------- |
| Delete the specified area | DELETE | /api/areas/{area_id} | area_id                           |
| Update area               | PUT    | /api/areas/{area_id} | area_id\narea_name\ndisplay_order |
| Get area details          | GET    | /api/areas/{area_id} |                                   |

## Features

- Handles Swagger files with nested paths and methods.
- Supports endpoints without parameters.
- Parameters are displayed as a newline-separated list in the "Params" column.
- Outputs a well-formatted Excel file for documentation and review purposes.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `openpyxl`

You can install the dependencies with:

```bash
pip install pandas openpyxl
```

## Usage

1. Place your Swagger JSON file in the same directory as the script or provide the full path.
2. Update the `input_file` and `output_file` variables in the script with the path to your Swagger JSON file and desired output Excel file name.

Example:

```python
input_file = "input.json"  # Path to your Swagger JSON file
output_file = "output.xlsx"  # Path to save the Excel file
```

3. Run the script:

```bash
python swagger_export_to_xlsx.py
```

4. The Excel file will be saved at the location specified in `output_file`.

## Output Format

The Excel file will contain the following columns:

- **Description**: Endpoint description.
- **Method**: HTTP method.
- **Endpoint**: Endpoint URL.
- **Params**: Newline-separated parameter names (empty if no parameters).

### Output (Excel):

| Description               | Method | Endpoint             | Params                            |
| ------------------------- | ------ | -------------------- | --------------------------------- |
| Delete the specified area | DELETE | /api/areas/{area_id} | area_id                           |
| Update area               | PUT    | /api/areas/{area_id} | area_id\narea_name\ndisplay_order |
| Get area details          | GET    | /api/areas/{area_id} |                                   |

## Notes

- Ensure your Swagger JSON file is properly formatted and adheres to the Swagger/OpenAPI specification.
- If the script encounters errors, verify the file path and JSON structure.
