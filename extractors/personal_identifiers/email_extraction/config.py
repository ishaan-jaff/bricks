from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import email_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=email_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=23,
        tabler_icon="Mail",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "personal_identifiers",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "email_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "email",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
