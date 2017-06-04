Feature: Write in text field
    There is a text field where one can type in text to have it analized
    Scenario: Empty text field
        Given Open Firefox
        And go to "http://localhost:8000"
        And the "id_url" is empty
        When "hola" is introduced in "id_url"
        Then there is only "hola" in "id_url"
        And close Firefox

    Scenario: More than 200 characters
        Given Open Firefox
        And go to "http://localhost:8000"
        And "ThSTuMsjxXDhGGHfRYNqKXTNGBpJOKBbBaFLENvWKCHCZlVIesOrFYybLYUzAOBvjkstMGLeZqGeNMMBlHDHdMfxlJsZMKGLhCzThanrMDgqdJuIIfMExwsumjwnjWgQTcDwAVYFUpIvMHRrWDcvyapwGWmKoMUWkoSWiNEiJBUXEbqLUbOxnKnXUpBvHIigRABlFzoY" is introduced in "id_url"
        When "rex un policia diferente" is introduced in "id_url"
        Then text in "id_url" has not changed
        And close Firefox
