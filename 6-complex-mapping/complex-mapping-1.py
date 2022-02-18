import yaml

my_file = "complex-mapping-1.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f"key: {key}")
            print(f"value: {value}")
            datatype=type(value)
            print()
            for key, value in value.items():
                print(f"key: {key}")
                print(f"value: {value}")
                print("-")
    except yaml.YAMLError as err:
        print(err)