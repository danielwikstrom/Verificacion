Feature: Execute button
    Counts the number of times every word appears in a text
    Scenario: An article in the text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And "http://www.publico.es/actualidad/guerra-taxistas-conductores-uber-cabify.html" is introduced in "id_url"
        And "execute" button is pressed
        Then is in result
        And close Firefox

    Scenario: Nothing in the text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the "id_url" is empty
        When "execute" button is pressed
        Then the "id_url" is empty
        And close Firefox

    Scenario: only spaces
        Given Open Firefox
        And go to "http://localhost:8000"
        And "   " is introduced in "id_url"
        When "execute" button is pressed
        Then go to "http://localhost:8000"
        And close Firefox
