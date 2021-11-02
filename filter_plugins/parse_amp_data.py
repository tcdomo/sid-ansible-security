from ansible.module_utils.common.text.converters import to_native
import json

def parse_amp_data(data):
    print(json.dumps(data, indent=2))
    return data


class FilterModule(object):
    def filters(self):
        return {'parse_amp_data': parse_amp_data}



if __name__=="main":
    print("running program")
    f = open('data.json',)
    data = json.load(f)
    parse_amp_data(data)

    f.close()
