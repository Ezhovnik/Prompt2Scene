import os
import re
import subprocess
import tempfile

def manim_render(
    code_string: str,
    output_dir: str,
    quality: str = "h"
) -> bool:
    """
    Renders a Manim scene from a code string into the specified output directory.

    Parameters:
        code_string: complete scene code (including imports and class definition).
        output_dir: directory where all media files will be saved.
        quality: quality flag ('l', 'm', 'h', 'p', 'k'), default is 'h' (1080p60).
        timeout: maximum execution time in seconds.

    Returns:
        True if rendering completes successfully,
        False otherwise.
    """

    match = re.search(r'class\s+(\w+)\s*\(', code_string)
    if not match:
        return False
    class_name = match.group(1)

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code_string)
        temp_py = f.name

    try:
        cmd = [
            "manim",
            f"-q{quality}",
            "--disable_caching",
            "--media_dir", output_dir,
            temp_py,
            class_name
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600
        )
        return result.returncode == 0

    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False
    finally:
        if os.path.exists(temp_py):
            os.unlink(temp_py)
