#!/usr/bin/env python3
"""
Test script for CSV import functionality
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def test_csv_import():
    """Test the CSV import functionality"""
    print("=== Testing CSV Import ===\n")
    
    db = DatabaseManager()
    
    # Get initial count
    initial_components = db.get_components()
    print(f"Initial components count: {len(initial_components)}")
    
    # Test import
    csv_file_path = "/home/dino/Python/ELC_LAB/imports/components.csv"
    
    try:
        results = db.import_csv_components(csv_file_path)
        
        print(f"\nImport Results:")
        print(f"• New components imported: {results['imported']}")
        print(f"• Existing components updated: {results['updated']}")
        print(f"• Components skipped: {results['skipped']}")
        print(f"• Errors encountered: {results['errors']}")
        
        # Get final count
        final_components = db.get_components()
        print(f"\nFinal components count: {len(final_components)}")
        print(f"Net increase: {len(final_components) - len(initial_components)}")
        
        # Show some examples of imported components
        print(f"\nSample of imported/updated components:")
        for i, comp in enumerate(final_components[-10:]):  # Last 10 components
            print(f"  {comp[1]}: ${comp[3]:.2f} - {comp[2] or 'No description'}")
        
        print("\n✅ CSV Import test completed successfully!")
        
    except Exception as e:
        print(f"❌ Import failed: {e}")


if __name__ == '__main__':
    test_csv_import()