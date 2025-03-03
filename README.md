# Research Agent

Small research agent based on the deep reasearch agent from [Smolagents](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research).

## Installation

This project requires [uv](https://github.com/astral-sh/uv) to be installed.

```bash
uv sync
.venv\Scripts\activate
```

## Configuration

Check the environment variables in [env local](./.env%20local)

You will need at least an OpenAI API key (Go to https://platform.openai.com/api-keys) and a Serp API (Go to https://serpapi.com/dashboard) key as well as a Hugging Face token which you can get from https://huggingface.co/settings/tokens

The Gemini API key is optional.

We have tested this agent with o1 and it works relatively well with it.

## Running the GradIO Server

You can run the server using 

```bash
uv run .\app.py
```