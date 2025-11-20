#!/usr/bin/env python3
"""
Test script for the new Category Settings functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager

def test_category_functionality():
    """Test the category settings functionality"""
    
    print("Testing Category Settings Functionality...")
    print("=" * 50)
    
    # Initialize database manager
    db_manager = DatabaseManager()
    
    # Test 1: Check standard categories
    print("\n1. Current Standard Categories:")
    for i, category in enumerate(db_manager.STANDARD_CATEGORIES, 1):
        print(f"   {i}. {category}")
    
    # Test 2: Get some sample components
    print("\n2. Sample Components and their Categories:")
    components = db_manager.get_components()[:5]  # Get first 5 components
    
    if components:
        for component in components:
            component_id, identifier, description, price, quantity, category, created_at, updated_at = component
            print(f"   ID: {component_id}, Identifier: {identifier}, Category: {category or 'Not Set'}")
    else:
        print("   No components found in database")
    
    # Test 3: Test updating a component category (if components exist)
    if components:
        test_component = components[0]
        component_id, identifier, description, price, quantity, old_category, _, _ = test_component
        
        print(f"\n3. Testing category update for component '{identifier}':")
        print(f"   Original category: {old_category}")
        
        # Update to a different category
        new_category = "RESISTOR" if old_category != "RESISTOR" else "CAPACITOR"
        
        try:
            db_manager.update_component(
                component_id, identifier, description, price, quantity, new_category
            )
            print(f"   Updated category to: {new_category}")
            
            # Verify the update
            updated_component = db_manager.get_component_by_id(component_id)
            if updated_component:
                _, _, _, _, _, actual_category, _, _ = updated_component
                print(f"   Verified category: {actual_category}")
                
                # Restore original category
                db_manager.update_component(
                    component_id, identifier, description, price, quantity, old_category
                )
                print(f"   Restored original category: {old_category}")
            
        except Exception as e:
            print(f"   Error during update: {e}")
    
    # Test 4: Test adding a new custom category
    print("\n4. Testing custom category management:")
    original_categories = db_manager.STANDARD_CATEGORIES.copy()
    print(f"   Original category count: {len(original_categories)}")
    
    # Add a test category
    test_category = "TEST_CATEGORY"
    if test_category not in db_manager.STANDARD_CATEGORIES:
        db_manager.STANDARD_CATEGORIES.append(test_category)
        print(f"   Added test category: {test_category}")
        print(f"   New category count: {len(db_manager.STANDARD_CATEGORIES)}")
        
        # Remove the test category
        db_manager.STANDARD_CATEGORIES.remove(test_category)
        print(f"   Removed test category: {test_category}")
        print(f"   Final category count: {len(db_manager.STANDARD_CATEGORIES)}")
    
    print("\n" + "=" * 50)
    print("Category Settings functionality test completed!")
    print("The new 'Category Settings' tab should provide:")
    print("• View and edit component categories")
    print("• Manage standard category list")
    print("• Bulk category assignment")
    print("• Search and filter components")

if __name__ == "__main__":
    test_category_functionality()