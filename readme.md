# CRUD exercises

This small repo contains a CRUD testing implementation with the usage of Python libraries. All CRUD endpoints were extracted from [CrudCrud page]("https://crudcrud.com/").
The test cases related with this exercise are:
* test_01_get_address
* test_02_create_new_unicorn
* test_03_get_unicorn
* test_04_update_unicorn_info
* test_05_get_updated_unicorn
* test_06_delete_unicorn
* test_07_validate_deleted_unicorn

Note: The design for the test suite and all test cases is to be executed continuously, that's why it includes # numbers in the test name. This is usually a bad practice during real-work automation testing, this naming is just for demo purposes.
## Installation
Clone repository:

```
git clone 
```

Setup Python Interpreter:
```
* Select 'myenv' as Python Interpreter under APIAutomationExercise/myenv 
```

## Usage
### How to run all test cases?
```
cd APIAutomationExercise/tests
pytest ExerciseTestCases.py
```

## Debug
### Common issues
For any reason, if test_01_get_address fails. The reason might be that address_id has been expired. In order to fix this issue, and continue with the next tests execution, follow the next steps:
* Navigate to [CrudCrud page]("https://crudcrud.com/").
* Copy the 30 character address_id value ( I.e. 8cd8eac03cb948a8bc207075622b700d) from generated URL into data/addressId.json
* Run the test again

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
