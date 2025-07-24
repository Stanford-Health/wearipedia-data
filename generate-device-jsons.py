import os
import json


def generate_devices_file(folder: str) -> None:
    aggregated_data = []
    for file_name in sorted(os.listdir(folder)):
        if file_name.endswith(".json"):
            with open(os.path.join(folder, file_name), 'r', encoding='utf-8') as f:
                data = json.load(f)
                aggregated_data.append(data)

    with open(folder + ".json", 'w', encoding='utf-8') as f:
        json.dump(aggregated_data, f, indent=2, ensure_ascii=False)


def generate_bibreferences_file(folder: str) -> None:
    aggregated_data = {}
    for file_name in sorted(os.listdir(folder)):
        if file_name.endswith(".json"):
            with open(os.path.join(folder, file_name), 'r', encoding='utf-8') as f:
                data = json.load(f)
                aggregated_data.update(data)

    with open(folder + ".json", 'w', encoding='utf-8') as f:
        json.dump(aggregated_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    generate_devices_file("devices")
    generate_devices_file("tags")
    generate_bibreferences_file("bibreferences")
