import PIL
from PIL import Image
import fire
from pathlib import Path
import tqdm


def main(inppath="", outpath="", quality=95, sim=False):
    inppath = Path(inppath)
    outpath = Path(outpath)
    
    if not sim:
        outpath.mkdir(parents=True, exist_ok=True)
    
    for filename in (list(inppath.glob("**/*.png")) + list(inppath.glob("**/*.jpg"))):
        relfilename = filename.relative_to(inppath)
        outf = outpath / f"{relfilename}.Q{quality}.jpg"
        print(f"{filename} -> {outf}")
        if not sim:
            img = Image.open(filename)
            outf.parent.mkdir(parents=True, exist_ok=True)
            if quality == 100:
                img.save(outf, format="jpeg", quality=quality, subsampling=0)
            else:
                img.save(outf, format="jpeg", quality=quality)
        


if __name__ == "__main__":
    fire.Fire(main)