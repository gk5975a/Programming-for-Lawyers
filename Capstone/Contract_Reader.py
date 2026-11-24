from pathlib import Path

def read_txt(path):
   
    """
    Extract text from a plain text file.
    """ 

    # content = path.read_text(
    #     encoding="utf-8",
    #     errors="replace"
    # )

    with open(path, mode="r", encoding="utf-8", errors="replace") as file:
     content = file.read()

    sections = []

    for page_number, page_text in enumerate(
        content.split("\f"), start=1
    ):
        # print ({page_number})
        # print ({page_text})
        sections.append({
            "source": path.name,
            "page_number": page_number,
            "location": f"Text page {page_number}",
            "text": page_text.strip()
        })
        print ([sections]["source"])
        print ([sections]["page_number"])
    return sections

# Main function that reads the contract in txt format.

def read_contract(file_path):
    
    path = Path(file_path)
    sections = read_txt(path)
    # Remove empty sections.
    sections = [
        section for section in sections
        if section["text"].strip()
    ]

    if not sections:
        raise ValueError(
            "No readable text was found in this contract. "
            "The document may be scanned or empty."
        )

    return sections