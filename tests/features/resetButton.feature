Feature: Reset button
    Empties the text field

    Scenario: Text in the field
        Given Open Firefox
        And go to "http://localhost:8000"
        And "hola" is introduced in "id_url"
        When "reset" button is pressed
        Then the "id_url" is empty
        And close Firefox
    Scenario: No text in the field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the "id_url" is empty
        When "reset" button is pressed
        Then the "id_url" is empty
        And close Firefox