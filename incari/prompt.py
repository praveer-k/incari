from incari.tests.examples import examples
system_message = f"""
Given an input text prompt produce output a sequence of nodes using the following list of possible Nodes:
Event Nodes
    [OnVariableChange]: Triggered when a specified variable changes value.
    [OnKeyRelease]: Triggered when a key is released.
    [OnKeyPress]: Triggered when a key is pressed.
    [OnClick]: Triggered when an element is clicked.
    [OnWindowResize]: Triggered when the window is resized.
    [OnMouseEnter]: Triggered when the mouse pointer enters an element.
    [OnMouseLeave]: Triggered when the mouse pointer leaves an element.
    [OnTimer]: Triggered at specified time intervals.

Action Nodes
    [Console]: Prints a message to the console.
    [Alert]: Displays an alert message.
    [Log]: Logs information for debugging purposes.
    [Assign]: Assigns a value to a variable.
    [SendRequest]: Sends a network request.
    [Navigate]: Navigates to a different URL or page.
    [Save]: Saves data to local storage or a database.
    [Delete]: Deletes specified data or records.
    [PlaySound]: Plays an audio file.
    [PauseSound]: Pauses an audio file.
    [StopSound]: Stops an audio file.

Transformation Nodes
    [Branch]: Conditional node that branches based on a true/false evaluation.
    [Map]: Transforms data from one format to another.
    [Filter]: Filters data based on specified criteria.
    [Reduce]: Reduces a list of items to a single value.
    [Sort]: Sorts data based on specified criteria.
    [GroupBy]: Groups data by a specified attribute.
    [Merge]: Merges multiple datasets into one.
    [Split]: Splits data into multiple parts based on criteria.

Display Nodes
    [Show]: Displays information on the screen.
    [Hide]: Hides information from the screen.
    [Update]: Updates the display with new information.
    [DisplayModal]: Displays a modal dialog.
    [CloseModal]: Closes an open modal dialog.
    [Highlight]: Highlights an element on the screen.
    [Tooltip]: Shows a tooltip with additional information.
    [RenderChart]: Renders a chart with specified data.

Data Nodes
    [FetchData]: Fetches data from an API or database.
    [StoreData]: Stores data in a variable or storage.
    [UpdateData]: Updates existing data.
    [DeleteData]: Deletes specified data.
    [CacheData]: Caches data for performance improvement.
"""
base_prompt = [[{"role": "system", "content": system_message }]]

for inout in examples[:3]:
    input_text, output_text = inout["input"], inout["output"]
    chat = [
        {"role": "user", "content":  input_text},
        {"role": "assistant", "content":  output_text}
    ]
    base_prompt.append(chat)



