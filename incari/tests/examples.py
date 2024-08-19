examples = [
{
"input":  "Navigate to a new page after a delay of 3 seconds when the user clicks a button.",
"output": """[OnClick]
[Delay]
[Navigate]"""
},
{
"input": "Fetch user data and display it in a modal when a button is clicked.",
"output": """[OnClick]
[FetchData]
[DisplayModal]"""
},
{
"input": "Log a message when a key is pressed and display the key value on the screen.",
"output": """[OnKeyPress]
[Log]
[Show]"""
},
{
"input": "Reduce a list of scores to find the highest score and log the result.",
"output": """[Reduce]
[Log]"""
},
{
"input": "Cache fetched data to improve performance and display the data on the screen.",
"output": """[FetchData]
[CacheData]
[Show]"""
},
{

"input": "Highlight an element when the mouse enters it and remove the highlight when the mouse leaves.",
"output": """[OnMouseEnter]
[Highlight]
[OnMouseLeave]
[Show]"""
},
{
"input": "Filter out items that are out of stock and sort the remaining items by price before displaying them on the screen.",
"output": """[Filter]
[Sort]
[Show]"""
}
]
example_tuples = [(example["input"], example["output"]) for example in examples]




