Feature: Reset button
    In order to reset the text
    As a user
    We'll use the reset button
    Scenario: Text in the field
        Given Open chrome
        And go to "http://localhost:8000"
        And "hola" is introduced in "id_url"
        When "reset" button is pressed
        Then the "id_url" is empty
        And close chrome
    Scenario: No text in the field
        Given Open chrome
        And go to "http://localhost:8000"
        And the "id_url" is empty
        When "reset" button is pressed
        Then the "id_url" is empty
        And close chrome