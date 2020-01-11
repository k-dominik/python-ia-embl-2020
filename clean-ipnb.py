"""
Script to clean notebook's in various ways

Use case:
 
 for `skimage`-based image analysis course we'd like to have pre-filled
 notebooks for teaching, but "empty" ones (no code, with exception of %loads)

 in particular,
 * remove all calls to `viewer.show()` (breaks flow, as blocking) for test runs
 * remove all code for publishing

"""
import json
import logging
import pathlib
import re
import shutil
from pprint import pprint
from typing import Dict

import click

logger = logging.getLogger("clean-ipnb")


@click.group()
@click.argument("notebook")
@click.option("--verbose", default=False, is_flag=True)
@click.pass_context
def cli(ctx, notebook, verbose):
    configure_logging(verbose)
    pth = pathlib.Path(notebook)
    assert pth.exists()
    if pth.is_dir():
        files = [pathlib.Path(x) for x in pth.glob("*.ipynb")]
    else:
        assert pth.suffix == ".ipynb"
        files = [pth]
    logger.debug(f"Working on {len(files)} notebooks.")
    ctx.obj = {
        "files": files,
    }


@cli.command()
@click.pass_obj
def restore(config):
    files = config["files"]
    backups = [gen_bkup_filename(x) for x in files]
    for backup, modified in zip(backups, files):
        shutil.copy(backup, modified)
        logger.debug(f"restored {modified} from {backup}")


@cli.command()
@click.pass_obj
def stripview(config):
    """Remove all calls to `viewer.show()`

    """
    files = config["files"]
    make_backup(files)
    mod_files(files, _strip_view)


@cli.command()
@click.pass_obj
def delcode(config):
    """Remove all code in cells, except %load magic"""
    files = config["files"]
    make_backup(files)
    mod_files(files, _delcode)


def _delcode(in_file):
    with open(in_file, "r") as f:
        content = json.load(f)

    cells = content["cells"]
    new_cells = []
    for cell in cells:
        new_cells.append(clean_cells(cell))

    content["cells"] = new_cells
    with open(in_file, "w") as f:
        json.dump(content, f, indent=1)
        f.write("\n")


def clean_cells(cell: Dict):
    if cell["cell_type"] != "code":
        return cell

    keepers = [re.compile("^\%load ")]

    new_lines = []
    for line in cell["source"]:
        if any(x.match(line) for x in keepers):
            new_lines.append(line)

    cell["source"] = new_lines
    cell["outputs"] = []
    return cell


def mod_files(files, func):
    for file in files:
        func(file)


def _strip_view(in_file):
    with open(in_file, "r") as f:
        content = json.load(f)

    cells = content["cells"]
    new_cells = []
    for cell in cells:
        new_cells.append(remove_cell_viewer(cell))

    content["cells"] = new_cells
    with open(in_file, "w") as f:
        json.dump(content, f, indent=1)
        f.write("\n")


def remove_cell_viewer(cell: Dict):
    if cell["cell_type"] != "code":
        return cell

    new_lines = []
    for line in cell["source"]:
        if "viewer.show()" in line:
            continue

        new_lines.append(line)

    cell["source"] = new_lines
    return cell


def configure_logging(verbosity):
    level = logging.INFO
    if verbosity:
        level = logging.DEBUG
    fmt = "%(levelname)s:%(message)s"
    logging.basicConfig(format=fmt, level=level)


def make_backup(in_files):
    for in_file in in_files:
        _make_backup(in_file)


def _make_backup(in_file):
    logger.debug(f"making a copy of {in_file}")
    out_file = gen_bkup_filename(in_file)
    shutil.copy(in_file, out_file)


def gen_bkup_filename(in_file):
    out_file = in_file.with_suffix(in_file.suffix + ".bak")
    return out_file


if __name__ == "__main__":
    cli()
