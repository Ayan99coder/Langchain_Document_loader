# LangChain Document Loader Examples

Small Python examples for loading documents with LangChain and optionally
summarizing their contents with Google Gemini.

## Examples

| File | Purpose |
| --- | --- |
| `text_loader.py` | Loads `poem.txt` and generates a summary with Gemini |
| `pdf_loader.py` | Loads pages from `Ayan_Resume_Updated.pdf` |
| `csv_loader.py` | Loads `flights.csv` with `CSVLoader` |
| `document_loader.py` | Loads PDFs from a directory with `DirectoryLoader` |
| `webbase_loader.py` | Loads a web page and asks Gemini a question about it |

## Requirements

- Python 3.10 or newer
- A Google Gemini API key for `text_loader.py` and `webbase_loader.py`

Install the Python dependencies:

```bash
pip install langchain langchain-community langchain-core langchain-google-genai python-dotenv pypdf beautifulsoup4
```

## Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

Do not commit `.env` or any other secret credentials.

## Running the examples

Run an example from the project root:

```bash
python csv_loader.py
python pdf_loader.py
python text_loader.py
python webbase_loader.py
```

`document_loader.py` is configured to discover PDF files from the current
directory. Update its `path` and `glob` values when loading PDFs from a
different folder.

## Notes

- `flights.csv` is a large sample dataset used by `csv_loader.py`.
- The Gemini examples make an external API request and may incur usage costs.
- The sample scripts print loaded document content directly to the terminal.
