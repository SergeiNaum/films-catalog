from typing import Annotated

import typer
from api.v1.auth.services.redis_tokens_helper import redis_tokens as tokens
from rich import print as rich_print
from rich.markdown import Markdown

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
    if tokens.token_exist(token):
        rich_print(f"token: {_token} [bright_green]exists[/bright_green]")
    else:
        rich_print(f"token: {_token} {_not} [bright_red]exist ![/bright_red]")


@app.command(help="Show all tokens in db")
def display_tokens() -> None:
    rich_print(Markdown("# Avalable API Tokens"))
    rich_print(Markdown("\n- ".join([""] + tokens.show_all_tokens())))
    rich_print()


@app.command(help="Generate new token and save in db")
def create_token() -> None:
    rich_print("Generating new token and saving into db")
    token = tokens.generate_and_save_token()
    rich_print(f"[bright_green]new_token:[/bright_green] {token}")


@app.command(help="Delete token in db")
def delete_token(
    token: Annotated[str, typer.Argument(help="Input token to check")],
) -> None:
    if not tokens.token_exist(token):
        print(f"Token: {token} [bright_red]not exists[/bright_red]")
        return
    print(f"Deleting this token: {token}")
    tokens.delete_token(token)


@app.command(help="Add token in db")
def add_token(
    token: Annotated[str, typer.Argument(help="Input token to check")],
) -> None:
    if not tokens.token_exist(token):
        tokens.add_token(token)
        print(f"[bright_white]Add token: {token}[/bright_white]")
    else:
        print("[bright_red]Token already exist[/bright_red]")
