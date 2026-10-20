import typer
from pathlib import Path

Folders = {
    "Documents": (".pdf", ".pptx", ".docx", ".md"),
    "Pictures": (".jpeg", ".jpg", ".png", ".gif"),
    "Videos": (".mkv", ".mp4"),
    "Archives": (".zip", ".dmg", ".7z"),
    "Audio": (".mp3", ".wav"),
}

app = typer.Typer()

@app.command()
def tidy(path: str):
    file = Path(path)

    for item in file.iterdir():
        suffix = item.suffix.lower()
        if item.is_file():
            for folder, exist in Folders.items():
                if suffix in exist:
                    print(item.name, folder)
                    break
            else:
                print(item.name, "Others")

if __name__ == "__main__":
    app()