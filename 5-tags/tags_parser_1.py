import yaml

with open("tags.yaml", 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
        for key, value in data.items():
            print(f"{key}: {value}")
            print(type(value))
    except yaml.YAMLError as exc:
        print(exc)