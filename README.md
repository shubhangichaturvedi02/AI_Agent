
## Requirements

- Python 3.7 or later
- `openai` library
- `PyMuPDF` library
- `slack-sdk` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shubhangichaturvedi02/AI_Agent.git
    cd AI_Agent
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for OpenAI and Slack:

    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    export SLACK_BOT_TOKEN='your_slack_bot_token'
    ```

## Usage

1. **Configuration**: Update `app/config.py` with your configuration settings, such as the Slack channel and other parameters.

2. **Run the Agent**:

    ```bash
    python main.py
    ```

   This script will extract text from the specified PDF, query the LLM with the provided questions, and post the results to Slack.


