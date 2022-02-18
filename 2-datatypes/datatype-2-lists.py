import yaml

my_file = "datatype-2-lists.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f"{key}: {value}")
            print(f"value: {value}")
            datatype=type(value)
            print(f"datatype : {datatype}")
            print()
    except yaml.YAMLError as err:
        print(err)