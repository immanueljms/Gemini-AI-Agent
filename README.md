# Gemini AI Agent

A Python-based AI agent powered by Google Gemini with tool-calling capabilities — built to autonomously read, write, and execute files in a sandboxed environment.

## Features

- Function-calling loop via Gemini API
- File system tools: read file content, list file info, write files, run Python scripts
- Modular function registry (add tools easily in `/functions`)
- Configurable prompts and model settings

## Project Structure
├── calculator/          # Sample task for the agent
├── functions/           # Tool definitions callable by the agent
├── main.py              # Agent loop entry point
├── call_function.py     # Dispatches Gemini tool calls to Python functions
├── config.py            # API keys, model config
├── prompts.py           # System prompt definitions
└── test_*.py            # Integration tests for each tool

## Setup

```bash
uv sync
```

Set your Gemini API key in `config.py` or as an environment variable.

## Usage

```bash
python main.py
```

The agent will accept a task, reason over it, and call tools iteratively until done.

## Tools Available

| Tool | Description |
|------|-------------|
| `get_file_content` | Read a file's contents |
| `get_files_info` | List files and metadata |
| `write_file` | Write or overwrite a file |
| `run_python_file` | Execute a Python script and return output |

## Stack

- Python 3.x, `uv` for package management
- Google Gemini API (function calling)
