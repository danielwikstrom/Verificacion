Feature: Write in text field
    There is a text field where one can type in text to have it analized
    Scenario: Empty text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the text field is empty
        When "hola" is introduced
        Then there is only "hola" in text field
        And close Firefox

    Scenario: More than 100 characters
        Given Open Firefox
        And go to "http://localhost:8000"
        And "kf3hjFMWJ05IVsNn6qA8DOVwKVkGiI7IuNk2 AEDvgl18Duy3t 40rJuuHZUnD mnPyU UZgDu tLXYY r1C2 qY OIZl EnFvce gaga blag blag" is introduced
        When "rex un policia diferente" is introduced
        Then text in text field has not changed
        And close Firefox
