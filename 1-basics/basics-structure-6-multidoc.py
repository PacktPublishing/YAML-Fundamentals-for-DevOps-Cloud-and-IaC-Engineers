import yaml

my_file = "basics-structure-6-multidoc.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.load_all(stream, Loader=yaml.SafeLoader)
        count = 0
        for yaml_doc in data:
            doc_no = count + 1
            print(f"<<<<<   YAML Document : {doc_no}   >>>>>")
            print(yaml_doc)
            for key, value in yaml_doc.items(): 
                print(f"key: {key}")
                print(f"value: {value}")
                print()
            count = count + 1
    except yaml.YAMLError as err:
        print(err)