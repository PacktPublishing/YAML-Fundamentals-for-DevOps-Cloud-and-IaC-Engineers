import yaml

with open("anchors-2.yaml", 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            if key == "server1":
                for key, value in value.items():
                    print(f"{key}: {value}")
    except yaml.YAMLError as exc:
        print(exc)