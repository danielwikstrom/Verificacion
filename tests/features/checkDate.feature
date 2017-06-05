Feature: Date button
    Checks if there exists any entry for the date entered in the database
    Scenario: There is a entry
        Given Open chrome
        And go to "http://localhost:8000"
        And "2017-06-03" is introduced in "id_id"
        And "search" button is pressed
        Then is in result
        And close chrome

    Scenario: Nothing in the text field
        Given Open chrome
        And go to "http://localhost:8000"
        And the "id_id" is empty
        When "search" button is pressed
        Then go to "http://localhost:8000"
        And close chrome

    Scenario: only spaces
        Given Open chrome
        And go to "http://localhost:8000"
        And "   " is introduced in "id_id"
        When "search" button is pressed
        Then go to "http://localhost:8000"
        And close chrome
