import unittest

from bob import (
    response,
)

# Tests adapted from `problem-specifications//canonical-data.json`
SURE = "Sure."
WHOA_CHILL_OUT = "Whoa, chill out!"
WHATEVER = "Whatever."
FINE_BE_THAT_WAY = "Fine. Be that way!"


class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(response("Tom-ay-to, tom-aaaah-to."), WHATEVER)

    def test_shouting(self):
        self.assertEqual(response("WATCH OUT!"), WHOA_CHILL_OUT)

    def test_shouting_gibberish(self):
        self.assertEqual(response("FCECDFCAAB"), WHOA_CHILL_OUT)

    def test_asking_a_question(self):
        self.assertEqual(
            response("Does this cryogenic chamber make me look fat?"), SURE
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(response("You are, what, like 15?"), SURE)

    def test_asking_gibberish(self):
        self.assertEqual(response("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(response("Hi there!"), WHATEVER)

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            response("It's OK if you don't want to go work for NASA."), WHATEVER
        )

    def test_forceful_question(self):
        self.assertEqual(
            response("WHAT'S GOING ON?"), "Calm down, I know what I'm doing!"
        )

    def test_shouting_numbers(self):
        self.assertEqual(response("1, 2, 3 GO!"), WHOA_CHILL_OUT)

    def test_no_letters(self):
        self.assertEqual(response("1, 2, 3"), WHATEVER)

    def test_question_with_no_letters(self):
        self.assertEqual(response("4?"), SURE)

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            WHOA_CHILL_OUT,
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(response("I HATE THE DENTIST"), WHOA_CHILL_OUT)

    def test_statement_containing_question_mark(self):
        self.assertEqual(response("Ending with ? means a question."), WHATEVER)

    def test_non_letters_with_question(self):
        self.assertEqual(response(":) ?"), SURE)

    def test_prattling_on(self):
        self.assertEqual(response("Wait! Hang on. Are you going to be OK?"), SURE)

    def test_silence(self):
        self.assertEqual(response(""), FINE_BE_THAT_WAY)

    def test_prolonged_silence(self):
        self.assertEqual(response("          "),  FINE_BE_THAT_WAY)

    def test_alternate_silence(self):
        self.assertEqual(response("\t\t\t\t\t\t\t\t\t\t"), FINE_BE_THAT_WAY)

    def test_multiple_line_question(self):
        self.assertEqual(
            response("\nDoes this cryogenic chamber make me look fat?\nNo."),
            WHATEVER,
        )

    def test_starting_with_whitespace(self):
        self.assertEqual(response("         hmmmmmmm..."), WHATEVER)

    def test_ending_with_whitespace(self):
        self.assertEqual(response("Okay if like my  spacebar  quite a bit?   "), SURE)

    def test_other_whitespace(self):
        self.assertEqual(response("\n\r \t"), FINE_BE_THAT_WAY)

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            response("This is a statement ending with whitespace      "), WHATEVER
        )


if __name__ == "__main__":
    unittest.main()
