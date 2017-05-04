Feature: Execute button

    Counts the number of times a word appears
    Scenario: "Rex un Policia Diferente" in the text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And "Rex un Policia Diferente" is introduced
        And "execute" button is pressed
        Then is in result
        And close Firefox

    Scenario: Nothing in the text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the text field is empty
        When "execute" button is pressed
        Then the text field is empty
        And close Firefox

    Scenario: only spaces
         Given Open Firefox
        And go to "http://localhost:8000"
        And "   " is introduced
        When "execute" button is pressed
        Then go to "http://localhost:8000"
        And close Firefox
