import unittest
from unittest.mock import patch
from ModuleSixMilestone import (
    get_command,
    validate_move_command,
    validate_command,
    handle_direction_command,
    handle_command,
)


class TestModuleSixMilestone(unittest.TestCase):
    def test_get_command(self):
        # Simulate user input and assert the returned command
        with patch("builtins.input", return_value="go North") as mock_input:
            command = get_command()
            self.assertEqual(command, ("go", "North"))
            mock_input.assert_called_once_with("Enter Command > ")

    def test_validate_move_command_valid(self):
        # Test a valid move command
        command = ("go", "North")
        current_room = {"North": "Bedroom"}
        self.assertTrue(validate_move_command(command, current_room))

    def test_validate_move_command_invalid_direction(self):
        # Test an invalid move command due to an unknown direction
        command = ("go", "West")
        current_room = {"North": "Bedroom"}
        with patch("builtins.print") as mock_print:
            result = validate_move_command(command, current_room)
            self.assertFalse(result)
            mock_print.assert_called_once_with("You cannot go that direction!")

    def test_validate_move_command_invalid_input(self):
        # Test an invalid move command due to incorrect direction format
        command = ("go", "Up")
        current_room = {"North": "Bedroom"}
        with patch("builtins.print") as mock_print:
            result = validate_move_command(command, current_room)
            self.assertFalse(result)
            mock_print.assert_called_once_with("Direction must be: <North|East|West|South>.")

    def test_validate_command_valid(self):
        # Test a valid command
        command = ("go", "North")
        current_room = {"North": "Bedroom"}
        self.assertTrue(validate_command(command, current_room))

    def test_validate_command_invalid_length(self):
        # Test an invalid command due to excessive arguments
        command = ("go", "North", "extra")
        current_room = {"North": "Bedroom"}
        with patch("builtins.print") as mock_print:
            result = validate_command(command, current_room)
            self.assertFalse(result)
            mock_print.assert_called_once_with("Invalid input!")

    def test_validate_command_invalid_input(self):
        # Test an invalid command due to unknown command type
        command = ("jump", "North")
        current_room = {"North": "Bedroom"}
        with patch("builtins.print") as mock_print:
            result = validate_command(command, current_room)
            self.assertFalse(result)
            mock_print.assert_called_once_with("Invalid input!")

    def test_handle_direction_command(self):
        # Test handling a direction command
        command = ("go", "East")
        current_room = {"East": "Cellar"}
        new_room = handle_direction_command(command, current_room)
        self.assertEqual(new_room, "Cellar")

    def test_handle_command_go(self):
        # Test handling a 'go' command
        command = ("go", "South")
        current_room = {"South": "Bedroom"}
        new_room, exit_program = handle_command(command, current_room)
        self.assertEqual(new_room, "Bedroom")
        self.assertFalse(exit_program)

    def test_handle_command_exit(self):
        # Test handling an 'exit' command
        command = ("exit", None)
        current_room = {"North": "Bedroom"}
        new_room, exit_program = handle_command(command, current_room)
        self.assertEqual(new_room, current_room)
        self.assertTrue(exit_program)


if __name__ == "__main__":
    unittest.main()
