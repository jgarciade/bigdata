import json
import re
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


class Cleaner():
    '''
    cleans data from JSON files to fit business logic
    '''
    _salary_ranges = {
        1: [0, 20],
        2: [20, 40],
        3: [40, 60],
        4: [60, 80],
        5: [80, 100],
        6: [100, 120],
        7: [120, 140]
    }

    def __init__(self, data_fields, satisfaction_map, path_to_file):
        '''
        @data_fields: { age': 2, 'experience': 3, 'region': 0, 'salary': 100,
                        'programming_languages': [56, 69], 'satisfaction': 99,
                        'gender': None, 'os': 81, 'company_size': 5
                      }
        @satisfaction_map: {enjoy: 5, hurts: 4, not happy: 1, bills: 3}
        @path_to_file: /path
        '''
        self._data_fields = data_fields
        self._satisfaction_map = satisfaction_map
        self._path_to_file = path_to_file
        self._raw_data = None

    def _read_file(self):
        with open(self._path_to_file) as f:
            self._raw_data = json.load(f)

    def _extract_programming_languages(self, start, end, data):
        programming_languages = []
        for i in range(start, end + 1):
            language = data.get(f'{_STRING_BASE_NAME}{i}')
            if language is not None:
                programming_languages.append(language)

        return programming_languages

    def _extract_satisfaction(self, value):
        for (key, value) in self._satisfaction_map.items():
            if key in value:
                return value

        return None

    def _extract_salary_operator(self, value):
        if value is None:
            return value
        salary_operator = value[:1]
        if salary_operator != '>' and salary_operator != '<':
            salary_operator = None
        return salary_operator

    def _extract_raw_salary(self, data):
        field = self._data_fields.get('salary')
        value = data.get(f'{_STRING_BASE_NAME}{field}')
        salary_operator = self._extract_salary_operator(value)

        # Extracts the max raw salary value
        value = value.replace(',', '')
        raw_salary = re.findall(r'\d+', value)
        raw_salary = raw_salary[-1:][0]
        raw_salary = float(raw_salary)

        if salary_operator == '>':
            raw_salary += 1
        elif salary_operator == '<':
            raw_salary -= 1

        return raw_salary

    def _get_salary_range(self, data):
        salary = self._extract_raw_salary(data)
        salary_range = '>140k'
        for ran in self._salary_ranges.values():
            if salary in range(ran[0], ran[1] + 1):
                salary_range = f'{ran[0]}-{ran[0]}'
        return salary_range

    def _extract_values(self):
        self._read_file()
        for data in self._raw_data:
            fields = {}
            pl_indexes = self._data_fields.get('programming_languages')
            pl = self._extract_programming_languages(pl_indexes[0],
                                                     pl_indexes[1],
                                                     data)
            fields.update({'programming_languages': pl})
            import ipdb; ipdb.set_trace()
            fields.update({'salary_range': self._get_salary_range(data)})
            print(fields)
            break


kwargs = {'data_fields': {'age': 2, 'experience': 3, 'region': 0, 'salary': 45,
                          'programming_languages': [30, 42], 'satisfaction': 44,
                          'gender': None, 'os': 43, 'company_size': 5},
            'satisfaction_map': {'enjoy': 5, 'hurts': 4, 'not happy': 1, 'bills': 3},
            'path_to_file': 'raw_data/2011.json'
            }
cleaner = Cleaner(**kwargs)
cleaner._extract_values()
