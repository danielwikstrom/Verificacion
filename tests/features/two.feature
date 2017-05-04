Feature: Reset button
    Empties the text field

    Scenario: Text in the field
        Given Open Firefox
        And go to "http://localhost:8000"
        And "hola" is introduced
        When "reset" button is pressed
        Then the text field is empty
        And close Firefox
    Scenario: No text in the field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the text field is empty
        When "reset" button is pressed
        Then the text field is empty
        And close Firefox