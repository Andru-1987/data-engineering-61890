import pandas as pd
import re

class PandasReader():
    # Data statica
    # Existen archivos donde tomaremos decisiones en base a lo que nos otorgan
    # ejemplo las :
    #     - API
    #     - SQL
    #     - JSON (que no deja de ser una response data de una API RESTFULL)

    def __init__(self, file:str, delimiter:str = ','):
        self.data_file = file 
        self.delimiter = delimiter
    
    def get_data_from_file(self):
        self.data_file = self.data_file.lower()

        match = re.search(r'\.(\w+)$', self.data_file)

        if not  match:
            raise ValueError("Not valid file extension")

        file_type = match.group(1)
            
        if self.data_file.startswith("http://") or self.data_file.startswith("https://"):
            return pd.read_csv(self.data_file,delimiter=self.delimiter)

        if file_type == 'csv':
            return pd.read_csv(self.data_file,delimiter=self.delimiter)

        elif file_type == 'xlsx' or file_type == 'xls':
            return pd.read_excel(self.data_file)

        elif file_type == 'txt':
            return pd.read_csv(self.data_file,delimiter=self.delimiter)

        else:
            raise ValueError(f"Unsupported file {self.data_file}")
