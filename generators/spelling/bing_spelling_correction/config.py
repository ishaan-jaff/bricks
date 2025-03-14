from util.configs import build_generator_premium_config
from util.enums import State, SelectionType, RefineryDataType, BricksVariableType
from . import bing_spelling_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=bing_spelling_correction,
        input_example=INPUT_EXAMPLE,
        issue_id=248,
        tabler_icon="BrandBing",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "spelling",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "bing_spelling_correction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "language": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "en-US",
                    "allowedValues": [
                        "da-DK",
                        "de-AT",
                        "de-CH",
                        "de-DE",
                        "en-AU",
                        "en-CA",
                        "en-GB",
                        "en-ID",
                        "en-IN",
                        "en-MY",
                        "en-NZ",
                        "en-PH",
                        "en-US",
                        "en-ZA",
                        "es-AR",
                        "es-CL",
                        "es-ES",
                        "es-MX",
                        "es-US",
                        "fi-FI",
                        "fr-BE",
                        "fr-CA",
                        "fr-CH",
                        "fr-FR",
                        "it-IT",
                        "ja-JP",
                        "ko-KR",
                        "nl-BE",
                        "nl-NL",
                        "no-NO",
                        "pl-PL",
                        "pt-BR",
                        "ru-RU",
                        "sv-SE",
                        "tr-TR",
                        "zh-CN",
                        "zh-HK",
                        "zh-TW",
                    ],
                    "description": "sets language, see all markets here: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/market-codes",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )
