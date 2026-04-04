import shutil
import zipfile

def make_zip(source_dir: str, zip_name: str) -> str:
    """Create a zip archive of source_dir."""
    return shutil.make_archive(zip_name, 'zip', source_dir)

def extract_zip(zip_path: str, extract_to: str):
    """Extract zip archive."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
