# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# class GroqLLM:
#     def __init__(self):
#         load_dotenv()

#     def get_llm(self):
#         try:
#             os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
#             llm=ChatGroq(api_key=self.groq_api_key,model="openai/gpt-oss-20b")
#             return llm
#         except Exception as e:
#             raise ValueError("Error occurred with exception:{e}")
        
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self):
        # Directly assign API key (⚠️ Not recommended for production)
        self.groq_api_key = ""

        print("✅ API Key Loaded:", self.groq_api_key[:8] + "********")

        # Define models (preferred + fallback)
        self.preferred_model = "llama-3.3-70b-versatile"
        self.fallback_model = "llama-3.1-8b-instant"

    def get_llm(self):
        """Return a ChatGroq LLM instance with fallback model support."""
        try:
            # Try preferred model
            llm = ChatGroq(
                api_key=self.groq_api_key,
                model=self.preferred_model
            )
            print(f"✅ Using preferred model: {self.preferred_model}")
            return llm

        except Exception as e:
            print(f"⚠️ Preferred model failed ({self.preferred_model}): {e}")
            print(f"👉 Trying fallback model: {self.fallback_model}")

            try:
                llm = ChatGroq(
                    api_key=self.groq_api_key,
                    model=self.fallback_model
                )
                print(f"✅ Using fallback model: {self.fallback_model}")
                return llm

            except Exception as e2:
                raise ValueError(
                    f"❌ Both preferred ({self.preferred_model}) and fallback "
                    f"({self.fallback_model}) models failed.\nError: {e2}"
                )

