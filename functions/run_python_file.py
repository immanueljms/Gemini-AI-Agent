import os 
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args != None:
            command.extend(args)
    
        process = subprocess.run(command, cwd=abs_working_dir, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        output=""
        if process.returncode != 0:
            output+= f"Process exited with code {process.returncode}"
        if process.stdout == "" and process.stderr == "":
            output += f"No output produced"
        else:
            output += f"STDOUT:\n{process.stdout}\n"
            output += f"STDERR:\n{process.stderr}\n"
        return output
        

    except Exception as e:
        return f"Error: executing Python file: {e}"