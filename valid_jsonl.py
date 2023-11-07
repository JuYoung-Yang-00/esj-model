import json

def validate_jsonl(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, 1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON on line {i}: {e}")
                return False
    return True

is_valid = validate_jsonl('./val_data.jsonl')
if is_valid:
    print("The JSONL file is valid.")
else:
    print("The JSONL file has issues.")
