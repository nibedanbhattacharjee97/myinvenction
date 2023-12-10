import pandas as pd
import openpyxl as opexcel

def excel_to_csv(input_excel_path, output_csv_path):
    try:
        # Load Excel file into a pandas DataFrame
        df = pd.read_excel(input_excel_path)

        # Save DataFrame to a CSV file
        df.to_csv(output_csv_path, index=False)

        print(f"Hi Nibedan Conversion successful. CSV file saved at: {output_csv_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Replace 'input_excel.xlsx' with the path to your Excel file
    input_excel_path = 'D:\myinvenction files\Placement_Doc_Verification_Report.xlsx'

    # Replace 'output_csv.csv' with the desired path for the CSV output
    output_csv_path = 'D:\myinvenction files\Placement_Doc_Verification_Report.csv'

    # Call the function to convert Excel to CSV
    excel_to_csv(input_excel_path, output_csv_path)
