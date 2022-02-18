import yaml

my_file = "basics-structure-5-nulls.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.load(stream, Loader=yaml.SafeLoader)
        for key, value in data.items():
            print()
            print(f"key: {key}")
            print(f"value: {value}")
            datatype=type(value)
            print(f"The datatype of {value} is {datatype}")
    except yaml.YAMLError as err:
        print(err)