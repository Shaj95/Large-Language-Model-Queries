"""

This python program has been created to send queries to a locally downloaded Large Language Model (LLM)
The queries are tokenized into bits that are processed by the model weights and then decoded back into human-readable language.

In this case the LLM is Llama-2-13B

"""


#importing the llama cpp library/packages and llama class
import llama_cpp

#import for timing the responses
import time

#import to measure CPU usage
import psutil

#setting the path to the quantized llama model
model = llama_cpp.Llama(model_path="/Users/SaudRAlvi/llama-modified/llama.cpp-master/models/13B/Quantized/ggml-model-q4_0.bin", chat_format="llama-2")

#the following queries were selected from MMLU and HellaSwag examples and the coding query is my own original query.

#here begins a list containing the queries

queries = [
    
    #Q1 - MMLU
    
            "What is true for a type-1a supernova?\na. This type occurs in binary systems\nb. This type occurs in young galaxies\nc. This type produces gamma-ray bursts\nd. This type produces high amounts of X-rays",

    #Q2 - MMLU
            
           "Nagel claims that most skeptical arguments:\na. Are the result of applying arbitrarily stringent standards.\nb. Are based on linguistic confusions.\nc. Are logically self-refuting\nd. Grow from the consistent application of ordinary standards.\nwhich of the four options is correct?",

    #Q3 - HellaSwag BaRDa dataset
            
           "Here are two premises and an entailment:\npremise: A pine tree is a kind of tree.\npremise: A tree is a kind of plant.\nentailment: A pine tree is a kind of plant.\nIs the entailment true?",

    #Q4 - HellaSwag BaRDa dataset
            
           "Here are two premises and an entailment:\npremise: The speed of an object can be measured using a meter stick and a stopwatch.\npremise: A turtle is a kind of object.\nentailment: The speed of a turtle can be measured using a meter stick and a stopwatch.\nIs the entailment true?",

    #Q5 - HellaSwag BaRDa dataset
            
           "Here are two premises and an entailment:\npremise: A plant requires nutrients in soil to grow.\npremise: Crops are a kind of edible plant for eating.\nentailment: Crops require nutrients in soil to grow.\nIs this true?",

    #Q6 - MMLU
            
           "The sum of three consecutive even numbers is 162. What is the smallest of the three numbers?\nThe answer is either 11 or 52.0. Which is the correct answer?",

    #Q7 - MMLU
            
           "A restaurant served 5 cakes during lunch and 6 during dinner today. The restaurant served 3 cakes yesterday.\nHow many cakes were served in total? The answer is either 31 or 14.0. Which is the correct answer?",

    #Q8 - MMLU
            
           "There are 7 dogwood trees currently in the park. Park workers will plant 3 more dogwood trees today and 2 more dogwood trees tomorrow.\nHow many dogwood trees will the park have when the workers are finished? The answer is either 33 or 12.0. Which is the correct answer?",

    #Q9 - MMLU
            
           "There are 33 walnut trees currently in the park. Park workers will plant 44 more walnut trees today.\nHow many walnut trees will the park have when the workers are finished? The answer is either 39 or 77.0. Which is the correct answer?",

    #Q10 - my own coding query
            
           "Write a python program that produces a list of 10 random integers between 1 and 10 and then converts that list into a set and then prints the set."

           ]

# Function to measure CPU usage

def measure_cpu_usage():
    
    return psutil.cpu_percent(interval=1)





for query in queries:

    #print the current query
    print("User:", query,"\n")

    #measure CPU usage before processing query
    cpu_before = measure_cpu_usage()
    print(f"CPU Usage before task: {cpu_before}%\n")
        
    #start the timer just before processing query
    start_time = time.time()

    #process the query and measure CPU immediately after
    response = model.create_chat_completion(messages=[{"role": "user", "content": query}])
    print("Llama:", response["choices"][0]["message"]["content"],"\n") #print response from model
    cpu_after = measure_cpu_usage()
    print(f"CPU Usage after task: {cpu_after}%\n")

    #calculate elapsed time as an integer and calculate CPU during task
    elapsed_time = int(time.time() - start_time)
      # cpu_usage_during_task = cpu_after - cpu_before

    #orint time taken to produce query
    print(f"Time Taken to process query: {elapsed_time} seconds\n")
    #print(f"CPU Usage during task: {cpu_usage_during_task}%\n")
