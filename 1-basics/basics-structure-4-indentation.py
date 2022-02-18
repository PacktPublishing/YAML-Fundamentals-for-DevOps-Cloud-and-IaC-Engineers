import yaml

my_file = "basics-structure-4-indentation.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(" ")
            print(f"key: {key}")
            print(f"value: {value}")
            for k, v in value.items():
                print(" ")
                print(f"key: {k}")
                print(f"value: {v}")

    except yaml.YAMLError as err:
        print(err)