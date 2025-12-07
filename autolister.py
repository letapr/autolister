from openai import OpenAI
import base64

openai_client = OpenAI()


def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_title_description(image_b64):
    response = openai_client.responses.create(
        model="gpt-4o", # gpt-4o-mini, gpt-4.1
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "I want to create an ebay listing for this object. please provide a title and description, clearly marked with 'title: ' and 'description: '."},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_b64}"
                    }
                ]
            }
        ]
    )
    return response.output_text


if __name__ == "__main__":
    filename="moto.jpg"
    image_b64 = load_image_base64(filename)
    response=generate_title_description(image_b64)
    print(response)
