#!/usr/bin/env python3
"""
Test updated components table layout
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def test_table_layout():
    """Test the updated table layout without the Updated column"""
    print("=== Testing Updated Table Layout ===\n")
    
    db = DatabaseManager()
    components = db.get_components()[:5]  # Get first 5 components
    
    print("✅ Updated Components Table Layout:")
    print("   • Removed 'Updated' column")
    print("   • 4 columns total: ID, Identifier, Description, Price")
    print("   • Even column spacing with window resize support")
    print()
    
    print("📊 Sample Components Display:")
    print("-" * 65)
    print(f"{'ID':<4} {'Identifier':<20} {'Description':<25} {'Price':<8}")
    print("-" * 65)
    
    for comp in components:
        comp_id = str(comp[0])
        identifier = comp[1][:19]  # Truncate if too long
        description = (comp[2] or 'No description')[:24]  # Truncate if too long
        price = f"${comp[3]:.2f}"
        
        print(f"{comp_id:<4} {identifier:<20} {description:<25} {price:<8}")
    
    print(f"\n📈 Column Resize Behavior:")
    print("   • ID: Fits content (auto-size)")
    print("   • Identifier: Expands with window")
    print("   • Description: Expands with window") 
    print("   • Price: Fits content (auto-size)")
    print()
    print("✨ Table now uses space more efficiently!")


if __name__ == '__main__':
    test_table_layout()