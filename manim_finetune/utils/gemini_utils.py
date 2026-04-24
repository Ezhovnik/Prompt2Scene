from google import genai
from google.genai.types import HttpOptions
import re

def get_gemini(api_key: str, timeout: int = 120000) -> genai.Client:
    return genai.Client(
        api_key=api_key,
        http_options=HttpOptions(timeout=timeout)
    )

def get_judge_prompt(prompt: str, code: str) -> str:
    return f"""You are an expert evaluator of Manim animations.
    Given a user request and the generated Python code using Manim, rate how well the code fulfills the request on a scale from 0 to 10.

    Consider:
    - Does the code produce the described animation?
    - Are the objects, colors, and motions correct?
    - Is the code concise and free of irrelevant elements?
    - Would the resulting animation match the user's expectation?

    User request:
    {prompt}

    Generated code:
    ```python
    {code}
    ```
    Output ONLY a number between 0 and 10 (can be decimal, e.g., 7.5). Do not include any other text.
    """

def evaluate_code_with_gemini(gemini_client: genai.Client, prompt: str, code: str, model_name: str) -> float:
    judge_prompt = get_judge_prompt(prompt, code)

    try:
        response = gemini_client.models.generate_content(
            model=model_name,
            contents=judge_prompt
        )
        answer = response.text.strip()

        match_ = re.search(r"(\d+(.\d+)?)", answer)
        if match_:
            score = float(match_.group(1))
            return min(10.0, max(0.0, score))
        else:
            print(f"Failed to parse the number from the response: {answer}")
            return 5.0
    except Exception as e:
        print(f"Error when calling Gemma: {e}")
        return 5.0
