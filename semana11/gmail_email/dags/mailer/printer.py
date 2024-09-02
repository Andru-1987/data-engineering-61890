def get_file_name(**kwargs):
    import os
    import glob
    
    # Path where the file is expected
    file_path_pattern = '/opt/airflow/data/data-*.csv'
    
    # Find files matching the pattern
    files = glob.glob(file_path_pattern)
    
    if files:
        file_name = files[-1]  # Assuming only one file matches
        # Push the file name to XCom
        kwargs['ti'].xcom_push(key='file_name', value=file_name)
    else:
        raise FileNotFoundError("No file found matching the pattern.")


def print_message(**kwargs):
    detected_file = kwargs['ti'].xcom_pull(key='file_name', task_ids='get_file_name')
    print(f"Llegó el archivo: {detected_file}")
