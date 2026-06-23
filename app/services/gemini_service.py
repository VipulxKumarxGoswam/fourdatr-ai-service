from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


# =====================================
# Generate AI Text
# =====================================

def generate_text(prompt: str):

    system_prompt = """
You are an expert social media content writer.

Rules:
1. Generate a single high-quality social media post.
2. Return ONLY the final post.
3. Do NOT explain your reasoning.
4. Do NOT use markdown.
5. Do NOT use headings like "Option 1" or "Here's your post".
6. Make the post engaging and ready to publish.
7. Use emojis naturally when appropriate.
8. Add relevant hashtags at the end.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=system_prompt + "\n\n" + prompt
        )

        if response.text:
            return response.text.strip()

        return "AI Generation Failed: Empty response from Gemini."

    except Exception as e:

        print("Gemini Error:", e)

        return "AI Generation Failed: " + str(e)


# =====================================
# Rewrite Existing Text
# =====================================

def rewrite_text(text: str, action: str):

    system_prompt = """
You are an expert social media copywriter.

Rewrite the content according to the requested action.

Rules:
1. Return ONLY the rewritten post.
2. Never explain your changes.
3. Never give multiple versions.
4. Never use headings.
5. Never use markdown.
6. Preserve the original meaning.
7. Keep the output ready for publishing.
8. Keep emojis and hashtags where appropriate.
"""

    prompts = {

        "improve":
            "Improve the following social media post while keeping the same meaning. Make it more engaging.\n\n",

        "shorten":
            "Rewrite the following social media post in a shorter version without losing important information.\n\n",

        "expand":
            "Expand the following social media post by adding useful details while keeping it engaging.\n\n",

        "professional":
            "Rewrite the following social media post in a professional LinkedIn style.\n\n",

        "casual":
            "Rewrite the following social media post in a casual, friendly and conversational style.\n\n"

    }

    instruction = prompts.get(
        action.lower(),
        "Rewrite the following text.\n\n"
    )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=system_prompt + "\n\n" + instruction + text
        )

        if response.text:
            return response.text.strip()

        return "AI Rewrite Failed: Empty response from Gemini."

    except Exception as e:

        print("Gemini Error:", e)

        return "AI Rewrite Failed: " + str(e)