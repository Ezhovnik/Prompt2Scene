import subprocess
import tempfile
import os
import re
import traceback

def manim_test(code_string: str, log_file: str = "manim_errors.log", idx: int = 0) -> bool:
    """
    Test if given manim code runs without errors.
    Returns True if successful, False otherwise.
    Errors are logged to log_file.
    """
    match_text = re.search(r'class\s+(\w+)\s*\(', code_string)
    if match_text is None:
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write("--- Failed to find class ---\n")
            log.write(f"IDX:\n{idx}\n")
            log.write("--- End ---\n\n")
        return False
    class_name = match_text.group(1)

    with tempfile.TemporaryDirectory() as media_dir:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code_string)
            temp_file = f.name

        try:
            result = subprocess.run(
                [
                    "manim", "-ql", "--disable_caching",
                    "--media_dir", media_dir,
                    temp_file,
                    class_name
                ],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                with open(log_file, 'a', encoding='utf-8') as log:
                    log.write("--- Manim error ---\n")
                    log.write(f"IDX:\n{idx}\n")
                    log.write(f"STDERR:\n{result.stderr}\n")
                    log.write(f"STDOUT:\n{result.stdout}\n")
                    log.write("--- End ---\n\n")
                return False
            return True
        except Exception as e:
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write("--- Exception during Manim execution ---\n")
                log.write(f"Code:\n{code_string}\n")
                log.write(f"Error: {str(e)}\n")
                log.write(traceback.format_exc())
                log.write("--- End ---\n\n")
            return False
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
