import os
import json


DEVICES_DIR = "devices"
OUTPUT_FILE = "devices.json"


def main():
    aggregated_data = []    
    for filename in sorted(os.listdir(DEVICES_DIR)):
        if filename.endswith(".json"):
            file_path = os.path.join(DEVICES_DIR, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    aggregated_data.append(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
            except Exception as e:
                print(f"An error occurred while processing {file_path}: {e}")
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(aggregated_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully wrote aggregated data to {OUTPUT_FILE}")
    except Exception as e:
        print(f"An error occurred while writing to {OUTPUT_FILE}: {e}")


if __name__ == "__main__":
    main()
