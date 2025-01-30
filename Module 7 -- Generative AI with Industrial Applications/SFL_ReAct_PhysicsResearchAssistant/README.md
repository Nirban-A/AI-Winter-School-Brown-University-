# About

## Setup

### Environment & Dependencies

The exercsies and exmaples we will be running today will require a `Python 3.12.0` based environment along with specific dependencies.
1. Install [miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) (if not already installed)
2. In a terminal, navigate to `SFL_ReAct_PhysicsResearchAssistant/` and install the environment with `conda env create -f environment.yaml`
3. Activate the environment with `conda activate demo_env`
    - As a reminder, this will separate the required build from your machine's main build to maintain consistency of dependncies required from other Python scripts
4. Install the packages with `pip install -r requirements.txt`

<br>
<br>

### LLM Setup

1) Download a setup and run a local LLM with an Ollama instance by following the instructions on the README here: `https://github.com/ollama/ollama`
2) Open your terminal, type `ollama run llama3.1`
2) Create a free Tavily account here `https://tavily.com/` and get an API key.
3) Create a file `.env` in the main directory of this repo, and add a line of text `TAVILY_API_KEY="<YOUR API KEY>"`. * This file should not be added to any version control or remote places. It stays on your local machine and no one sees it. 
    - Populate the `TAVILY_API_KEY` with your specific API key

Your .env file should look like the following:
```
TAVILY_API_KEY="<YOUR TAVILY API KEY>"
OPENAI_API_KEY="<YOUR OPENAI API KEY (OR AN EMPTY STRING)>"
```



