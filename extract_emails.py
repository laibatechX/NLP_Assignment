# extract_emails.py
import re

def extract_emails(text):
    """
    Extract email addresses from a text string using regex.
    Returns a list of unique emails in the order found.
    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    found = re.findall(pattern, text)
    # Optionally remove duplicates while preserving order
    seen = set()
    unique = []
    for e in found:
        if e not in seen:
            seen.add(e)
            unique.append(e)
    return unique

if __name__ == "__main__":
    sample_text = """
    In this exercise, I used Python’s Regular Expressions (Regex) to extract email addresses from text. The sample paragraph contained several emails such as info@university.edu, contact@datasciencehub.org, and laiba.azhar01@gmail.com. Using the re module and a suitable pattern, the code successfully identified and printed all valid emails from the text. This method is very helpful in automating email collection from large text files or websites.
    """
    emails = extract_emails(sample_text)
    print("Extracted emails:", emails)
