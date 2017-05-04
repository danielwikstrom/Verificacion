Feature: Execute button
    Counts the number of times a word appears
    Scenario: "Rex un Policia Diferente" in the text field
        Given there is "Rex un Policia Diferente" in the text field
        When Execute button is pressed
        Then the number of times every different word appears is shown

    Scenario: Nothing in the text field
        Given there is nothing in the text field
        When Execute button is pressed
        Then a warning message appears

    Scenario: only spaces
        Given there is "   " in the text field
        When button is pressed
        Then no more characters are typed
