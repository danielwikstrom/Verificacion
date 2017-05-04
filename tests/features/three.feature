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
