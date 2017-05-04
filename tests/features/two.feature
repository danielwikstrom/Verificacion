Feature: Reset button
    Empties the text field

    Scenario: Text in the field
        Given there is text
        When Reset button is pressed
        Then Text field is emptied
    Scenario: No text in the field
        Given there is no text
        When Reset button is pressed
        Then Text field is empty
