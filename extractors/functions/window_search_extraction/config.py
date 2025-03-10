from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import window_search_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=window_search_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=41,
        tabler_icon="AppWindow",
        state=State.PUBLIC.value,
        min_refinery_version="1.7.0",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "functions",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "window_search_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "WINDOW": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 4,
                    "description": "choose any window size here",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "PERSON",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_LISTS": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "either lookup lists or lookup values or both",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LOOKUP_LIST.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_VALUES": {
                    "selectionType": SelectionType.LIST.value,
                    "defaultValue": "Max",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )
