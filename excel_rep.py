#For excel report , storing the waveform data and summary
from csv import writer

import pandas as pd

def export_to_excel(excel_filename, waveform_df, summary_df):

    with pd.ExcelWriter(excel_filename , engine="openpyxl") as writer:

        waveform_df.to_excel( writer,sheet_name="Waveform Data",index=False)

        summary_df.to_excel(writer,sheet_name="System Analysis",index=False)

        '''for sheet in writer.sheets.values():
            for column_cells in sheet.columns:
                length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in column_cells)
                sheet.column_dimensions[column_cells[0].column_letter].width = length + 2'''
        
        worksheet1 = writer.sheets["Waveform Data"]
        worksheet2 = writer.sheets["System Analysis"]

        worksheet1.freeze_panes = "A2"
        worksheet2.freeze_panes = "A2"


    print("Excel file exported successfully!")
    print(f"File saved as: {excel_filename}")

