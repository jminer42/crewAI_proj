#!/usr/bin/env python
import sys
from prod_writer.crew import ProdWriterCrew

pm_pdfs = '/Users/j/Desktop/Reforge'

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'directory': pm_pdfs
    }
    ProdWriterCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        "directory": pm_pdfs
    }
    try:
        ProdWriterCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ProdWriterCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "directory": pm_pdfs
    }
    try:
        ProdWriterCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
