class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.memory = []

    def add_turn(self, user_input, bot_response):
        self.memory.append(f"User: {user_input}\nBot: {bot_response}")
        if len(self.memory) > self.max_turns:
            self.memory.pop(0)

    def get_context(self):
        return "\n".join(self.memory)
