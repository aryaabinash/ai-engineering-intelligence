
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def experiment_temperature(question):

    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions="You are a creative AI assistant.",
        input=question,
        max_output_tokens=200
    )

    print("\n========== AI RESPONSE ==========")
    print(response.output_text)

    print("\n========== TOKEN USAGE ==========")
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    print("Total tokens:", response.usage.total_tokens)


if __name__ == "__main__":

    question = "Suggest a creative name for an AI startup."

    experiment_temperature(question)
