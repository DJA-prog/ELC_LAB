#!/usr/bin/env python3
"""
Test duplicate handling during CSV import
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def test_duplicate_handling():
    """Test how duplicates are handled during import"""
    print("=== Testing Duplicate Handling ===\n")
    
    db = DatabaseManager()
    
    # Check some specific components that should have been updated
    test_components = [
        "LM317",      # Should have been updated (higher price in CSV: 7 vs existing)
        "IRFZ44",     # Should have been updated (higher price in CSV: 11.5 vs 3.4)  
        "74LS00",     # Should have been updated (higher price in CSV: 25 vs existing)
        "LM741",      # Should check which one was kept
        "RES-1K",     # This was in sample data, check if it was updated
    ]
    
    print("Checking how duplicates were handled:\n")
    
    for identifier in test_components:
        component = db.get_component_by_identifier(identifier)
        if component:
            print(f"{identifier}:")
            print(f"  Current price: ${component[3]:.2f}")
            print(f"  Description: {component[2] or 'No description'}")
            print()
    
    # Show all LM317 variations to see how similar components were handled
    print("Looking for LM317 variations:")
    all_components = db.get_components()
    lm317_components = [comp for comp in all_components if 'LM317' in comp[1].upper()]
    
    for comp in lm317_components:
        print(f"  {comp[1]}: ${comp[3]:.2f} - {comp[2] or 'No description'}")


if __name__ == '__main__':
    test_duplicate_handling()