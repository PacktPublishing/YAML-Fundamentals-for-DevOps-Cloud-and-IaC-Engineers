import yaml

my_file = "multiline-1.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            for k, v in value.items():
                if k == "note1":
                    print(f"note1 of dc: {v}")
                    print("-----")
                if k == "note2":
                    print(f"note2 of dc: {v}")
    except yaml.YAMLError as err:
        print(err)