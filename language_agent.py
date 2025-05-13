from langchain import LLM

class LanguageAgent:
    def __init__(self):
        self.llm = LLM()

    def generate_narrative(self, data):
        narrative = self.llm.generate(data)
        return narrative
