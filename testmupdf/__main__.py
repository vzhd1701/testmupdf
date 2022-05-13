from pathlib import Path

import fitz
import argparse


def _get_pdf_first_page_png(pdf_bin: bytes):
    doc = fitz.open("pdf", pdf_bin)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    return pix.tobytes()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract first page of PDF as PNG image."
    )
    parser.add_argument("pdf", type=argparse.FileType("rb"), help="PDF file")
    parser.add_argument("-o", type=Path, required=True, help="Output PNG")

    args = parser.parse_args()

    png_data = _get_pdf_first_page_png(args.pdf.read())
    if args.o:
        args.o.write_bytes(png_data)
