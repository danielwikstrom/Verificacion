Feature: Write in text field
    In order analize a url
    As a user
    We'll use the url proper url
    Scenario: Empty text field
        Given Open chrome
        And go to "http://localhost:8000"
        And the "id_url" is empty
        When "hola" is introduced in "id_url"
        Then there is only "hola" in "id_url"
        And close chrome

    Scenario: More than 200 characters
        Given Open chrome
        And go to "http://localhost:8000"
        And "ThSTuMsjxXDhGGHfRYNqKXTNGBpJOKBbBaFLENvWKCHCZlVIesOrFYybLYUzAOBvjkstMGLeZqGeNMMBlHDHdMfxlJsZMKGLhCzThanrMDgqdJuIIfMExwsumjwnjWgQTcDwAVYFUpIvMHRrWDcvyapwGWmKoMUWkoSWiNEiJBUXEbqLUbOxnKnXUpBvHIigRABlFzoY" is introduced in "id_url"
        When "rex un policia diferente" is introduced in "id_url"
        Then text in "id_url" has not changed
        And close chrome
