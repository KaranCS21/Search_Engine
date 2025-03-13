from tkinter import *
import wikipedia

def get_data():
    # handle errors
    entry_value = entry.get().strip()
    answer.delete(1.0, END)  # Clear last output
    if not entry_value:
        answer.insert(INSERT, "ERROR! Please enter a search term.")
        return
    try:
        # Fetch data
        answer_value = wikipedia.summary(entry_value, sentences=5)  
        answer.insert(INSERT, answer_value)
    except wikipedia.exceptions.DisambiguationError:
        answer.insert(INSERT, "ERROR! The query is ambiguous. Please refine your search.")
    except wikipedia.exceptions.PageError:
        answer.insert(INSERT, "ERROR! Page not found. Try another search.")
    except Exception as e:
        answer.insert(INSERT, f"ERROR! {str(e)}")


win = Tk()
win.title("Wikipedia Search Engine")

# Top frame
topframe = Frame(win)
entry = Entry(topframe, width=50)  
entry.pack()
button = Button(topframe, text="Search", command=get_data)
button.pack()
topframe.pack(side=TOP, pady=10)

# Bottom 
bottomframe = Frame(win)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(bottomframe, width=60, height=20, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()


# welcome message
answer.insert(INSERT, "Welcome to the Wikipedia Search Engine!\nDeveloped by Karan🧑‍💻\n\n")

# footer 
footer = Label(win, text="Knowledge Begins with a Single Search.", font=("Calibri", 10), fg="black")
footer.pack(side=BOTTOM, pady=5)

# Run 
win.mainloop()

