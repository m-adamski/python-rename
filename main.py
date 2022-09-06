import click
import csv as csv_lib
import os
import tabulate


@click.group()
def cli():
    pass


@cli.command()
@click.argument("source", type=click.Path(exists=True, file_okay=False))
@click.option("--csv", type=click.Path(dir_okay=False, writable=True))
def summary(source, csv):
    items = os.listdir(source)

    # Define table variables
    table_headers = ["relative_path", "filename", "basename", "extension"]
    table_data = []

    for item in items:
        item_path = os.path.join(source, item)

        # Accept only files, exclude directories
        if os.path.isfile(item_path):
            table_data.append(
                [item_path, item, os.path.splitext(item)[0], os.path.splitext(item)[1]]
            )

    # Save summary into CSV file or just print it as table in console
    if csv is not None:
        with open(csv, "w", encoding="UTF8") as csv_file:
            csv_writer = csv_lib.writer(csv_file)
            csv_writer.writerow(table_headers)
            csv_writer.writerows(table_data)
    else:
        print(tabulate.tabulate(table_data, headers=table_headers, tablefmt="simple"))


@cli.command()
@click.argument("source", type=click.Path(exists=True, file_okay=False))
@click.option("--csv", type=click.Path(dir_okay=False), required=True)
@click.option("--columns", nargs=2, type=click.Tuple([str, str]), required=True)
def rename(source, csv, columns):
    table_headers = []
    table_data = []

    # Open CSV file and read rows
    with open(csv, "r", encoding="UTF8") as csv_file:
        csv_reader = csv_lib.reader(csv_file)

        for row in csv_reader:
            if csv_reader.line_num == 1:
                table_headers = row
            else:
                table_data.append(row)

    if columns[0] in table_headers and columns[1] in table_headers:
        filename_index = table_headers.index(columns[0])
        rename_index = table_headers.index(columns[1])

        # Generate list with current & new filename
        rename_items = []
        for table_item in table_data:
            rename_items.append([table_item[filename_index], table_item[rename_index]])

        # Display table with changes
        print(tabulate.tabulate(rename_items, headers=["Current", "After"], tablefmt="simple"))
        print("")

        if click.confirm("Are you sure you want to apply changes?", abort=True):
            for rename_item in rename_items:
                rename_item_source = os.path.join(source, rename_item[0])
                rename_item_destination = os.path.join(source, rename_item[1])

                if os.path.isfile(rename_item_source):
                    if not os.path.exists(rename_item_destination):
                        os.rename(rename_item_source, rename_item_destination)
                        print(rename_item_source, rename_item_destination, "OK")
                    else:
                        print(rename_item_source, rename_item_destination, "Destination file exist")


if __name__ == "__main__":
    cli()
