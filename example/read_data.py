import zipfile
import json

def read_metadata(zip_Path):
    with zipfile.ZipFile(zip_Path, 'r') as z:
        with z.open("metadata.json") as f:
            metadata = json.load(f)
            return metadata

# example call

path_to_audiopkg = 'sascha_mester_-_verliebtheit_ist_nur_ein_gefuehl.audiopkg'
metadata = read_metadata(path_to_audiopkg)

print (json.dumps(metadata, indent=4, ensure_ascii=False))
