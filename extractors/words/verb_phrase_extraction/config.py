from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import verb_phrase_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=verb_phrase_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=238,
        tabler_icon="SquareLetterV",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "verb_phrase_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "only texts allowed",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TOKENIZER": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "en_core_web_sm",
                    "allowedValues": ["en_core_web_sm", "de_core_news_sm"],
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "verb-action",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
