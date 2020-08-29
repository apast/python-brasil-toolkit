import csv
import sys

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-c", "--columns", type=click.File("r"), help="File with columns to keep")
@click.option("csvout", "--out", default=sys.stdout, type=click.File("w"), help="Save output to file")
@click.argument("file", type=click.File("r"))
def csvfilter(file, csvout, columns):
    columns_to_keep = [c.strip() for c in columns.readlines()]

    reader = csv.DictReader(file)
    writer = csv.DictWriter(csvout, fieldnames=columns_to_keep)
    writer.writeheader()

    for row in reader:
        writer.writerow({column: row[column] for column in columns_to_keep})


if __name__ == "__main__":
    cli()
