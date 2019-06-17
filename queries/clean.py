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

    _company_size_range = {
        1: [1, 25],
        2: [26, 100],
        3: [101, 1000]
    }

    _age_range = {
        1: [0, 20],
        2: [21, 25],
        3: [26, 30],
        4: [31, 40],
        5: [41, 50]
    }

    _experience_range = {
        1: [0, 2],
        2: [3, 5],
        3: [6, 10],
        4: [10, 15],
        5: [15, 20],
        6: [20, 90]
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

    def _create_list_from_field(self, data, field):
        result = []
        pl_indexes = self._data_fields.get(field)
        if len(pl_indexes) == 1:
            value = data.get(f'{_STRING_BASE_NAME}{pl_indexes[0]}')
            is_valid = self._is_valid_value(value)
            if not is_valid:
                value = None
            result.append(value)
            return result

        for i in range(pl_indexes[0], pl_indexes[1] + 1):
            value = data.get(f'{_STRING_BASE_NAME}{i}')
            is_valid = self._is_valid_value(value)

            if value is not None and is_valid:
                result.append(value)

        return result

    def _extract_programming_languages(self, data):
        return self._create_list_from_field(data, 'programming_languages')

    def _extract_os(self, data):
        return self._create_list_from_field(data, 'os')

    def _extract_upper_limit_num_from_string(self, value):
        # Extracts the max raw salary value
        value = value.replace(',', '')
        number = re.findall(r'\d+', value)
        if len(number) == 0:
            return None
        number = number[-1:][0]
        number = float(number)

        return number

    def _get_satisfaction(self, data):
        field = self._data_fields.get('satisfaction')
        satisfaction_answer = data.get(f'{_STRING_BASE_NAME}{field}')
        is_valid = self._is_valid_value(satisfaction_answer)
        if satisfaction_answer is None or not is_valid:
            return None

        for (key, value) in self._satisfaction_map.items():
            if key in satisfaction_answer:
                return value

        return None

    def _extract_range_operator(self, value):
        if value is None:
            return value
        salary_operator = value[:1]
        if salary_operator != '>' and salary_operator != '<':
            salary_operator = None
        return salary_operator

    def _extract_raw_number_from_range(self, value):
        range_operator = self._extract_range_operator(value)

        raw_number = self._extract_upper_limit_num_from_string(value)
        if raw_number is None:
            return None

        if range_operator == '>':
            raw_number += 1
        elif range_operator == '<':
            raw_number -= 1

        return raw_number

    def _get_salary_range(self, data):
        field = self._data_fields.get('salary')
        value = data.get(f'{_STRING_BASE_NAME}{field}')
        is_valid = self._is_valid_value(value)
        if value is None or not is_valid:
            return None

        salary = self._extract_raw_number_from_range(value)
        if salary is None:
            return None

        salary_range = '>140k'
        salary /= 1000

        for ran in self._salary_ranges.values():
            if salary in range(ran[0], ran[1] + 1):
                salary_range = f'{ran[0]}-{ran[1]}'
        return salary_range

    def _get_company_size_range(self, data):
        field = self._data_fields.get('company_size')
        value = data.get(f'{_STRING_BASE_NAME}{field}')

        is_valid = self._is_valid_value(value)
        if value is None or not is_valid:
            return None

        value = self._extract_raw_number_from_range(value)

        company_size_range = '>1000'
        for ran in self._company_size_range.values():
            if value in range(ran[0], ran[1] + 1):
                company_size_range = f'{ran[0]}-{ran[1]}'
        return company_size_range

    def _get_age_range(self, data):
        field = self._data_fields.get('age')
        value = data.get(f'{_STRING_BASE_NAME}{field}')
        is_valid = self._is_valid_value(value)
        if value is None or not is_valid:
            return None

        age_range = '>50'
        age = self._extract_raw_number_from_range(value)
        if age is None:
            return None

        for ran in self._age_range.values():
            if age in range(ran[0], ran[1] + 1):
                age_range = f'{ran[0]}-{ran[1]}'
        return age_range

    def _get_experience_range(self, data):
        field = self._data_fields.get('experience')
        value = data.get(f'{_STRING_BASE_NAME}{field}')
        is_valid = self._is_valid_value(value)
        if value is None or not is_valid:
            return None

        experience_range = None
        experience = self._extract_raw_number_from_range(value)
        if experience is None:
            return None

        for ran in self._age_range.values():
            if experience in range(ran[0], ran[1] + 1):
                experience_range = f'{ran[0]}-{ran[1]}'
        return experience_range

    def _get_raw_value_from_data(self, data, key):
        key_index = self._data_fields.get(key, None)
        if key_index is None:
            return None

        value = data.get(f'{_STRING_BASE_NAME}{key_index}')
        is_valid = self._is_valid_value(value)
        if not is_valid:
            value = None
        return value

    def _is_valid_value(self, value):
        if value is None:
            return False
        is_valid = True
        is_valid = is_valid and ('?' not in value)
        is_valid = is_valid and ('please' not in value.lower())
        is_valid = is_valid and ('response' not in value.lower())

        return is_valid

    def _extract_values(self):
        self._read_file()
        results = []
        for data in self._raw_data:
            fields = {}
            fields.update({'programming_languages': self._extract_programming_languages(data)})
            fields.update({'os': self._extract_os(data)})
            fields.update({'salary_range': self._get_salary_range(data)})
            fields.update({'satisfaction': self._get_satisfaction(data)})
            fields.update({'company_size_range': self._get_company_size_range(data)})
            fields.update({'age_range': self._get_age_range(data)})
            fields.update({'experience_range': self._get_experience_range(data)})
            fields.update({'gender': self._get_raw_value_from_data(data, 'gender')})
            fields.update({'region': self._get_raw_value_from_data(data, 'region')})
            fields.update({'gender': self._get_raw_value_from_data(data, 'gender')})
            results.append(fields)
        return results

    def clean_and_save(self, file_path_to_save):
        results = self._extract_values()
        with open(file_path_to_save, 'w') as outfile:
            json.dump(results, outfile, indent=4, sort_keys=True)

kwargs = {'data_fields': {'age': 2, 'experience': 3, 'region': 0, 'salary': 45,
                        'programming_languages': [30, 42], 'satisfaction': 44,
                        'gender': None, 'os': [43], 'company_size': 5},
        'satisfaction_map': {'enjoy': 5, 'hurts': 4, 'not happy': 1, 'bills': 3},
        'path_to_file': 'raw_data/2011.json'
        }
cleaner = Cleaner(**kwargs)
cleaner.clean_and_save('clean_files/2011.json')
