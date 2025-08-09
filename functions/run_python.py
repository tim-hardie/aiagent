import os

def run_python_file(working_directory, file_path, args=[]):
    relative_path = os.path.join(working_directory, file_path)
    target_path = os.path.abspath(relative_path)
    
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.exists(target_path):
        return f"Error: File \"{file_path}\" not found."
    
    if not os.path.isfile(target_path) and target_path[-3:] != ".py":
        return f"Error: \"{file_path}\" is not a Python file."