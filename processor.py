from docling.document_converter import DocumentConverter
import re
from langchain_core.documents import Document as LangchainDocument

def get_splits_from_all_docs(file_list):
    converter = DocumentConverter()
    all_chunks = []

    for file_path in file_list:
        result = converter.convert(file_path)
        md_text = result.document.export_to_markdown()

        sections = re.split(r'\n#{1,3} ', md_text)

        for section in sections:
            section = section.strip()
            if len(section) < 100:
                continue

            all_chunks.append(
                LangchainDocument(
                    page_content=section,
                    metadata={"source": file_path} 
                )
            )
    
    return all_chunks