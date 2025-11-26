# # modules/ai_chat.py

# from openai import OpenAI
# from modules.web_features import wiki_search

# import os

# # Load API key from environment (recommended)
# OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# # Initialize client only if key exists
# client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None


# def ai_chat(prompt: str, context=None):
#     """
#     Intelligent conversational model.
#     Uses GPT-4o-mini if online.
#     Falls back to Wikipedia + offline mode if API unavailable.
#     """

#     if not prompt:
#         return "Please say something, Jeet."

#     # Normalize prompt
#     cleaned_prompt = prompt.strip()

#     # ------------------------------------
#     # 🧠 STEP 1: GPT MODE (if available)
#     # ------------------------------------
#     if client:
#         try:
#             if context is None:
#                 context = []

#             context.append({"role": "user", "content": cleaned_prompt})

#             response = client.responses.create(
#                 model="gpt-4o-mini",     # super fast & smart
#                 input=context
#             )

#             answer = response.output_text.strip()

#             # Save assistant response
#             context.append({"role": "assistant", "content": answer})

#             return answer

#         except Exception as e:
#             print("[GPT ERROR]", e)
#             # continue to fallback


#     # ------------------------------------
#     # 🧠 STEP 2: WIKIPEDIA FALLBACK
#     # ------------------------------------
#     question = cleaned_prompt.lower()

#     # Detect knowledge-based questions
#     if any(q in question for q in ["what is", "who is", "define", "explain"]):
#         topic = (
#             question.replace("what is", "")
#             .replace("who is", "")
#             .replace("define", "")
#             .replace("explain", "")
#             .strip()
#         )
        
#         wiki_result = wiki_search(topic)
#         if wiki_result:
#             return wiki_result


#     # ------------------------------------
#     # 🧠 STEP 3: Simple offline chatbot
#     # ------------------------------------
#     offline_responses = [
#         "Sorry, I’m offline right now. Try again later.",
#         "I can’t reach the internet, but I'm still here to talk!",
#         "I'm having trouble connecting online—give me something simple!"
#     ]
#     return offline_responses[0]






















from openai import OpenAI
from modules.web_features import wiki_search
import os

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None

def ai_chat(prompt: str, context=None):
    if not prompt:
        return "Please say something."

    # GPT Mode
    if client:
        try:
            if context is None:
                context = []

            context.append({"role": "user", "content": prompt})

            response = client.responses.create(
                model="gpt-4o-mini",
                input=context
            )

            answer = response.output_text.strip()

            context.append({"role": "assistant", "content": answer})

            return answer

        except Exception as e:
            print("[GPT ERROR]", e)

    # Wikipedia fallback
    lower = prompt.lower()
    if any(q in lower for q in ["what is", "explain", "define"]):
        topic = (
            lower.replace("what is", "")
            .replace("explain", "")
            .replace("define", "")
            .strip()
        )
        return wiki_search(topic)

    return "I couldn't understand that, please try again."
