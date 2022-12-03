from file_reader.reader import InputReader
import importlib
import click

@click.command()
@click.option('--day', prompt="Day to run", help="Which advent day to run", type=click.INT)
@click.option('--part', prompt="Part of day to run", help="A or B", type=click.Choice(['a', 'b']))
def runner(day, part):
    try:
        module = importlib.import_module(f"days.day{day}")
        data = InputReader.read_day_input(f"day{day}")
        print(f"Results: {module.run(part, data.data)}")
    except ModuleNotFoundError as exc:
        raise exc


if __name__ == '__main__':
    runner()
