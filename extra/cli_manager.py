#!/usr/bin/env python3
"""
Command Line Interface for Component Manager
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def show_menu():
    print("\n=== Component Manager CLI ===")
    print("1. View all components")
    print("2. View all categories") 
    print("3. Add component")
    print("4. Add category")
    print("5. Link component to category")
    print("6. Show component categories")
    print("7. Show category components")
    print("8. Exit")
    print("=" * 30)


def view_components(db):
    components = db.get_components()
    print(f"\n{len(components)} Components:")
    print("-" * 60)
    for comp in components:
        print(f"ID: {comp[0]:<3} | {comp[1]:<15} | ${comp[3]:<6.2f} | {comp[2] or 'No description'}")


def view_categories(db):
    categories = db.get_categories()
    print(f"\n{len(categories)} Categories:")
    print("-" * 40)
    for cat in categories:
        print(f"ID: {cat[0]:<3} | {cat[1]:<15} | {cat[2] or 'No description'}")


def add_component(db):
    print("\nAdd New Component:")
    identifier = input("Identifier (required): ").strip()
    if not identifier:
        print("❌ Identifier is required!")
        return
    
    description = input("Description (optional): ").strip()
    try:
        price = float(input("Price (default 0.0): ") or "0.0")
    except ValueError:
        price = 0.0
    
    comp_id = db.insert_component(identifier, description, price)
    print(f"✅ Component added with ID: {comp_id}")


def add_category(db):
    print("\nAdd New Category:")
    name = input("Category name (required): ").strip()
    if not name:
        print("❌ Category name is required!")
        return
    
    description = input("Description (optional): ").strip()
    
    cat_id = db.insert_category(name, description)
    print(f"✅ Category added with ID: {cat_id}")


def link_component_category(db):
    print("\nLink Component to Category:")
    
    # Show available components
    components = db.get_components()
    print("\nAvailable Components:")
    for comp in components[:10]:  # Show first 10
        print(f"  {comp[0]}: {comp[1]}")
    if len(components) > 10:
        print(f"  ... and {len(components) - 10} more")
    
    try:
        comp_id = int(input("Component ID: "))
    except ValueError:
        print("❌ Invalid component ID!")
        return
    
    # Show available categories
    categories = db.get_categories()
    print("\nAvailable Categories:")
    for cat in categories:
        print(f"  {cat[0]}: {cat[1]}")
    
    try:
        cat_id = int(input("Category ID: "))
    except ValueError:
        print("❌ Invalid category ID!")
        return
    
    success = db.link_component_category(comp_id, cat_id)
    if success:
        print("✅ Link created successfully!")
    else:
        print("⚠️  Link already exists!")


def show_component_categories(db):
    try:
        comp_id = int(input("Enter Component ID: "))
    except ValueError:
        print("❌ Invalid component ID!")
        return
    
    categories = db.get_component_categories(comp_id)
    if categories:
        print(f"\nCategories for Component ID {comp_id}:")
        for cat in categories:
            print(f"  - {cat[1]}: {cat[2] or 'No description'}")
    else:
        print(f"No categories found for Component ID {comp_id}")


def show_category_components(db):
    try:
        cat_id = int(input("Enter Category ID: "))
    except ValueError:
        print("❌ Invalid category ID!")
        return
    
    components = db.get_category_components(cat_id)
    if components:
        print(f"\nComponents for Category ID {cat_id}:")
        for comp in components:
            print(f"  - {comp[1]}: ${comp[3]:.2f} - {comp[2] or 'No description'}")
    else:
        print(f"No components found for Category ID {cat_id}")


def main():
    db = DatabaseManager()
    
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                view_components(db)
            elif choice == '2':
                view_categories(db)
            elif choice == '3':
                add_component(db)
            elif choice == '4':
                add_category(db)
            elif choice == '5':
                link_component_category(db)
            elif choice == '6':
                show_component_categories(db)
            elif choice == '7':
                show_category_components(db)
            elif choice == '8':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please enter 1-8.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == '__main__':
    main()