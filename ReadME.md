# Large Language Models Query
This repository contains a basic Python Project that I made for a University Term Project.
It sends queries to locally downloaded Large Language Models that are operating on your computer.
These are focussed on Llama-7B, Llama-13B and Falcon-7B

This was my first foray into learning about Large Language Models.

The results (the response times and memory/energy usage) is actually quite interesting: on my Macbook Pro M2, if i query the Llama-7B via the python project,
it will take a long time to produce a response. However, if i access the LLM directly from the Terminal and call the scripts (that are available in the Llama helper code)
in the Terminal itself to place queries, it is instantaneous. Meaning, as soon as you hit enter on your query, it begins producing a response.

So you can essentially have a "Chat-GPT"-esque Language Model running locally on your computer for your own needs, though of course, it would not be getting updated in real-time
- that is unless you train the model parameters that are now downloaded in your computer.

Modifying some of the parameters in the JSON files that come with Llama allow you to vary the amount of tokens used in the response and how random it should be
(i.e. the length of response and how widely ranging the output should be based on your question - in short, the accuracy of the response).

The queries that are were used were a collection of standardized test-questions for LLMs that are available on huggingface to check benchmarking.

# How To Run

Download the project on to your computer. Open the file in your IDE of choice.

Ensure that all files have been downloaded and are present in the project folder when you have opened the project in the IDE of your choice.

You would need to download the language models Llama-7B and Llama-13B which you can access from Meta's website here: https://www.llama.com/llama-downloads/
Once downloaded and setup, you will find the llama scripts and queries in a helper file.
It can be a little tricky when you are operating on Macbook silicon chips (M2 Pro in my case) as you will need to fiddle around with a lot of the queries
and find work arounds for several compiler errors as they are originally native to frameworks that are typically available to windows computers.

In the case of Falcon-7B, I implemented code that was developed by renting cloud GPUs such as Google Cloud. Therefore, there is less local file calling.

Each Python file is to be run individually in order to query its respective Language Model.

Upon running, there should not be any errors.

Findings have been compiled in the Excel file that is part of this project and will be accessible once it has been downloaded.
Note that the findings are based on my own computer: Macbook Pro M2.

The project runs entirely in the Terminal of your computer or in the console of your IDE as text at the moment, however there is one GUI file that allows you to choose between Llama-7B and Llama-13B.

# Code Complexity

I intend to keep the complexity low but effective, and yet demonstrate some prowess. Possibly use some unique code implementations/tools.

This is currently a very basic project that does not utilize data structures because it was my first LLM project that was developed during my intense Master's Program, before i learned data structures. I may also include a complete GUI for this program in future.

# Code Maintainability, Readability and Reusability

Code should be loosely coupled. Should be able to demonstrate the addition of code/variables, reuse older code (such as reader),
The code should be well segmented, naming conventions. Minimize smells.

In future, I plan to download and experiment with different Language Models and update the Excel file.

