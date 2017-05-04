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

Feature: Execute button
    Counts the number of times a word appears
    Scenario: Text in the field
        Given there is text
        When Execute button is pressed
        Then the number of times every different word appears is shown
    Scenario: No text in the field
        Given there is no text
        When Execute button is pressed
        Then a warning message appears

Feature: Write in text field
    The text field gagablagblag
    Scenario: Less than 100 characters
        Given there are less than 100 characters in the text field
        When key a is pressed
        Then character a is typed

    Scenario: More than 100 characters
        Given 100 characters
        When key a is pressed
        Then no more characters are typed

