import os

def get_files_info(working_directory, directory="."):
    relative_path = os.path.join(working_directory, directory)
    target_path = os.path.abspath(relative_path)
    
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    
    if not os.path.isdir(target_path):
        return f"Error: \"{directory}\" is not a directory"
    
    try:
        content_list = []
        for content in os.listdir(relative_path):
            content_path = os.path.join(relative_path, content)
            content_list.append(f" - {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}")
        return "\n".join(content_list)
    except Exception as e:
        return f"Error listing files: {e}"