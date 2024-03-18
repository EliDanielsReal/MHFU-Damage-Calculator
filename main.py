import typer
from typing import Optional
from typing_extensions import Annotated
from calculate import calculate_raw
from rich import print
from styling import element_display, raw_display

app = typer.Typer()



@app.command("raw")
def raw(weapon_class: str, raw_attack: int, raw_element: int, element_type: str, sharpness: Annotated[Optional[str], typer.Argument()] = "GREEN"):

    true_raw, true_element = calculate_raw(weapon_class, raw_attack, raw_element, sharpness)

    display = raw_display(sharpness, true_raw) + element_display(element_type, true_element)

    print(display)

if __name__ == "__main__":

    app()