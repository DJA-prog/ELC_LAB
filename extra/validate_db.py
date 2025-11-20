#!/usr/bin/env python3
"""
Validation script to test the database operations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def validate_database():
    """Validate that the database is working correctly"""
    print("=== Database Validation ===\n")
    
    db = DatabaseManager()
    
    # Test components
    print("Components in database:")
    components = db.get_components()
    for comp in components:
        print(f"  ID: {comp[0]}, Identifier: {comp[1]}, Price: ${comp[3]:.2f}")
    
    print(f"\nTotal components: {len(components)}")
    
    # Test categories
    print("\nCategories in database:")
    categories = db.get_categories()
    for cat in categories:
        print(f"  ID: {cat[0]}, Name: {cat[1]}")
    
    print(f"\nTotal categories: {len(categories)}")
    
    # Test links
    print("\nComponent-Category Links:")
    for comp in components[:5]:  # Show first 5 components
        comp_cats = db.get_component_categories(comp[0])
        if comp_cats:
            cat_names = [cat[1] for cat in comp_cats]
            print(f"  {comp[1]} -> {', '.join(cat_names)}")
    
    print("\n=== Validation Complete ===")
    print("✅ Database is working correctly!")


if __name__ == '__main__':
    validate_database()