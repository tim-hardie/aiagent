import os

def write_file(working_directory, file_path, content):
    relative_path = os.path.join(working_directory, file_path)
    target_path = os.path.abspath(relative_path)
    
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        with open(target_path, "w") as f:
            f.write(content)
        
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: Error writing file \"{file_path}\": {e}"