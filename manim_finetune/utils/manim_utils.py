import os
import re
import subprocess
import tempfile
import glob
import shutil
from typing import Tuple, Optional

def manim_render(
        code_string: str,
        output_dir: str,
        quality: str = "h"
    ) -> Tuple[bool, Optional[str]]:
    """
    Renders a Manim scene from a code string into the specified output directory.

    Parameters:
        code_string: complete scene code (including imports and class definition).
        output_dir: directory where all media files will be saved.
        quality: quality flag ('l', 'm', 'h', 'p', 'k'), default is 'h' (1080p60).

    Returns:
        Tuple of (success: bool, mp4_path: str or None).
        If successful, mp4_path is the absolute path to the rendered .mp4 file.
    """
    match = re.search(r'class\s+(\w+)\s*\(', code_string)
    if not match:
        return False, None
    class_name = match.group(1)

    os.makedirs(output_dir, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_media_dir:
        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(code_string)
            temp_py = f.name

        try:
            cmd = [
                "manim",
                f"-q{quality}",
                "--disable_caching",
                "--media_dir", tmp_media_dir,
                temp_py,
                class_name
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600
            )

            if result.returncode != 0:
                return False, None

            mp4_files = glob.glob(
                os.path.join(tmp_media_dir, "**", f"{class_name}.mp4"),
                recursive=True
            )
            if not mp4_files:
                mp4_files = glob.glob(
                    os.path.join(tmp_media_dir, "**", "*.mp4"),
                    recursive=True
                )

            if mp4_files:
                src = mp4_files[0]
                dst = os.path.join(output_dir, f"{class_name}.mp4")
                shutil.move(src, dst)
                return True, dst
            else:
                return False, None

        except subprocess.TimeoutExpired:
            return False, None
        except Exception:
            return False, None
        finally:
            if os.path.exists(temp_py):
                os.unlink(temp_py)
