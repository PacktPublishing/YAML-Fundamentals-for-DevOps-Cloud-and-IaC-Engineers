import yaml

my_file = "basics-structure-1.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for k, v in data.items():
            print()
            print(f"key: {k}")
            print(f"value: {v}")
            datatype = type(v)
            print(f"The datatype of {v} is {datatype}")
    except yaml.YAMLError as err:
        print(err)