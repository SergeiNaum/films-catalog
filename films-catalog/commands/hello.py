from typing import Annotated

import typer
from rich import print


app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.command(help="Greet user by name")
def hello(name: Annotated[str, typer.Argument(help="Name to greet")]):
    colored_hello = (
        "[red]H[/red]"
        "[yellow]e[/yellow]"
        "[green]l[/green]"
        "[blue]l[/blue]"
        "[purple]o[/purple]"
    )
    colored_exclamation = "[bold][red]![/red][yellow]![/yellow][green]![/green][/bold]"
    print(f"{colored_hello} [bold green]{name}[/bold green] {colored_exclamation}")
