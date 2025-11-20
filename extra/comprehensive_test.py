#!/usr/bin/env python3
"""
Comprehensive test of the updated import logic
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def comprehensive_test():
    """Test all scenarios of the updated import logic"""
    print("=== Comprehensive Import Logic Test ===\n")
    
    db = DatabaseManager()
    
    # First, add some test components to the database
    print("Setting up test data...")
    test_data = [
        ("COMP-A", "Original description", 10.0),
        ("COMP-B", "", 5.0),  # No description
        ("COMP-C", "Has description", 8.0),
        ("COMP-D", "", 3.0),  # No description
    ]
    
    for identifier, desc, price in test_data:
        # Check if exists first
        existing = db.get_component_by_identifier(identifier)
        if not existing:
            db.insert_component(identifier, desc, price)
    
    # Create a test CSV with various scenarios
    csv_content = """ITEM,PRICE,DESCRIPTION
COMP-A,15.0,New description
COMP-B,5.0,Added description
COMP-C,8.0,
COMP-D,2.0,Lower price
NEW-COMP-1,12.0,
NEW-COMP-2,7.5,Has description
NEW-COMP-3,1.0,"""
    
    with open('/tmp/comprehensive_test.csv', 'w') as f:
        f.write(csv_content)
    
    print("Test scenarios:")
    print("• COMP-A: Higher price ($15 vs $10) - should update")
    print("• COMP-B: Same price, CSV has description - should update") 
    print("• COMP-C: Same price, existing has description, CSV doesn't - should keep existing")
    print("• COMP-D: Lower price ($2 vs $3) - should keep existing")
    print("• NEW-COMP-1: New component without description - should import")
    print("• NEW-COMP-2: New component with description - should import")
    print("• NEW-COMP-3: New component without description - should import")
    print()
    
    # Perform import
    results = db.import_csv_components('/tmp/comprehensive_test.csv')
    
    print("Import Results:")
    print(f"• New components imported: {results['imported']}")
    print(f"• Existing components updated: {results['updated']}")
    print(f"• Components skipped: {results['skipped']}")
    print()
    
    # Verify results
    print("Final state:")
    test_components = ["COMP-A", "COMP-B", "COMP-C", "COMP-D", "NEW-COMP-1", "NEW-COMP-2", "NEW-COMP-3"]
    
    for identifier in test_components:
        comp = db.get_component_by_identifier(identifier)
        if comp:
            print(f"  {identifier}: ${comp[3]:.1f} - {comp[2] or 'No description'}")
    
    # Clean up
    os.remove('/tmp/comprehensive_test.csv')
    
    print("\n✅ Comprehensive test completed!")


if __name__ == '__main__':
    comprehensive_test()