import tkinter as tk
from tkinter import messagebox
import re
import random
from datetime import datetime

last_topic = None

def get_random_response(options):
    """Helper to pick a random response from a list."""
    return random.choice(options)

def chatbot_response(user_input):
    global last_topic
    user_input = user_input.lower().strip()
    
    if re.search(r'\b(hello|hi|hey|greetings|sup|yo|howdy)\b', user_input):
        responses = [
            "Hey there! 😊 What's up?",
            "Hi! Great to see you. How's your day going?",
            "Hello! Ready to chat? What's on your mind?"
        ]
        last_topic = "greeting"
        return get_random_response(responses)
    
    elif re.search(r'\b(how are you|how\'s it going|what\'s up|how r u)\b', user_input):
        if last_topic == "greeting":
            responses = [
                "I'm awesome, thanks! How about you? 😄",
                "Doing great! What's new with you?",
                "All good here—life's treating me well. How's yours?"
            ]
        else:
            responses = [
                "I'm doing well, thanks for asking! How are you holding up?",
                "Pretty chill! What's going on in your world?"
            ]
        last_topic = "wellbeing"
        return get_random_response(responses)

    elif re.search(r'\b(weather|forecast|rain|sunny|temp|temperature)\b', user_input):
        responses = [
            "I can't check it live, but hopefully it's nice where you are! ☀️",
            "Weather changes so fast! What's it like there today?"
        ]
        last_topic = "weather"
        return get_random_response(responses)

    elif re.search(r'\b(time|what time is it|clock|hour)\b', user_input):
        current_time = datetime.now().strftime("%I:%M %p")
        responses = [
            f"It's {current_time} right now. Time flies, huh? What are you up to?",
            f"Clock says {current_time}. Got any plans soon? ⏰"
        ]
        last_topic = "time"
        return get_random_response(responses)

    elif re.search(r'\b(bye|goodbye|see you|exit|later|cya)\b', user_input):
        responses = [
            "Aww, bye for now! Take care and chat soon! 👋",
            "See ya later! Have an amazing day! 😊",
            "Goodbye! It was fun talking—catch you next time!"
        ]
        last_topic = None
        return get_random_response(responses)

    elif re.search(r'\b(who are you|what are you|about you|your name)\b', user_input):
        responses = [
            "I'm your friendly neighborhood chatbot! Built with simple rules to keep things fun. 🤖 What's your name?",
            "Just a chill AI here to chat and help. Think of me as your digital pal! What's up with you?"
        ]
        last_topic = "about"
        return get_random_response(responses)

    elif re.search(r'\b(hobby|hobbies|interests|like to do|favorite|passion)\b', user_input):
        responses = [
            "Hobbies are the best! I 'enjoy' learning new things. What's yours? Maybe reading or gaming? 📚",
            "I'm all about chatting, but you? What's your go-to hobby? Let's swap ideas! 🎸"
        ]
        last_topic = "hobbies"
        return get_random_response(responses)

    elif re.search(r'\b(advice|help|how to|tips|recommend|suggest)\b', user_input):
        responses = [
            "Sure thing! I'm here to help. What's the scoop—what do you need advice on? 💡",
            "Advice is my middle name (well, kinda). Lay it on me—what's troubling you?"
        ]
        last_topic = "advice"
        return get_random_response(responses)

    elif re.search(r'\b(what do you think|opinion|believe|feel about|thoughts on)\b', user_input):
        responses = [
            "As a bot, I don't have strong opinions, but I'm curious—what's yours? 🤔",
            "That's a deep one! I think it depends, but I'd love to hear your take. What do you believe?"
        ]
        last_topic = "opinion"
        return get_random_response(responses)

    elif re.search(r'\b(thanks|thank you|nice|good job|awesome|cool)\b', user_input):
        responses = [
            "You're so welcome! 😊 Anything else I can do?",
            "Aww, thanks! Means a lot. What's next on your mind?"
        ]
        return get_random_response(responses)

    elif re.search(r'\b(joke|funny|laugh|tell me a joke|make me laugh)\b', user_input):
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts! 😂 Want another?",
            "What did the ocean say to the beach? Nothing, it just waved! 🌊 Your turn—got a joke?"
        ]
        last_topic = "joke"
        return get_random_response(jokes)

    elif re.search(r'\b(food|eat|drink|hungry|favorite food|snack)\b', user_input):
        responses = [
            "Food is life! I'm not hungry, but pizza sounds amazing. What's your fave? 🍕",
            "Ah, food—my favorite topic (besides chatting)! What's cooking in your world?"
        ]
        last_topic = "food"
        return get_random_response(responses)

    elif last_topic and re.search(r'\b(more|tell me|what about|and|yeah|okay)\b', user_input):
        followups = {
            "hobbies": "More on hobbies? Awesome! I 'love' hearing about them. What's another one? 🎉",
            "advice": "Got more on that advice? I'm all ears—break it down for me! 🤝",
            "weather": "Still chatting weather? Hope it's treating you well! Any fun plans outdoors?",
            "food": "Food again? Let's keep it going—what's your go-to snack? 🍿"
        }
        return followups.get(last_topic, "Go on, tell me more!")

    else:
        responses = [
            "Hmm, I'm not quite getting that. 😅 Try asking about the weather, a joke, or your hobbies?",
            "Oops, that one's over my head! Rephrase it or tell me more—I'm here to chat! 😉"
        ]
        return get_random_response(responses)

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return
    add_message(f"You: {user_input}", "user")
    entry.delete(0, tk.END)
    response = chatbot_response(user_input)
    add_message(f"Chatbot: {response}", "bot")
    
    if re.search(r'\b(bye|goodbye|see you|exit|later|cya)\b', user_input.lower()):
        messagebox.showinfo("Chatbot", "Thanks for chatting! Closing now.")
        root.destroy()

def add_message(text, sender):
    frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
    frame.pack(anchor="e" if sender == "user" else "w", pady=5, padx=10, fill="x")

    bg_color = "#007bff" if sender == "user" else "#28a745"
    fg_color = "white"
    label = tk.Label(frame, text=text, bg=bg_color, fg=fg_color,
                     font=("Arial", 10), wraplength=320,
                     padx=10, pady=5, relief="raised", borderwidth=2)
    label.pack(anchor="e" if sender == "user" else "w")

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

root = tk.Tk()
root.title("Chatbot")
root.geometry("460x520")
root.configure(bg="#f0f0f0")

canvas = tk.Canvas(root, bg="#f0f0f0", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

add_message("Chatbot: Hey! I'm your friendly chatbot. Type a message and hit Send or press Enter. Say 'bye' to exit.", "bot")

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(fill="x", pady=10)

entry = tk.Entry(input_frame, font=("Arial", 12), width=32)
entry.pack(side="left", padx=10, pady=5)
entry.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message,
                        bg="#28a745", fg="white", font=("Arial", 10, "bold"))
send_button.pack(side="right", padx=10)

root.mainloop()
