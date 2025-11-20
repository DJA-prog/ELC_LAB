#!/usr/bin/env python3
"""
Debug the category update issue
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager

def debug_category_issue():
    """Debug the category update issue"""
    
    print("Debugging Category Update Issue...")
    print("=" * 50)
    
    # Initialize database manager
    db_manager = DatabaseManager()
    
    # Get a component to test
    components = db_manager.get_components()
    if components:
        test_component = components[0]
        print("Component data structure:")
        print(f"Raw data: {test_component}")
        print(f"Length: {len(test_component)}")
        
        # Try to unpack it correctly
        try:
            component_id, identifier, description, price, created_at, updated_at, quantity, category = test_component
            print(f"\nUnpacked correctly:")
            print(f"ID: {component_id}")
            print(f"Identifier: {identifier}")
            print(f"Description: {description}")
            print(f"Price: {price}")
            print(f"Quantity: {quantity}")
            print(f"Category: {category}")
            print(f"Created: {created_at}")
            print(f"Updated: {updated_at}")
            
            # Test the update method step by step
            print(f"\nTesting update_component method...")
            print(f"Current category: {category}")
            new_category = "TEST_CATEGORY"
            
            print(f"Calling update_component with:")
            print(f"  component_id: {component_id}")
            print(f"  identifier: {identifier}")
            print(f"  description: {description}")
            print(f"  price: {price}")
            print(f"  quantity: {quantity}")
            print(f"  category: {new_category}")
            
            # Update the component
            db_manager.update_component(
                component_id, identifier, description, price, quantity, new_category
            )
            
            # Check the result
            updated_component = db_manager.get_component_by_id(component_id)
            print(f"\nAfter update:")
            print(f"Raw data: {updated_component}")
            
            if updated_component:
                upd_id, upd_identifier, upd_description, upd_price, upd_created_at, upd_updated_at, upd_quantity, upd_category = updated_component
                print(f"Updated category: {upd_category}")
                print(f"Updated timestamp: {upd_updated_at}")
                
                # Restore original
                db_manager.update_component(
                    component_id, identifier, description, price, quantity, category
                )
                print(f"Restored to original category: {category}")
            
        except Exception as e:
            print(f"Error unpacking: {e}")
    else:
        print("No components found in database")

if __name__ == "__main__":
    debug_category_issue()