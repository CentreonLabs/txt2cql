from typing import Annotated
import pyperclip
import typer
from openai import OpenAI
from rich import print
import os

app = typer.Typer()
client = OpenAI()

# Get the absolute path of the root directory of the project
instruction_path = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")),
    "instructions.txt",
)


@app.command()
def txt2cql(
    input_text: Annotated[list[str], typer.Argument(help="The text to convert to CQL")]
):
    cql = convert_to_cql(input_text)
    copy_to_clipboard(cql)
    print("\n[italic white]CQL copied to clipboard![/italic white]")


def convert_to_cql(input_text: str) -> str:
    with open(instruction_path, "r") as file:
        instruction = file.read()
    cql = ""
    print()
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": " ".join(input_text)},
        ],
        stream=True,
    )
    for chunk in stream:
        chunk_content = chunk.choices[0].delta.content or ""
        cql += chunk_content
        print("[bold]" + chunk_content + "[/bold]", end="")
    typer.echo()
    return cql


def copy_to_clipboard(text: str):
    pyperclip.copy(text)


if __name__ == "__main__":
    app()
