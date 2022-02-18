import yaml

my_file = "basics-structure-3-spaces.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print()
            print(f"key: {key}")
            print(f"value: {value}")
    except yaml.YAMLError as err:
        print(err)