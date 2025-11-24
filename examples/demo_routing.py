import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models import FilePreview
from src.router import DocumentRouter

def main():
    print("🚦 Smart Router Kit - Demo")
    print("==========================")
    
    # Initialize Router (Mock LLM for demo)
    router = DocumentRouter()
    
    # Example 1: An Invoice
    invoice_text = """
    INVOICE #2024-001
    Date: 2024-11-24
    
    Item          | Qty | Price
    --------------|-----|-------
    Consulting    | 10  | 150.00
    Server Setup  | 1   | 500.00
    
    Total: 2000.00 EUR
    """
    
    file1 = FilePreview(
        filename="invoice_nov.pdf",
        preview_text=invoice_text
    )
    
    decision1 = router.route(file1)
    print(f"\n📄 File: {file1.filename}")
    print(f"   -> Collection: {decision1.target_collection}")
    print(f"   -> Strategy:   {decision1.chunking_strategy}")
    print(f"   -> Reasoning:  {decision1.reasoning}")
    
    # Example 2: Python Code
    code_text = """
    def analyze_data(data: List[float]) -> Dict[str, float]:
        \"\"\"Calculates statistics for the dataset.\"\"\"
        return {
            "mean": sum(data) / len(data),
            "max": max(data)
        }
    """
    
    file2 = FilePreview(
        filename="utils.py",
        preview_text=code_text
    )
    
    decision2 = router.route(file2)
    print(f"\n📄 File: {file2.filename}")
    print(f"   -> Collection: {decision2.target_collection}")
    print(f"   -> Strategy:   {decision2.chunking_strategy}")
    print(f"   -> Reasoning:  {decision2.reasoning}")

if __name__ == "__main__":
    main()
