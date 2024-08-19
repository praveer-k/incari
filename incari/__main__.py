import re
import torch
from functools import reduce
from operator import concat
from datasets import Dataset
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from incari.prompt import base_prompt
from incari.tests.examples import example_tuples
from incari.timeit import timeit


@timeit
def llm_response(input_text, model_name):
    print(f"Using model: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    messages = reduce(concat, base_prompt) + [{"role": "user", "content": input_text }]
    output = pipe(messages, max_new_tokens=128)[0]
    response: str = output["generated_text"]
    response = response[-1]['content'].strip()
    return response

def add_spaces_to_labels(label):
    # Add space before each capital letter except at the start
    return re.sub(r'(?<!^)(?<!\s)([A-Z])', r' \1', label)

def classify_label(text, model_name):
    texts = [
        "Triggered when a specified variable changes value.",
        "Triggered when a key is released.",
        "Triggered when a key is pressed.",
        "Triggered when an element is clicked.",
        "Triggered when the window is resized.",
        "Triggered when the mouse pointer enters an element.",
        "Triggered when the mouse pointer leaves an element.",
        "Triggered at specified time intervals.",
        "Prints a message to the console.",
        "Displays an alert message.",
        "Logs information for debugging purposes.",
        "Assigns a value to a variable.",
        "Sends a network request.",
        "Navigates to a different URL or page.",
        "Saves data to local storage or a database.",
        "Deletes specified data or records.",
        "Plays an audio file.",
        "Pauses an audio file.",
        "Stops an audio file.",
        "Conditional node that branches based on a true/false evaluation.",
        "Transforms data from one format to another.",
        "Filters data based on specified criteria.",
        "Reduces a list of items to a single value.",
        "Sorts data based on specified criteria.",
        "Groups data by a specified attribute.",
        "Merges multiple datasets into one.",
        "Splits data into multiple parts based on criteria.",
        "Displays information on the screen.",
        "Hides information from the screen.",
        "Updates the display with new information.",
        "Displays a modal dialog.",
        "Closes an open modal dialog.",
        "Highlights an element on the screen.",
        "Shows a tooltip with additional information.",
        "Renders a chart with specified data.",
        "Fetches data from an API or database.",
        "Stores data in a variable or storage.",
        "Updates existing data.",
        "Deletes specified data.",
        "Caches data for performance improvement."
    ]
    candidate_labels = [
        "OnVariableChange", "OnKeyRelease", "OnKeyPress", "OnClick",
        "OnWindowResize", "OnMouseEnter", "OnMouseLeave", "OnTimer",
        "Console", "Alert", "Log", "Assign", "SendRequest", "Navigate",
        "Save", "Delete", "PlaySound", "PauseSound", "StopSound",
        "Branch", "Map", "Filter", "Reduce", "Sort", "GroupBy",
        "Merge", "Split", "Show", "Hide", "Update", "DisplayModal",
        "CloseModal", "Highlight", "Tooltip", "RenderChart", "FetchData",
        "StoreData", "UpdateData", "DeleteData", "CacheData"
    ]
    if text in candidate_labels:
        return text
    classifier = pipeline("zero-shot-classification", model=model_name, device=0 if torch.cuda.is_available() else -1)
    formatted_labels = [add_spaces_to_labels(label) + ": " + texts[i] for i, label in enumerate(candidate_labels)]
    formatted_text = add_spaces_to_labels(text)
    result = classifier(formatted_text, formatted_labels, multi_label=False)
    print(f"Text: {text}\nFormatted Labels:{formatted_labels}\nClassification: {result}\n")
    highest_score_index = result['scores'].index(max(result['scores']))
    highest_label = result['labels'][highest_score_index]
    print("~"*100)
    print(f'{formatted_text} ---> {highest_label}')
    print(f'{text} ---> {highest_label.replace(" ", "")}')
    print("~"*100)
    return highest_label.replace(" ", "")

def OnVariableChange():
    pass

def main():
    # "google/codegemma-2b",
    # "google/gemma-2-2b",
    # "stabilityai/stable-code-3b",
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # "facebook/blenderbot-400M-distill"
    # "stabilityai/stablelm-2-zephyr-1_6b"
    model_name = "stabilityai/stablelm-2-zephyr-1_6b"
    for example in example_tuples[3:]:
        input_text, output_text = example
        response = llm_response(input_text=input_text, model_name=model_name)
        seq = [step.strip("[]") for step in response.split("\n")]
        seq = [classify_label(step, model_name=model_name) for step in seq]
        seq = "\n".join([f'[{step}]' for step in seq])
        print("-"*100)
        print(input_text)
        print("-"*100)
        print(response)
        print("-"*100)
        print(seq)
        print("-"*100)
        print(output_text)
        print("="*100)

    
    