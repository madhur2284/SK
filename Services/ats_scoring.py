async def generate_ats_score(kernel, resume_text):

    with open("prompts/ats_prompt.txt", "r") as f:
        prompt = f.read()

    result = await kernel.invoke_prompt(
        prompt,
        resume_text=resume_text
    )

    return str(result)