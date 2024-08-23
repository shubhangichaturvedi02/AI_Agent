import logging
from app.pdf_processor import PDFProcessor
from app.qa_agent import QAAgent

from app.slack_notifier import post_message

logging.basicConfig(level=logging.INFO)

def main(pdf_path: str, questions: list):
    logger = logging.getLogger(__name__)
    pdf_processor = PDFProcessor(pdf_path)
    qa_agent = QAAgent()


    # Extract text from the PDF
    text = pdf_processor.extract_text()
    logger.info(f"Extracted text from PDF: {pdf_path}")

    # Extract answers for each question
    for question in questions:
        answer = qa_agent.extract_answer(text, question)
        message = f"Q: {question}\nA: {answer}"
        logger.info(f"Posting message to Slack: {message}")
        post_message(message)

if __name__ == "__main__":
    pdf_path = "/Users/shubhangichaturvedi/Downloads/Title_ Sample Document.pdf"
    questions = [
        "What is the main theme of the document?",
        "List the key findings mentioned in the document.",
        # Add more questions as needed
    ]
    main(pdf_path, questions)
