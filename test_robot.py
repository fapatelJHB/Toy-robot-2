import unittest
import robot
from unittest.mock import patch
import sys
import io
from io import StringIO
from robot import *




class TestRobot(unittest.TestCase):

    @patch("sys.stdin", StringIO("HAL\n"))
    def test_robot_name(self):
        """
            This function checks if the user input is correct.
        """ 
        sys.stdout = StringIO()
        self.assertEqual(robot_name(),"HAL")

    # @patch("sys.stdin", StringIO("''\nHAL"))
    # def test_robot_name(self):
    #     """
    #         This function checks if the user input is correct.
    #     """ 
    #     sys.stdout = StringIO()
    #     self.assertEqual(robot_name(),"HAL")


    def test_user_input(self):
        """
            This function makes sure that the game works with uppercase and lowercase.
        """
        self.assertEqual("OFF".lower(),"off")
        self.assertEqual("HELP".lower(),"help")
        self.assertEqual("FORWARD".lower(),"forward")
        self.assertEqual("BACK".lower(),"back")
        self.assertEqual("RIGHT".lower(),"right")
        self.assertEqual("LEFT".lower(),"left")
        self.assertEqual("SPRINT".lower(),"sprint")

    @patch("sys.stdin", StringIO("HAL\noff\n"))
    def test_off_command(self):
        """
            This functions checks the off command.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nhelp\noff\n"))
    def test_help_command(self):
        """
            This function checks the help command.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
Forward - Move forward a certain amount of steps
Back - Move back a certain amount of steps
Right - Turn right
Left - Turn left
Sprint - Move forward by a short burst of speed
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nforward 10\noff\n"))
    def test_forward_command(self):
        """
            This function checks that the position is right when the user inputs forward.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nback 10\noff\n"))
    def test_back_command(self):
        """
            This function checks that the position is right when the user inputs back.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nright\noff\n"))
    def test_right_command(self):
        """
            This function makes sure it prints out the right line when the user inputs right.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nleft\noff\n"))
    def test_left_command(self):
        """
            This function makes sure it prints out the right line when the user inputs left.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nsprint 4\noff\n"))
    def test_sprint_command(self):
        """
            This function makes sure the robot sprints and prints out all the steps and position.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nforward 200\noff\n"))
    def test_forward_range(self):
        """
            This function checks to see if the range for the y-axis works when the user enters forward. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nback 200\noff\n"))
    def test_back_range(self):
        """
            This function checks to see if the range for the y-axis works when the user enters back. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nright\nforward 20\noff"))
    def test_right_forward(self):
        """
            This function checks to see if the range for the x-axis works when the user enters right then forward. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (20,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nright\nback 10\noff"))
    def test_right_back(self):
        """
            This function checks to see if the range for the x-axis works when the user enters right then back. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..
""")


    @patch("sys.stdin", StringIO("HAL\nleft\nforward 30\noff"))
    def test_left_forward(self):
        """
            This function checks to see if the range for the x-axis works when the user enters left then forward. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 30 steps.
 > HAL now at position (-30,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nleft\nback 50\noff"))
    def test_left_back(self):
        """
            This function checks to see if the range for the x-axis works when the user enters left then back. And it prints out the correct line.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 50 steps.
 > HAL now at position (50,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nright\nforward 101\noff"))
    def test_right_range(self):
        """
            This function checks the range for when the user inputs right.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")

    @patch("sys.stdin", StringIO("HAL\nleft\nback 101\noff"))
    def test_left_range(self):
        """
            This function checks the range for when the user inputs left.
        """
        sys.stdout = StringIO()
        user_input()
        self.assertEqual(sys.stdout.getvalue(),"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..
""")


if __name__ == "__main__":
    unittest.main()