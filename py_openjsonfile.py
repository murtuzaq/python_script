import json

def open_json_file( file ):
    print("open json file :", file)
    try:
        with open(file) as json_file:
            # json file may be improperly formatted, and thus crash without a try/catch
            try:
                data = json.load(json_file)
                return data
            except ValueError as e:
                print("E: fail to parse json file")

    except IOError:
        print("E: fail to open file", file)

    return None


/
def main():
    json_data = open_json_file("more.json" )
    print(json_data)

if __name__ == '__main__':
    main()