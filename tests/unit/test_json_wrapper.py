from tasssktracker.tasssktracker.json_wrapper import JSON
import pytest
import json
import sys

def test_json_load_success(mocker):
    # Mock data and setup
    mock_data = {"key": "value"}
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=json.dumps(mock_data)))

    # Instance of JSON class
    json_handler = JSON()

    # Load JSON and verify
    result = json_handler.load("dummy_path.json")
    mock_open.assert_called_once_with("dummy_path.json", 'r', encoding='utf-8')
    assert result == mock_data

def test_json_load_file_not_found(mocker):
    # Mock open to raise FileNotFoundError
    mocker.patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    
    # Completely mock sys.exit to verify it's called
    mock_exit = mocker.patch('sys.exit', side_effect=SystemExit)
    
    # Capture stderr output
    mock_stderr = mocker.patch('sys.stderr.write')
    
    # Instance of JSON class
    json_handler = JSON()

    # Verify that SystemExit is raised
    with pytest.raises(SystemExit):
        json_handler.load("nonexistent_file.json")
    
    # Verify sys.exit was called once with exit code 1
    mock_exit.assert_called_once_with(1)
    
    # Verify error message was printed to stderr
    # Check that the stderr write calls match the expected behavior
    assert mock_stderr.call_count == 2
    assert mock_stderr.call_args_list[0][0][0] == "Error: Failure to load file: File not found"
    assert mock_stderr.call_args_list[1][0][0] == "\n"

def test_json_load_invalid_format(mocker):
    # Mock open with invalid JSON data
    mocker.patch("builtins.open", mocker.mock_open(read_data="invalid json"))

    # Completely mock sys.exit to verify it's called
    mock_exit = mocker.patch('sys.exit', side_effect=SystemExit)

    # Redirect stderr and verify
    mock_stderr = mocker.patch("sys.stderr.write")

    # Instance of JSON class
    json_handler = JSON()

    with pytest.raises(SystemExit):
        json_handler.load("invalid.json")

    # Verify sys.exit was called once with exit code 1
    mock_exit.assert_called_once_with(1)

    # Verify error message was printed to stderr
    # Check that the stderr write calls match the expected behavior
    assert mock_stderr.call_count == 2
    assert mock_stderr.call_args_list[0][0][0] == "Error: Invalid JSON format: Expecting value: line 1 column 1 (char 0)"
    assert mock_stderr.call_args_list[1][0][0] == "\n"

def test_json_dump_success(mocker):
    # Mock the open function
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    
    # Instance of JSON class
    json_handler = JSON()
    
    # Test data
    test_data = {"key": "value"}
    
    # Dump JSON data
    json_handler.dump(test_data, "dummy_path.json")
    
    # Verify that open was called with the correct arguments
    mock_open.assert_called_once_with("dummy_path.json", 'w', encoding='utf-8')
    
    # Capture all write calls
    write_calls = mock_open().write.call_args_list
    
    # Reconstruct the output by joining all write calls
    written_data = ''.join(call[0][0] for call in write_calls)
    
    # Assert the written data matches the expected JSON string
    assert written_data == json.dumps(test_data)

def test_json_dump_unknown_error(mocker):
    # Mock open to raise an OSError
    mocker.patch("builtins.open", side_effect=OSError("Disk full"))
    
    # Completely mock sys.exit to verify it's called
    mock_exit = mocker.patch('sys.exit', side_effect=SystemExit)
    
    # Mock sys.stderr.write to capture the error output
    mock_stderr = mocker.patch('sys.stderr.write')
    
    # Instance of JSON class
    json_handler = JSON()
    
    # Test data
    test_data = {"key": "value"}
    
    # Verify that SystemExit is raised
    with pytest.raises(SystemExit):
        json_handler.dump(test_data, "dummy_path.json")
    
    # Verify sys.exit was called once with exit code 1
    mock_exit.assert_called_once_with(1)
    
    # Verify the error message was printed to stderr
    assert mock_stderr.call_count == 2
    assert mock_stderr.call_args_list[0][0][0] == "Error: unknown error: Disk full"
    assert mock_stderr.call_args_list[1][0][0] == "\n"
