"""Package entrypoint for Image Assembler."""
<<<<<<< HEAD
import json
import logging
import typing
from os import environ
from pathlib import Path

import typer

from .image_assembler import assemble_images
from .image_assembler import generate_output_filenames
=======
import logging
from os import environ
from pathlib import Path
import typing
import typer
import json

from .image_assembler import (
    assemble_image, generate_output_filenames
)
>>>>>>> de6ea1d (Update: update to new plugin standard:)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.plugins.transforms.images.image_assembler")
logger.setLevel(POLUS_LOG)
logging.getLogger("bfio").setLevel(POLUS_LOG)

POLUS_IMG_EXT = environ.get("POLUS_IMG_EXT", ".ome.tif")

app = typer.Typer(help="Image Assembler plugin.")

<<<<<<< HEAD

def generate_preview(
    img_path: Path,
    stitch_path: Path,
    out_dir: Path,
    timeslice_naming: bool,
) -> None:
    """Generate preview of the plugin outputs."""
    output_filenames = generate_output_filenames(
        img_path,
        stitch_path,
        out_dir,
        timeslice_naming,
    )

    preview: dict[str, typing.Union[list, str]] = {
=======
def generate_preview(img_path : Path,
                     out_dir : Path,
                     stitch_path : Path,
                     timeslice_naming : bool):
    """Generate preview of the plugin outputs."""
    output_filenames = generate_output_filenames(img_path, stitch_path, timeslice_naming)

    preview: typing.Dict[str, typing.Union[typing.List, str]] = {
>>>>>>> de6ea1d (Update: update to new plugin standard:)
        "outputDir": [],
    }

    for filename in output_filenames:
<<<<<<< HEAD
        preview["outputDir"].append(filename)

    with Path.open(out_dir / "preview.json", "w") as fw:
        json.dump(preview, fw, indent=2)


=======
        preview["outputDir"].append(filename) 
    
    with open( out_dir / "preview.json", "w") as fw:
        json.dump(preview, fw, indent=2)

>>>>>>> de6ea1d (Update: update to new plugin standard:)
@app.command()
def main(
    img_path: Path = typer.Option(
        ...,
        "--imgPath",
        "-i",
<<<<<<< HEAD
        help="""Absolute path to the input image collection
        directory to be processed by this plugin.""",
    ),
    stitch_path: Path = typer.Option(
        ...,
        "--stitchPath",
        "-s",
        help="Absolute path to a stitching vector directory.",
    ),
    out_dir: Path = typer.Option(
        ...,
        "--outDir",
        "-o",
        help="Absolute path to the output collection directory.",
    ),
    timeslice_naming: bool = typer.Option(
        False,
        "--timesliceNaming",
        "-t",
        help="Use timeslice number as image name.",
    ),
    preview: bool = typer.Option(
        False,
        "--preview",
        "-p",
        help="Generate preview of expected outputs.",
    ),
) -> None:
    """Assemble images from a single stitching vector."""
=======
        help="Absolute path to the input image collection directory to be processed by this plugin.",
    ),
    stitch_path: Path = typer.Option(
        ..., "--stitchPath", "-s", help="Absolute path to a stitching vector directory."
    ),
    out_dir: Path = typer.Option(
        ..., "--outDir", "-o", help="Absolute path to the output collection directory."
    ),
    timeslice_naming: bool = typer.Option(
        False, "--timesliceNaming", "-t", help="Use timeslice number as image name.",
    ),
    preview: bool = typer.Option(
        False, "--preview", "-p", help="Generate preview of expected outputs."
    )
):
    """Assemble images from a single stitching vector."""

>>>>>>> de6ea1d (Update: update to new plugin standard:)
    logger.info(f"imgPath: {img_path}")
    logger.info(f"stitchPath: {stitch_path}")
    logger.info(f"outDir: {out_dir}")
    logger.info(f"timesliceNaming: {timeslice_naming}")

<<<<<<< HEAD
    if not img_path.exists():
        msg = "imgPath does not exist"
        raise ValueError(msg, img_path)

    if not out_dir.exists():
        msg = "outDir does not exist"
        raise ValueError(msg, out_dir)

    if not stitch_path.exists():
        msg = "stitchPath does not exist"
        raise ValueError(msg, stitch_path)

    # if the input image collection contains a images subdirectory, we use that
    # TODO this is an artifact from WIPP integration.
    # This should eventually be removed from the implementation.
=======
    if(not img_path.exists()) :
        raise ValueError("imgPath does not exist", img_path)
    
    if(not img_path.exists()) :
        raise ValueError("outDir does not exist", out_dir)
    
    if(not stitch_path.exists()) :
        raise ValueError("stitchPath does not exist", stitch_path)

    # if the input image collection contains a images subdirectory, we use that
    # TODO this is an artifact from WIPP integration.This should eventually be removed from the implementation.
>>>>>>> de6ea1d (Update: update to new plugin standard:)
    if img_path.joinpath("images").is_dir():
        img_path = img_path.joinpath("images")
        logger.warning(f"imgPath : images subdirectory found so using that: {img_path}")

<<<<<<< HEAD
    if preview:
        generate_preview(img_path, stitch_path, out_dir, timeslice_naming)
        logger.info(f"generating preview data in {out_dir}")
        return

    assemble_images(img_path, stitch_path, out_dir, timeslice_naming)
=======
    if(preview):
        generate_preview(img_path, out_dir, stitch_path, timeslice_naming)
        logger.info(f"generating preview data in {out_dir}")
        return

    assemble_image(img_path, stitch_path, out_dir, timeslice_naming)
>>>>>>> de6ea1d (Update: update to new plugin standard:)


if __name__ == "__main__":
    app()