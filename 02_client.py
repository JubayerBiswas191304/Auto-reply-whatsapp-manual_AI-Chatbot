from openai import OpenAI

# ✅ Replace with your real API key
client = OpenAI(api_key="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")

# ✅ Chat message to analyze


# ✅ Initialize OpenAI client with your API key


# ✅ Chat message to analyze
command = """
[11:16, 7/15/2025] Abdullah: Dak dis
[11:16, 7/15/2025] Abdullah: Jab
[11:16, 7/15/2025] Abdullah: Tor sate
[09:40, 7/17/2025] Abdullah: Dak
[09:40, 7/17/2025] Abdullah: Dis
[09:40, 7/17/2025] Abdullah: Aksate jab
[09:41, 7/17/2025] Juβaye®~βiswas😎: ok
[09:41, 7/17/2025] Abdullah: Ok
[10:31, 7/18/2025] Abdullah: https://youtube.com/shorts/7T8ajSiw6XU?si=rjAeGr5eyMaIbmOn
[10:09, 7/19/2025] Juβaye®~βiswas😎: https://youtube.com/shorts/3GoOS727umQ?si=NoI7KnAZglQtAe0o
"""

# ✅ Send a chat completion request
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": f":\n{command}"}
    ]
)

# ✅ Print the result
print(response.choices[0].message.content)
