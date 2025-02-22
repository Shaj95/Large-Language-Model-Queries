"""

This python program has been created to send queries to a locally downloaded Large Language Model (LLM)
The queries are tokenized into bits that are processed by the model weights and then decoded back into human-readable language.

"""

#to create the GUI
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#importing the llama cpp library/packages and llama class
import llama_cpp

#import for timing the responses
import time

#import to measure CPU usage
import psutil

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


app = tk.Tk()
app.title("Large Language Models")


label = tk.Label(app, text="Please Choose a Language Model")


def open_model_window(model_name):
    # Destroy the current window
    app.destroy()

    
    model_window = tk.Tk()
    model_window.title(model_name)

    # Function to handle the "Start" button click
    def start_button_click():
        
        if model_name == "Llama2-7B":
            get_llamaseven_response(queries)
        elif model_name == "Llama2-13B":
            get_llamathirteen_response(queries)

    # Function to handle the "View Results" button click
    def view_results_button_click():
        # Create a new window for displaying results
        results_window = tk.Tk()
        results_window.title("Results")

        # Assuming you have image files in a specific path
        image_path = "/Users/SaudRAlvi/Desktop/TermProjectData.png"
        
        # Display images from the specified path
        display_images(results_window, image_path)

    # Function to handle the "Model Options" button click
    def model_options_button_click():
        # Close the current window and go back to the main screen
        model_window.destroy()
        create_main_screen()

    # Create buttons in the Model window
    start_button = tk.Button(model_window, text="Start", command=start_button_click)
    view_results_button = tk.Button(model_window, text="View Results", command=view_results_button_click)
    model_options_button = tk.Button(model_window, text="Model Options", command=model_options_button_click)

    # Pack the buttons to display them in the model window
    start_button.pack(pady=5)
    view_results_button.pack(pady=5)
    model_options_button.pack(pady=5)

# Create "Llama2-7B" button with the command to open the Apples window
llamaseven_button = tk.Button(app, text="Llama2-7B", command=lambda: open_model_window("Llama2-7B"))

# Create "Llama2-13B" button with the command to open the Oranges window
llamathirteen_button = tk.Button(app, text="Llama2-13B", command=lambda: open_model_window("Llama2-13B"))

# Pack the label and buttons to display them in the window
label.pack(pady=10)
llamaseven_button.pack(pady=5)
llamathirteen_button.pack(pady=5)

# Function to execute processing for Llama2-7B
def get_llamaseven_response(queries):

    #setting the path to the quantized llama model
    model = llama_cpp.Llama(model_path="/Users/SaudRAlvi/llama-modified/llama.cpp-master/models/7B/Quantized/ggml-model-q4_0.bin", chat_format="llama-2")

    
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
        #cpu_usage_during_task = cpu_after - cpu_before

        #orint time taken to produce query
        print(f"Time Taken to process query: {elapsed_time} seconds\n")
        #print(f"CPU Usage during task: {cpu_usage_during_task}%\n")

# Function to execute processing for Llama2-13B
def get_llamathirteen_response(queries):

    #setting the path to the quantized llama model
    model = llama_cpp.Llama(model_path="/Users/SaudRAlvi/llama-modified/llama.cpp-master/models/13B/Quantized/ggml-model-q4_0.bin", chat_format="llama-2")


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
      #  cpu_usage_during_task = cpu_after - cpu_before

        #orint time taken to produce query
        print(f"Time Taken to process query: {elapsed_time} seconds\n")
        #print(f"CPU Usage during task: {cpu_usage_during_task}%\n")

# Function to display images from a specified path
def display_images(window, path):

        # Open the image file using Pillow
        image = Image.open("/Users/SaudRAlvi/Desktop/TermProjectData.png")

        # Convert the Pillow image to a Tkinter PhotoImage
        img = ImageTk.PhotoImage(image)

        # Create a label to display the image
        label = tk.Label(window, image=img)
        label.image = img  # Keep a reference to the image to prevent garbage collection
        label.pack()

# Function to recreate the main screen
def create_main_screen():
    global app
    app = tk.Tk()
    app.title("Large Language Models")  # Set the title of the window to "Fruits"

    # Add widgets (Fruits label, Apples button, Oranges button)
    label = tk.Label(app, text="Please Choose a Language Model")

    # Create "Apples" button with the command to open the Apples window
    apples_button = tk.Button(app, text="Llama2-7B", command=lambda: open_model_window("Llama2-7B"))

    # Create "Oranges" button with the command to open the Oranges window
    oranges_button = tk.Button(app, text="Llama2-13B", command=lambda: open_model_window("Llama2-13B"))

    # Pack the label and buttons to display them in the window
    label.pack(pady=10)
    apples_button.pack(pady=5)
    oranges_button.pack(pady=5)

    # Run the main event loop
    app.mainloop()

# Step 3: Run the main event loop
app.mainloop()
