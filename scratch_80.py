import time


# Simple chat responses
def chat():
    user_input = input("You: ").lower()
    if user_input == "hello":
        print("Bot: Hello! 👋")
    elif user_input == "how are you":
        print("Bot: I'm good! How about you?")
    elif user_input == "bye":
        print("Bot: Goodbye! 👋")
    else:
        print("Bot: I don't understand that.")


# Poll system that runs until user chooses to end
def poll():
    question = input("Poll question: ")
    option1 = input("First option: ")
    option2 = input("Second option: ")
    votes = {option1: 0, option2: 0}

    while True:
        print(f"\nVote: 1 for {option1}, 2 for {option2}, or type 'end' to finish voting.")
        vote = input("Enter your choice: ")

        if vote == "1":
            votes[option1] += 1
        elif vote == "2":
            votes[option2] += 1
        elif vote.lower() == "end":
            break
        else:
            print("Invalid choice, try again.")

    print("\nFinal Poll Results:")
    print(f"{option1}: {votes[option1]} votes")
    print(f"{option2}: {votes[option2]} votes")


# Reminder system
def reminder():
    message = input("Reminder message: ")
    seconds = int(input("Set time in seconds: "))
    print(f"Reminder set! It will remind you in {seconds} seconds.")
    time.sleep(seconds)
    print(f"\nReminder: {message}")


# Simple music queue
music_queue = []


def add_song():
    song = input("Enter song name: ")
    music_queue.append(song)
    print(f"Added {song} to the queue.")


def play_song():
    if music_queue:
        print(f"Playing: {music_queue.pop(0)}")
    else:
        print("No songs in the queue.")


# Main menu
while True:
    print("\nOptions: [1] Chat [2] Poll [3] Reminder [4] Add Song [5] Play Song [6] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        chat()
    elif choice == "2":
        poll()
    elif choice == "3":
        reminder()
    elif choice == "4":
        add_song()
    elif choice == "5":
        play_song()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
