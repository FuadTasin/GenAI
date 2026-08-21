student_answer = """
   Python is a high-level programming language.
   It is widely used in web development, data science,
   and artificial intelligence.
"""

def clean_answer(answer):
    return answer.strip()

cleaned_ans=clean_answer(student_answer)

def count_words(answer):
    return len(answer.split())

word_count=count_words(cleaned_ans)

def generate_feedback(answer,word_count): 
    return f"""
    The answer contains {word_count} words.
    The student correctly explained python and mentioned some important applicatin areas.

    """

feedback = generate_feedback(cleaned_ans,word_count)

def format_feedback(feedback): 
    return feedback.strip().upper()


