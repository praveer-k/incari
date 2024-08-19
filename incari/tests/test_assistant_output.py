from incari.__main__ import llm_response
from incari.tests.examples import example_tuples
import pytest

@pytest.mark.parametrize("input_text, example_output", example_tuples)
def test_examples(input_text, example_output):
    response = llm_response(input_text=input_text, model="stabilityai/stablelm-2-zephyr-1_6b")
    assert response == example_output
