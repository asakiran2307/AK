from pathlib import Path

def read_document(path,max_chars=50000):
    p=Path(path).expanduser().resolve()
    if not p.is_file(): return f"Document not found: {p}"
    suffix=p.suffix.lower()
    if suffix in {".txt",".md",".json",".csv",".log"}:
        return p.read_text(encoding="utf-8",errors="replace")[:max_chars]
    if suffix==".pdf":
        try:
            from pypdf import PdfReader
            text=[]
            for page in PdfReader(str(p)).pages:
                text.append(page.extract_text() or "")
            return "\n".join(text)[:max_chars]
        except ImportError:
            return "Install pypdf for PDF text extraction."
        except Exception as exc:
            return f"PDF extraction failed: {exc}"
    return "This document type is not enabled yet."
