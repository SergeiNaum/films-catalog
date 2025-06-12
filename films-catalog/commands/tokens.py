from typing import Annotated

import typer
from rich import print
from rich.markdown import Markdown

from api.v1.auth.services.redis_tokens_helper import redis_tokens

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.command(help="Checks that the token exists")
def check_token(
    token: Annotated[str, typer.Argument(help="Input token to check")],
) -> None:
    _not = "[red]n[/red][yellow]o[/yellow][green]t[/green]"
    _token = f"[bright_white]{token}[/bright_white]"
    if redis_tokens.token_exist(token):
        print(f"token: {_token} [bright_green]exists[/bright_green]")
    else:
        print(f"token: {_token} {_not} [bright_red]exist ![/bright_red]")


@app.command(help="Show all tokens in db")
def display_tokens() -> None:
    print(Markdown("# Avalable API Tokens"))
    print(Markdown("\n- ".join([""] + redis_tokens.show_all_tokens())))
    print()
