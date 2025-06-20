from model_loader import load_model
from chat_memory import ChatMemory

def main():
    print("🤖 Welcome to the CLI Chatbot! Type '/exit' to quit.\n")
    generator = load_model()
    memory = ChatMemory(max_turns=5)

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        context = memory.get_context() + f"\nUser: {user_input}\nBot:"
        response = generator(context, max_length=200, do_sample=True, top_k=50, top_p=0.95, temperature=0.7)[0]["generated_text"]
        
        # Extract only the new bot reply
        bot_reply = response.split("Bot:")[-1].strip().split("User:")[0].strip()
        print(f"Bot: {bot_reply}\n")

        memory.add_turn(user_input, bot_reply)

if __name__ == "__main__":
    main()
