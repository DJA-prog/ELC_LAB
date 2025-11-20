#!/usr/bin/env python3
"""
Standalone CSV import script for component manager
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def import_components_csv(csv_file_path):
    """Import components from CSV file with detailed reporting"""
    print("=== Component CSV Import Tool ===\n")
    
    if not os.path.exists(csv_file_path):
        print(f"❌ Error: CSV file not found: {csv_file_path}")
        return
    
    db = DatabaseManager()
    
    # Get initial state
    initial_components = db.get_components()
    print(f"Initial components in database: {len(initial_components)}")
    
    print(f"Importing from: {csv_file_path}")
    print("\nImport rules:")
    print("• New components: Always imported (with or without description)")
    print("• Duplicate handling:")
    print("  - Higher price overwrites existing component")
    print("  - Same price: prefer component with description")
    print("  - Lower price: keep existing component")
    print("\nProcessing...")
    
    try:
        results = db.import_csv_components(csv_file_path)
        
        print(f"\n✅ Import completed successfully!")
        print(f"\nResults:")
        print(f"  📥 New components imported: {results['imported']}")
        print(f"  🔄 Existing components updated: {results['updated']}")
        print(f"  ⏭️  Components skipped (lower price/no description): {results['skipped']}")
        if results['errors'] > 0:
            print(f"  ❌ Errors encountered: {results['errors']}")
        
        # Final state
        final_components = db.get_components()
        print(f"\nFinal components in database: {len(final_components)}")
        print(f"Net increase: +{len(final_components) - len(initial_components)} components")
        
    except Exception as e:
        print(f"❌ Import failed: {e}")


def main():
    if len(sys.argv) > 1:
        csv_file_path = sys.argv[1]
    else:
        # Default to the provided CSV file
        csv_file_path = "/home/dino/Python/ELC_LAB/imports/components.csv"
    
    import_components_csv(csv_file_path)


if __name__ == '__main__':
    main()