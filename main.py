from dataclasses import dataclass
import datetime
import os
from numbers import Number
from typing import NamedTuple
from typing_extensions import Annotated
import typer

app = typer.Typer()


@dataclass
class RecipeIngredient:
    name: str
    quantity: tuple
    unit: str
    preparation: str = ""

    def __str__(self):
        return f"{self.quantity} {self.unit + ' ' + self.name if self.unit else self.name}, {self.preparation}"

@dataclass
class Recipe:
    name: str
    created: datetime.datetime
    ingredients: list[RecipeIngredient]


###
### Helper Functions
###

def yes_no_prompt(prompt: str):
    response = input(f"{prompt} [yes]/no ")
    if not response or response.lower() == "yes":
        return True
    elif response.lower() == "no":
        return False
    else:
        print("Invalid response. Try again.")
        return yes_no_prompt(prompt)

###
### App Functions
###

def _add_ingredient():
    name = input("Ingredient name: ")
    quantity = input("Quantity: ")
    unit = input("Unit: ")
    preparation = input("Preparation: ")
    return RecipeIngredient(name, quantity, unit, preparation)


def add_ingredients():
    ingredients = []
    print("Let's add ingredients...")
    ingredients.append(_add_ingredient())
    while True:
        os.system('clear')
        for ingredient in ingredients:
            print(f"- {ingredient}")
        print()
        ingredients.append(_add_ingredient())
        # Exit loop and return ingredients
        if input("Add another ingredient? [Yes]/No ").lower() == "no":
            return ingredients


def add_steps():
    steps = []
    n = 0
    while True:
        for step in steps:
            print(step)
        step = input(f"{n}. ")
        if not step:
            return steps
        else:
            steps.append(step)
            n += 1
            os.system('clear')


@app.command()
def create_recipe(
    name: Annotated[str, typer.Option(prompt=True)],
    ):
    print(f"Creating {name} recipe.")
    ingredients = add_ingredients()
    steps = add_steps()
    recipe = Recipe(name, datetime.datetime.now(), ingredients, steps)


@app.command()
def view_recipe(
    name: Annotated[str, typer.Option(prompt=True)],
):
    print(f"Viewing {name}")


if __name__ == "__main__":
    app()