import json
_STRING_BASE_NAME = 'string_field_'

'''
2011 data type

[
  {
    "string_field_0": "United States of America",
    "string_field_2": "40-50",
    "string_field_3": "11",
    "string_field_45": ">$140,000",
    "string_field_30": null,
    "string_field_31": null,
    "string_field_32": null,
    "string_field_33": null,
    "string_field_34": "Python",
    "string_field_35": null,
    "string_field_36": null,
    "string_field_37": null,
    "string_field_38": null,
    "string_field_39": "C",
    "string_field_40": null,
    "string_field_41": null,
    "string_field_42": null,
    "string_field_44": "I enjoy going to work",
    "string_field_43": "Linux",
    "string_field_5": "Fortune 1000 (1,000+)"
  }
]

'''

def read_file(path):
    with open(path) as f:
        data = json.load(f)

    return data

def extract_programming_languages(start, end, data):
    programming_languages = []
    for i in range(start, end + 1):
        language = data.get(f'{_STRING_BASE_NAME}{i}')
        if language is not None:
            programming_languages.append(language)

    return programming_languages



if __name__ == "__main__":
    data = read_file('raw_data/2011.json')
    programming_languages = extract_programming_languages(30, 42, data[0])
    print(programming_languages)
