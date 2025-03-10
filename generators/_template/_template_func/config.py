from util.configs import build_generator_function_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import _template_func, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        # strapi information
        function=_template_func,
        input_example=INPUT_EXAMPLE,
        issue_id=157,
        tabler_icon="MoodCrazyHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "_template_func",
        ],  # first entry should be parent directory
        # !!! bricks integrator information for the Kern AI team, you can leave this blank !!! 
        integrator_inputs={
            "globalComment": "Only for english text.",
            "name": "_template_func",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": ["positive", "neutral", "negative"],
            "variables": {
                "ATTRIBUTE": {  # previously ATTRIBUTE, never optional
                    "selectionType": SelectionType.CHOICE.value,  # choice of all available text attributes
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                    "description": "The refinery attribute that contains the data to be used.",
                },
                "BASE_SENTENCE": {
                    "selectionType": SelectionType.STRING.value,  # input can be any non-predefined string
                    "defaultValue": "This is a test sentence.",
                    "description": "The sentence to be used as a base for the sentiment analysis.",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "MODE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "allowedValues": ["classification", "scores"],
                    "defaultValue": "classification",
                    "description": "Choose classification to return either positive, neutral or negative. Choose scores to retrieve a float score.",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                    "optional": "true",  # if optional variable is missing it defaults to "false"
                },
                "MIN_SCORE": {
                    "selectionType": SelectionType.RANGE.value,
                    "defaultValue": 100,
                    "allowedValueRange": [0, 100],  # from 0 to 100
                    "description": "The lowest possible sentiment score.",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
            },
        },
    )
